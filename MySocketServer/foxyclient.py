# -*- encoding: utf-8 -*-
"""
@File           : foxyclient
@Time           : 2020/1/12
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import socket

ip = ('127.0.0.1', 8000)
sk = socket.socket()
sk.connect(ip)
sk.settimeout(10)
while True:
    data = sk.recv(1024)
    print('receive: %s', data)
    inp = raw_input('please input:')
    sk.sendall(bytes(inp))
    if inp == 'exit':
        break

sk.close()
