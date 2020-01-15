# -*- coding: utf-8 -*-

import socket
import time

# 字符串转二进制字节
# s = "example"                      # str object
# bin = bytes(s, encoding = "utf8")  # str to bytes
# bin = str.encode(s)                # str to bytes

# 二进制转字符串
# b = b"example"                     # bytes object
# str = str(b, encoding = "utf8")    # bytes to str
# str = bytes.decode(b)              # bytes to str


class SocketClient(object):
    def connect(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        time.sleep(1)
        sock.send(str.encode('1'))
        print(sock.recv(1024))
        sock.close()


if __name__ == "__main__":
    client = SocketClient()
    client.connect('127.0.0.1', 9090)
