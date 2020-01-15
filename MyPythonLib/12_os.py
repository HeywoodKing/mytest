# -*- coding: utf-8 -*-

import os

print(os.getcwd())
# 改变当前工作目录
# os.chdir('F:/')
# print(os.getcwd())
# os.system('mkdir today')
# print(dir(os))
# print(help(os))
# print(os.__doc__)
# print(os.__dict__)

if os.path.exists('tomorrow'):
    os.rmdir('tomorrow')
else:
    os.mkdir('tomorrow')
    # os.rename('tomorrow', 'tomorrow2')
    # print(os.name, os.st, os.altsep)

print(os.curdir, os.defpath)
# print(os.devnull)
print(os.environ)
# print(os.error.filename, os.error.errno)
# print(os.F_OK)
# print(os.fsdecode, os.fsencode)


