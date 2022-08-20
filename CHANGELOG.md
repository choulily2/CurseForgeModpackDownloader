# Changelog

## [1.4.2](https://github.com/choulily2/CurseForgeModpackDownloader/compare/v1.4.2...v1.4.2) (2022-08-20)


### ⚠ BREAKING CHANGES

* **master:** project has been renamed to CurseForgeModpackDownloader

### Features

* ✨ add command parameters to ignore license notice ([b08807a](https://github.com/choulily2/CurseForgeModpackDownloader/commit/b08807a974578a38f673f0010ebc8f13bc32e99b))
* ✨ add debug loggings ([10452ef](https://github.com/choulily2/CurseForgeModpackDownloader/commit/10452efefa19f10993f721f15c7bd5feb7fa9023))
* ✨ add logger debug setting ([fbc648f](https://github.com/choulily2/CurseForgeModpackDownloader/commit/fbc648f735cc16920b46c1bc9302bf5b2fdaf312))
* ✨ add logger name to message ([73aef83](https://github.com/choulily2/CurseForgeModpackDownloader/commit/73aef8341c6a1e876240feb254a6c4a86d6e4230))
* ✨ add logger to factory ([b631662](https://github.com/choulily2/CurseForgeModpackDownloader/commit/b63166220a3de48b51b833b7d7eed1534577a77c))
* 🐧 add linux compatibility ([#22](https://github.com/choulily2/CurseForgeModpackDownloader/issues/22)) ([085de93](https://github.com/choulily2/CurseForgeModpackDownloader/commit/085de93b5741e8847d54d9039df4257f1acdbec7))
* 🚚 add temp dir ([536dab1](https://github.com/choulily2/CurseForgeModpackDownloader/commit/536dab1c193d161a4de341ea8294f11c1bff3e6d))
* **config:** ✨ add config file check ([23bb19e](https://github.com/choulily2/CurseForgeModpackDownloader/commit/23bb19e44052507554dace3f25feb39f5d90e35d))
* **config:** ✨ add config file to storage api key ([a3ecd95](https://github.com/choulily2/CurseForgeModpackDownloader/commit/a3ecd956b37e81063556b642c857d8fcc5ce476b))
* **download:** ✨ add download avartar (resolve [#8](https://github.com/choulily2/CurseForgeModpackDownloader/issues/8)) ([08f171f](https://github.com/choulily2/CurseForgeModpackDownloader/commit/08f171f64964daf23f542a1d00d606b15882ae48))
* **download:** 💥 add progressbar (resolve [#17](https://github.com/choulily2/CurseForgeModpackDownloader/issues/17)) ([a5fd1bb](https://github.com/choulily2/CurseForgeModpackDownloader/commit/a5fd1bb7995032efd0fc20f2eff4084d605c2235))
* **download:** 🔇 remove verify failed warning ([c22014b](https://github.com/choulily2/CurseForgeModpackDownloader/commit/c22014babb6295af1e787bbfe37a2752a4bdc14e))
* **i18n:** ✨ add lang specific param in translate method ([45d89e2](https://github.com/choulily2/CurseForgeModpackDownloader/commit/45d89e20e1d753d2da853c0c815e1cf037e78bb8))
* **i18n:** 🌐 add i18n for logs ([571923e](https://github.com/choulily2/CurseForgeModpackDownloader/commit/571923e5921b0ccfe34ddf308a7ff697e094b631))
* **i18n:** 🌐 add multilanguage (resolve [#18](https://github.com/choulily2/CurseForgeModpackDownloader/issues/18)) ([6a5ffd9](https://github.com/choulily2/CurseForgeModpackDownloader/commit/6a5ffd977f62e1fa7a77e4ee4ca73aa51b41446c))
* **requester:** ✨ add json method for Response ([3ed3dc2](https://github.com/choulily2/CurseForgeModpackDownloader/commit/3ed3dc24a4c5c26890e7135b9b79500589bb6d64))
* **requester:** ✨ add search modpack ([f8e549c](https://github.com/choulily2/CurseForgeModpackDownloader/commit/f8e549c8e42af9263804600d73f08abe4211e0b1))
* **requester:** ✨ allow params in get method ([b85da0d](https://github.com/choulily2/CurseForgeModpackDownloader/commit/b85da0d38d492eafdd0efdb0cafa295a4df77853))
* **ui:** ✨ add download function (resolve [#6](https://github.com/choulily2/CurseForgeModpackDownloader/issues/6)) ([c7de2fd](https://github.com/choulily2/CurseForgeModpackDownloader/commit/c7de2fdb0b23da60aa5c4086c7a91022ec352753))
* **ui:** ✨ add downloading progressbar ([06ed7bd](https://github.com/choulily2/CurseForgeModpackDownloader/commit/06ed7bd388ff6bb683b6e11dd228541477ed6e06))
* **ui:** ✨ add language switch combobox ([d35b407](https://github.com/choulily2/CurseForgeModpackDownloader/commit/d35b407448d55e8bc895d44b310a2e4fe92d3690))
* **ui:** ✨ add search result check ([1b67e4f](https://github.com/choulily2/CurseForgeModpackDownloader/commit/1b67e4fa85123de5e96b126265dfea56121b302d))
* **ui:** ✨ search modpacks and filter ([c478858](https://github.com/choulily2/CurseForgeModpackDownloader/commit/c478858346b7a44dc93bd21030669a452b6775e6))
* **ui:** ✨ set modpack version filter when select a modpack ([3f408a6](https://github.com/choulily2/CurseForgeModpackDownloader/commit/3f408a65115016c0a7669c8f9c28d3ca3c4cea26))
* **ui:** 💥 draw the ui ([dd63860](https://github.com/choulily2/CurseForgeModpackDownloader/commit/dd63860daadd3dc524a97f1efed8872967790df8))


### Bug Fixes

* ✏️ add acronym for spaced name ([b289b84](https://github.com/choulily2/CurseForgeModpackDownloader/commit/b289b84bd24281d329b67bbae3cc9003a3e56873))
* ➕ add PyYAML to requirements.txt for CI ([fca7cd1](https://github.com/choulily2/CurseForgeModpackDownloader/commit/fca7cd19723f1c8df6f395df4a6dd4d1f9d04bc0))
* 🐛 add base dir to constant ([3b5cfee](https://github.com/choulily2/CurseForgeModpackDownloader/commit/3b5cfee44f70b513460fe738e02430af93a024af))
* 🔥 remove downloading dir at startup ([e68d228](https://github.com/choulily2/CurseForgeModpackDownloader/commit/e68d228e92502b3d8289c596d8013c23546e039c))
* 🚑️ move api to api.curseforge.com (fix [#23](https://github.com/choulily2/CurseForgeModpackDownloader/issues/23)) ([047ab1c](https://github.com/choulily2/CurseForgeModpackDownloader/commit/047ab1cd922c84bb01caf937ff400f3a97261d1b))
* 🚑️ use working dir for temp instead of base dir ([080bcee](https://github.com/choulily2/CurseForgeModpackDownloader/commit/080bcee7a4d8971056d276ae847b0b3dbd42e87e))
* **download:** 🐛 fix avatar bugs ([67c17cb](https://github.com/choulily2/CurseForgeModpackDownloader/commit/67c17cba6fd73dd6a22c9b3c09f4b283440503f8))
* **download:** 🐛 move downloaded file out of temp dir to avoid delete ([6b60a3a](https://github.com/choulily2/CurseForgeModpackDownloader/commit/6b60a3a0a87a26886d2972cedab5beb3ef54edb4))
* **download:** 🐛 resolve special characters error ([7935939](https://github.com/choulily2/CurseForgeModpackDownloader/commit/79359398c1c12cfa48a20be1bc9ba6f65544798f))
* **download:** 🐛 set temp dir path to absolute path ([320e557](https://github.com/choulily2/CurseForgeModpackDownloader/commit/320e5570d9f39b83ebbd33458b2b67bcab254ff1))
* **download:** 🐛 stop exit when no file selected ([953b146](https://github.com/choulily2/CurseForgeModpackDownloader/commit/953b1467ea32ebc9fda28f0ac9f5981c523c0d28))
* **i18n:** 🌐 fix chinese download.getModWarning.content ([c76cd4e](https://github.com/choulily2/CurseForgeModpackDownloader/commit/c76cd4e09069c84301c496af3d33a88031d39a1f))
* **i18n:** 🐛 return a better structure of get languages ([8f42def](https://github.com/choulily2/CurseForgeModpackDownloader/commit/8f42deffb3aa175a1568e812d02b1ed2b63bfde4))
* **requester:** 🐛 specify request method ([3e19011](https://github.com/choulily2/CurseForgeModpackDownloader/commit/3e1901111ca7ce767ef8454f333e09803c6b9978))
* **ui:** ✨ fill all filter space by modpak version combobox ([da5344b](https://github.com/choulily2/CurseForgeModpackDownloader/commit/da5344ba0c65e4e87f730e21b0cd2d0ec675597b))
* **ui:** 🐛 clear data of list when not append updating ([0076bea](https://github.com/choulily2/CurseForgeModpackDownloader/commit/0076bea6da459e4853fc3e35733642c7b47dd0de))
* **ui:** 🐛 clear modpack version combobox before get new versions ([79b7e01](https://github.com/choulily2/CurseForgeModpackDownloader/commit/79b7e014fa74020f6bb58f6781e3d86878d1b866))
* **ui:** 🐛 fix modpack version filter sorting ([b7cb871](https://github.com/choulily2/CurseForgeModpackDownloader/commit/b7cb8711309e768cc1e861d52dc116d37ea8ea90))
* **ui:** 🐛 fix search index was default as 1 ([a6b2685](https://github.com/choulily2/CurseForgeModpackDownloader/commit/a6b2685877742d738300cfdd5f105f9ab1e0b6b0))
* **ui:** 🐛 give more space for modpack version in filters ([b2ed963](https://github.com/choulily2/CurseForgeModpackDownloader/commit/b2ed963a088d278498aa6b98e617100de21d11f5))
* **ui:** 🐛 make a new Download when click import button ([39713bb](https://github.com/choulily2/CurseForgeModpackDownloader/commit/39713bbb63af61c1994968eaf7961e4054643c02))
* **ui:** 🐛 open a new thread for ask license ([a6be93c](https://github.com/choulily2/CurseForgeModpackDownloader/commit/a6be93ca12e9a13ac6d483cf31ddfd6e6095b173))
* **ui:** 🐛 refresh search index when search ([f7c8f40](https://github.com/choulily2/CurseForgeModpackDownloader/commit/f7c8f40ba6bc603c785bedad39978ceb09d48ea9))
* **ui:** 🐛 reselect modpack after select modpack version (fix [#16](https://github.com/choulily2/CurseForgeModpackDownloader/issues/16)) ([558fbe4](https://github.com/choulily2/CurseForgeModpackDownloader/commit/558fbe4813ab59d38e7dbb710347ee434af533af))
* **ui:** 🐛 select first option of modpack version filter automatically when values are set ([d414159](https://github.com/choulily2/CurseForgeModpackDownloader/commit/d414159f2e6b500016efba3da406317b5b941875))
* **ui:** 🐛 sort modpack versions ([2294a87](https://github.com/choulily2/CurseForgeModpackDownloader/commit/2294a876232a0cf069aa2fbbeabd3c6b7002a391))
* **ui:** 🐛 update list when combobox selected ([cd19d56](https://github.com/choulily2/CurseForgeModpackDownloader/commit/cd19d5677d5a0e49dd4fdc9f9130e7d50cd6e307))


### Performance Improvements

* ⚡️ add debug logging estimate ([9d16b09](https://github.com/choulily2/CurseForgeModpackDownloader/commit/9d16b09c62021d4be1d3d19d2b885225c72e6dee))
* **download:** ⚡️ remove variable of thread in downloading ([693ebcc](https://github.com/choulily2/CurseForgeModpackDownloader/commit/693ebccd8f865b1d82c35d9b24158c8a9b1155ad))
* **ui:** ⚡️ save a thread while initialization ([269134e](https://github.com/choulily2/CurseForgeModpackDownloader/commit/269134e76d7fd6052b8f182f59bef503a969d417))


### Miscellaneous Chores

* **master:** 🚚 rename project ([bf0e07a](https://github.com/choulily2/CurseForgeModpackDownloader/commit/bf0e07a6fbc493239f11e98cabc9a28e519bc53f))


### Continuous Integration

* **i18n:** 💚 fix lang files packing ([b76bcec](https://github.com/choulily2/CurseForgeModpackDownloader/commit/b76bcecb356eba0828128cdfaf4d84ef9d5f9761))
* **i18n:** 💚 fix lang pack on linux ([442f00b](https://github.com/choulily2/CurseForgeModpackDownloader/commit/442f00b0ae9e3e1a2bb655933837d06552a1388c))

## [1.4.2](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/v1.4.1...v1.4.2) (2022-07-02)


### Continuous Integration

* **i18n:** 💚 fix lang pack on linux ([442f00b](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/442f00b0ae9e3e1a2bb655933837d06552a1388c))

## [1.4.1](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/v1.4.0...v1.4.1) (2022-07-02)


### Continuous Integration

* **i18n:** 💚 fix lang files packing ([b76bcec](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/b76bcecb356eba0828128cdfaf4d84ef9d5f9761))

## [1.4.0](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/v1.3.2...v1.4.0) (2022-07-02)


### Features

* ✨ add debug loggings ([10452ef](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/10452efefa19f10993f721f15c7bd5feb7fa9023))
* ✨ add logger debug setting ([fbc648f](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/fbc648f735cc16920b46c1bc9302bf5b2fdaf312))
* ✨ add logger name to message ([73aef83](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/73aef8341c6a1e876240feb254a6c4a86d6e4230))
* ✨ add logger to factory ([b631662](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/b63166220a3de48b51b833b7d7eed1534577a77c))
* **config:** ✨ add config file check ([23bb19e](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/23bb19e44052507554dace3f25feb39f5d90e35d))
* **i18n:** ✨ add lang specific param in translate method ([45d89e2](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/45d89e20e1d753d2da853c0c815e1cf037e78bb8))
* **i18n:** 🌐 add i18n for logs ([571923e](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/571923e5921b0ccfe34ddf308a7ff697e094b631))
* **i18n:** 🌐 add multilanguage (resolve [#18](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/issues/18)) ([6a5ffd9](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/6a5ffd977f62e1fa7a77e4ee4ca73aa51b41446c))
* **ui:** ✨ add language switch combobox ([d35b407](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/d35b407448d55e8bc895d44b310a2e4fe92d3690))


### Bug Fixes

* **i18n:** 🌐 fix chinese download.getModWarning.content ([c76cd4e](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/c76cd4e09069c84301c496af3d33a88031d39a1f))
* **i18n:** 🐛 return a better structure of get languages ([8f42def](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/8f42deffb3aa175a1568e812d02b1ed2b63bfde4))
* **ui:** 🐛 give more space for modpack version in filters ([b2ed963](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/b2ed963a088d278498aa6b98e617100de21d11f5))


### Performance Improvements

* ⚡️ add debug logging estimate ([9d16b09](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/9d16b09c62021d4be1d3d19d2b885225c72e6dee))

## [1.3.2](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/v1.3.1...v1.3.2) (2022-06-27)


### Bug Fixes

* **ui:** 🐛 fix modpack version filter sorting ([b7cb871](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/b7cb8711309e768cc1e861d52dc116d37ea8ea90))

## [1.3.1](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/v1.3.0...v1.3.1) (2022-06-26)


### Bug Fixes

* ➕ add PyYAML to requirements.txt for CI ([fca7cd1](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/fca7cd19723f1c8df6f395df4a6dd4d1f9d04bc0))

## [1.3.0](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/v1.2.0...v1.3.0) (2022-06-26)


### Features

* **config:** ✨ add config file to storage api key ([a3ecd95](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/a3ecd956b37e81063556b642c857d8fcc5ce476b))
* **download:** 🔇 remove verify failed warning ([c22014b](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/c22014babb6295af1e787bbfe37a2752a4bdc14e))


### Bug Fixes

* 🔥 remove downloading dir at startup ([e68d228](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/e68d228e92502b3d8289c596d8013c23546e039c))
* 🚑️ move api to api.curseforge.com (fix [#23](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/issues/23)) ([047ab1c](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/047ab1cd922c84bb01caf937ff400f3a97261d1b))


### Performance Improvements

* **download:** ⚡️ remove variable of thread in downloading ([693ebcc](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/693ebccd8f865b1d82c35d9b24158c8a9b1155ad))
* **ui:** ⚡️ save a thread while initialization ([269134e](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/269134e76d7fd6052b8f182f59bef503a969d417))

## [1.2.0](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/v1.1.2...v1.2.0) (2022-06-20)


### Features

* 🐧 add linux compatibility ([#22](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/issues/22)) ([085de93](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/085de93b5741e8847d54d9039df4257f1acdbec7))


### Bug Fixes

* **download:** 🐛 resolve special characters error ([7935939](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/79359398c1c12cfa48a20be1bc9ba6f65544798f))

## [1.1.2](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/v1.1.1...v1.1.2) (2022-06-16)


### Bug Fixes

* **ui:** 🐛 refresh search index when search ([f7c8f40](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/f7c8f40ba6bc603c785bedad39978ceb09d48ea9))

## [1.1.1](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/v1.1.0...v1.1.1) (2022-06-16)


### Bug Fixes

* 🚑️ use working dir for temp instead of base dir ([080bcee](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/080bcee7a4d8971056d276ae847b0b3dbd42e87e))

## [1.1.0](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/v1.0.0...v1.1.0) (2022-06-16)


### Features

* ✨ add command parameters to ignore license notice ([b08807a](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/b08807a974578a38f673f0010ebc8f13bc32e99b))
* 🚚 add temp dir ([536dab1](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/536dab1c193d161a4de341ea8294f11c1bff3e6d))
* **download:** ✨ add download avartar (resolve [#8](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/issues/8)) ([08f171f](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/08f171f64964daf23f542a1d00d606b15882ae48))
* **download:** 💥 add progressbar (resolve [#17](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/issues/17)) ([a5fd1bb](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/a5fd1bb7995032efd0fc20f2eff4084d605c2235))
* **requester:** ✨ add json method for Response ([3ed3dc2](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/3ed3dc24a4c5c26890e7135b9b79500589bb6d64))
* **requester:** ✨ add search modpack ([f8e549c](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/f8e549c8e42af9263804600d73f08abe4211e0b1))
* **requester:** ✨ allow params in get method ([b85da0d](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/b85da0d38d492eafdd0efdb0cafa295a4df77853))
* **ui:** ✨ add download function (resolve [#6](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/issues/6)) ([c7de2fd](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/c7de2fdb0b23da60aa5c4086c7a91022ec352753))
* **ui:** ✨ add downloading progressbar ([06ed7bd](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/06ed7bd388ff6bb683b6e11dd228541477ed6e06))
* **ui:** ✨ add search result check ([1b67e4f](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/1b67e4fa85123de5e96b126265dfea56121b302d))
* **ui:** ✨ search modpacks and filter ([c478858](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/c478858346b7a44dc93bd21030669a452b6775e6))
* **ui:** ✨ set modpack version filter when select a modpack ([3f408a6](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/3f408a65115016c0a7669c8f9c28d3ca3c4cea26))
* **ui:** 💥 draw the ui ([dd63860](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/dd63860daadd3dc524a97f1efed8872967790df8))


### Bug Fixes

* ✏️ add acronym for spaced name ([b289b84](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/b289b84bd24281d329b67bbae3cc9003a3e56873))
* 🐛 add base dir to constant ([3b5cfee](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/3b5cfee44f70b513460fe738e02430af93a024af))
* **download:** 🐛 fix avatar bugs ([67c17cb](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/67c17cba6fd73dd6a22c9b3c09f4b283440503f8))
* **download:** 🐛 move downloaded file out of temp dir to avoid delete ([6b60a3a](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/6b60a3a0a87a26886d2972cedab5beb3ef54edb4))
* **download:** 🐛 set temp dir path to absolute path ([320e557](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/320e5570d9f39b83ebbd33458b2b67bcab254ff1))
* **download:** 🐛 stop exit when no file selected ([953b146](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/953b1467ea32ebc9fda28f0ac9f5981c523c0d28))
* **requester:** 🐛 specify request method ([3e19011](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/3e1901111ca7ce767ef8454f333e09803c6b9978))
* **ui:** ✨ fill all filter space by modpak version combobox ([da5344b](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/da5344ba0c65e4e87f730e21b0cd2d0ec675597b))
* **ui:** 🐛 clear data of list when not append updating ([0076bea](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/0076bea6da459e4853fc3e35733642c7b47dd0de))
* **ui:** 🐛 clear modpack version combobox before get new versions ([79b7e01](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/79b7e014fa74020f6bb58f6781e3d86878d1b866))
* **ui:** 🐛 fix search index was default as 1 ([a6b2685](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/a6b2685877742d738300cfdd5f105f9ab1e0b6b0))
* **ui:** 🐛 make a new Download when click import button ([39713bb](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/39713bbb63af61c1994968eaf7961e4054643c02))
* **ui:** 🐛 open a new thread for ask license ([a6be93c](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/a6be93ca12e9a13ac6d483cf31ddfd6e6095b173))
* **ui:** 🐛 reselect modpack after select modpack version (fix [#16](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/issues/16)) ([558fbe4](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/558fbe4813ab59d38e7dbb710347ee434af533af))
* **ui:** 🐛 select first option of modpack version filter automatically when values are set ([d414159](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/d414159f2e6b500016efba3da406317b5b941875))
* **ui:** 🐛 sort modpack versions ([2294a87](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/2294a876232a0cf069aa2fbbeabd3c6b7002a391))
* **ui:** 🐛 update list when combobox selected ([cd19d56](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/cd19d5677d5a0e49dd4fdc9f9130e7d50cd6e307))

## [1.0.0](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/compare/0.2.3...v1.0.0) (2022-06-10)


### ⚠ BREAKING CHANGES

* **master:** project has been renamed to CurseForgeModpackDownloader

### Miscellaneous Chores

* **master:** 🚚 rename project ([bf0e07a](https://github.com/AnzhiZhang/CurseForgeModpackDownloader/commit/bf0e07a6fbc493239f11e98cabc9a28e519bc53f))
