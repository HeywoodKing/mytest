# MyTranslate

## 安装(一定要全局安装，这样才能在任何地方打开终端窗口就能使用)
```
pip3 install pytranslate -i https://pypi.douban.com/simple
或
pipenv install pytranslate
```

## 使用
```
Usage: trans [OPTIONS] word

Options:
  --where             Output project home information.
  --envs              Output Environment Variable options.
  --man               Display manpage.
  --support           Output diagnostic information for use in GitHub issues.
  --clear             Clears caches
  -y                  使用有道翻译源
  -b                  使用百度翻译源
  -g                  使用谷歌翻译源
  -p                  使用金山词霸翻译源
  -v, --version       Show the version and exit.
  -h, --help          Show this message and exit.

Usage Examples:
   检测翻译源是否可用:
   $ trans check

   进入翻译环境:
   $ trans shell 

Commands:
  check      Checks for security vulnerabilities and against PEP 508 markers
             provided in Pipfile.
  clean      清理翻译缓存.
  shell      Spawns a shell within the virtualenv.
  update     更新翻译缓存.
  upgrade    升级库版本.

```

## License
[MIT](https://github.com/ "aaa")


