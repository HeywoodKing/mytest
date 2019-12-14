# -*- encoding: utf-8 -*-
"""
@File           : scheduler.py
@Time           : 2019/11/20 17:13
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
from multiprocessing import Process
from threading import Thread

# from MyWxPy.mywxpy.setting import *
from MyWxPy.mywxpy.loader import *


class Scheduler(object):
    def __init__(self):
        pass

    def scheduler_loader(self):
        loader = Loader()
        loader.run()

    def run(self):
        if ROBOT_ENABLE:
            if START_DAEMON_TYPE.lower() == 'process':
                process = Process(target=self.scheduler_loader,)
                process.start()

            elif START_DAEMON_TYPE.lower() == 'thread':
                thread = Thread(target=self.scheduler_loader,)
                thread.start()
        else:
            print('启动机器人开关未开启！')

