# -*- encoding: utf-8 -*-
"""
@File           : test
@Time           : 2020/2/8
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
from MyParamiko.paramikoclient import ParamikoClient
import time


def put_callback(size1, size2):
    print(size1, size2)


client = ParamikoClient('config.ini')
client.connect()
client.run_cmd('date')

sftp_client = client.get_sftp_client()
sftp_client.put('/home/flack/Github/MyTest/MyParamiko/config.ini', '/home/flack/config.ini', put_callback)

client.run_cmd('md5sum /home/flack/config.ini')
