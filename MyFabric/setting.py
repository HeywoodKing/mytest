# -*- encoding: utf-8 -*-
"""
@File           : setting.py
@Time           : 2019/12/27 19:22
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""

HOST = '192.168.1.100'
PORT = 22
USER = 'flack.chen'
PASSWORD = 'flack.chen123'
CONNECT_TIMEOUT = 10
COMPRESS_TYPE = 'gztar'

# 本地要打包的路径
LOCAL_PATH = r'E:/valid_file_txt'
# 服务器上传的文件存放路径
SERVER_PATH = r'/home/flack.chen/'
# 打包文件前缀
PACK_FILENAME = 'test_archive'
# 打包文件全名
PACK_FULL_FILENAME = '{}.tar.gz'.format(PACK_FILENAME)
