import os
import json
import shutil
import hashlib
from zipfile import ZipFile, ZIP_STORED
from concurrent.futures import ThreadPoolExecutor
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo, showwarning

from utils.constant import PATH
from utils.logger import Logger
from utils.requester import Requester


class Download:
    def __init__(
            self,
            name: str = None,
            zip_file_path: str = None,
            avatar_url: str = None
    ):
        self.name = name
        self.zip_file_path = zip_file_path
        self.avatar_url = avatar_url
        self.avatar_name = None
        self.avatar_base_name = None

        self.file_base_name = None
        self.dir_path = None
        self.log_file_path = None
        self.avatar_path = None
        self.overrides_dir_path = None
        self.manifest_path = None
        self.logger = None
        self.thread_pool = None

    def main(self):
        if not self.zip_file_path:
            self.zip_file_path = askopenfilename().replace('/', os.sep)
            if self.zip_file_path == '':
                return
        if self.avatar_url:
            name = os.path.basename(self.avatar_url)
            ext = os.path.splitext(name)[1]
            self.avatar_base_name = self.name if self.name else name
            self.avatar_base_name = self.avatar_base_name.replace('.', '_')
            self.avatar_name = self.avatar_base_name + ext

        # 计算路径
        self.file_base_name = os.path.basename(self.zip_file_path)
        self.dir_path = os.path.join(
            os.getcwd(),
            PATH.TEMP_DIR_PATH,
            self.file_base_name.replace('.zip', '')
        )
        self.log_file_path = os.path.join(self.dir_path, PATH.LOG_FILE_NAME)
        self.avatar_path = os.path.join(self.dir_path, self.avatar_name)
        self.overrides_dir_path = os.path.join(self.dir_path, 'overrides')
        self.manifest_path = os.path.join(self.dir_path, 'manifest.json')

        # 新建临时文件夹
        os.mkdir(self.dir_path)

        # 工具
        self.logger = Logger(self.log_file_path)
        self.thread_pool = ThreadPoolExecutor(4)

        # 解压文件
        self.unzip()

        try:
            with open(self.avatar_path, 'wb') as f:
                f.write(Requester.get(self.avatar_url).content)
            download_urls = self.get_download_urls()
        except:
            self.clean_file()
            showwarning('警告', '获取模组下载地址失败，这可能是由于网络不稳定，请重试')
        else:
            self.download_mods(download_urls)
            self.write_mmc_files()
            self.make_zip()
            self.clean_file()
            showinfo(
                '下载完成',
                '请直接导入启动器\n'
                '下载地址及问题反馈：\n'
                'https://github.com/AnzhiZhang/CurseForgeModpackDownloader'
            )

    def unzip(self):
        with ZipFile(self.zip_file_path) as zf:
            for i in zf.namelist():
                zf.extract(i, self.dir_path)

    def get_download_urls(self):
        # 获取下载链接 API
        with open(self.manifest_path) as f:
            data = json.load(f)
            files = data['files']

        count = len(files)
        result = []
        i = 0
        for r in self.thread_pool.map(
                lambda file: Requester.download_url(
                    file["projectID"],
                    file["fileID"]
                ), files
        ):
            i += 1
            self.logger.info(f'获取模组下载链接（{i}/{count}）')
            result.append(r.text)
        return result

    def download_mods(self, urls):
        def download(url):
            # 计算路径
            mod_name = os.path.basename(url)
            mod_path = os.path.join(mods_dir_path, mod_name)

            try:
                # 下载
                response = Requester.get(url)

                # 校验
                md5 = hashlib.md5(response.content).hexdigest()
                if md5 != response.headers['ETag'].replace('"', ''):
                    failed_mods['verify'].append(f'{mod_name}（{url}）')

                # 写入文件
                with open(mod_path, 'wb') as f:
                    f.write(response.content)
            except Exception as e:
                failed_mods['download'].append(f'{mod_name}（{url}）')
                self.logger.error(f'下载 {mod_name} 失败：{repr(e)}')

            return mod_name

        # 检查模组文件夹
        mods_dir_path = os.path.join(self.overrides_dir_path, 'mods')
        if not os.path.isdir(mods_dir_path):
            os.makedirs(mods_dir_path)

        # 下载模组
        count = len(urls)
        failed_mods = {
            'download': [],
            'verify': []
        }
        i = 0
        for name in self.thread_pool.map(download, urls):
            i += 1
            self.logger.info(f'下载模组（{i}/{count}）：{name}')

        # 提示结果
        warning_text = ''

        # 下载失败日志
        failed_download_count = len(failed_mods['download'])
        if failed_download_count > 0:
            warning_text += f'{failed_download_count} 个模组下载失败，请手动下载！\n'
            self.logger.error(
                f'{failed_download_count} 个模组下载失败，请手动下载：\n' +
                '\n'.join(failed_mods['download'])
            )

        # 验证失败日志
        failed_verify_count = len(failed_mods['verify'])
        if failed_verify_count > 0:
            warning_text += f'{failed_verify_count} 个模组校验失败，可能存在问题\n'
            self.logger.warning(
                f'{failed_verify_count} 个模组校验失败，一般无需手动下载：\n' +
                '\n'.join(failed_mods['verify'])
            )

        # 弹窗提示
        if warning_text:
            showwarning('警告', warning_text + '请查看控制台或日志获取详细信息')

    def write_mmc_files(self):
        # 获取版本信息
        with open(self.manifest_path) as f:
            data = json.load(f)['minecraft']
            minecraft_version = data['version']
            mod_loader = data['modLoaders'][0]['id']
            if mod_loader.startswith('forge'):
                mod_loader_uid = 'net.minecraftforge'
            elif mod_loader.startswith('fabric'):
                mod_loader_uid = 'net.fabricmc.fabric-loader'
            mod_loader_version = mod_loader.split('-')[-1]

        # 写入 mmc-pack.json
        mmc_pack_path = os.path.join(self.dir_path, 'mmc-pack.json')
        with open(mmc_pack_path, 'w', encoding='utf-8') as f:
            json.dump({
                'components': [
                    {
                        'uid': 'net.minecraft',
                        'version': minecraft_version
                    },
                    {
                        'uid': mod_loader_uid,
                        'version': mod_loader_version
                    }
                ],
                'formatVersion': 1
            }, f, indent=4)

        # 写入 instance.cfg
        instance_cfg_path = os.path.join(self.dir_path, 'instance.cfg')
        content = 'InstanceType=OneSix\n'
        if self.avatar_base_name:
            content += f'iconKey={self.avatar_base_name}\n'
        with open(instance_cfg_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def make_zip(self):
        # 清理 CF 文件
        modlist_path = os.path.join(self.dir_path, 'modlist.html')
        if os.path.isfile(modlist_path):
            os.remove(modlist_path)
        os.remove(self.manifest_path)
        os.rename(
            self.overrides_dir_path,
            os.path.join(self.dir_path, '.minecraft')
        )

        # 压缩
        with ZipFile(self.zip_file_path, mode='w', compression=ZIP_STORED) as z:
            for dirpath, dirnames, filenames in os.walk(self.dir_path):
                for filename in filenames:
                    zf_path = os.path.join(dirpath, filename)
                    arcname = zf_path.replace(
                        self.dir_path,
                        self.dir_path.split(os.sep)[-1]
                    )
                    z.write(zf_path, arcname=arcname)

    def clean_file(self):
        # 关闭日志
        self.logger.close()

        # 删除文件夹
        shutil.rmtree(self.dir_path)
