# -*- coding: UTF-8 -*-

import socket

s = socket.socket()

host = socket.gethostname()
port = 12345
addr = (host, port)

s.connect(addr)
data = s.recv(1024).decode()
print('接收到数据：', data)

s.close()

