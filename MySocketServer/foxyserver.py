# -*- encoding: utf-8 -*-
"""
@File           : FoxyServer
@Time           : 2020/1/12
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import SocketServer
from multiprocessing import Process


class FoxyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        conn=self.request
        conn.sendall('hello')
        while True:
            data = str(conn.recv(1024))
            conn.sendall('server:' + data)


if __name__ == '__main__':
    # 多进程监听多端口
    server1 = SocketServer.ForkingTCPServer(('127.0.0.1', 8000), FoxyServer)
    server1.max_children = 2

    server2 = SocketServer.ForkingTCPServer(('127.0.0.1', 9000), FoxyServer)
    server2.max_children = 2

    p = Process(target=server2.serve_forever, args=())
    p.start()

    # server1需放在p.start后启动不然会阻塞进程，server2无法启动
    server1.serve_forever()
    p.join()

    # # 多线程监听多端口
    # server1 = SocketServer.ThreadingTCPServer(('127.0.0.1', 8000), FoxyServer)
    # server1.max_children = 2
    #
    # server2 = SocketServer.ThreadingTCPServer(('127.0.0.1', 9000), FoxyServer)
    # server2.max_children = 2
    #
    # p = Process(target=server2.serve_forever, args=())
    # p.start()
    #
    # # server1需放在p.start后启动不然会阻塞进程，server2无法启动
    # server1.serve_forever()
    # p.join()

    pass

