# -*- coding: utf-8 -*-

import socket


class SocketServer(object):
    def run(self, host, port, connect_num=5):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(connect_num)
        print('socket server running...')
        while True:
            connect, address = sock.accept()
            try:
                connect.settimeout(5)
                buf = connect.recv(1024)
                # print(type(buf), bytes.decode(buf))
                if bytes.decode(buf) == '1':
                    connect.send(b'welcome to server!')
                else:
                    connect.send(b'please go out!')
            except socket.timeout:
                print('time out')
                connect.close()


if __name__ == "__main__":
    sock = SocketServer()
    sock.run('127.0.0.1', 9090)


