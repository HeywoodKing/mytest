# -*- coding: UTF-8 -*-

import socket
from time import ctime

s = socket.socket()
# s = socket.socketpair(AF_INET, SOCK_STREAM)

host = socket.gethostname()
port = 12345
address = (host, port)
s.bind(address)

s.listen(5)
while True:
    c, addr = s.accept()
    print('连接地址', addr)
    c.send(('[%s] 欢迎访问python' % ctime()).encode())
    c.close()



