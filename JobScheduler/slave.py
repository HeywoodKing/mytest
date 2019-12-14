# -*- encoding: utf-8 -*-
"""
@File           : slave.py
@Time           : 2019/11/15 16:32
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import time
from queue import Queue
from multiprocessing.managers import BaseManager
from job import Job
from queuemanager import QueueManager


class Slave(object):
    def __init__(self):
        # 派发出去的作业队列
        self.dispatched_job_queue = Queue()
        # 完成的作业队列
        self.finished_job_queue = Queue()

    def start(self):
        # 把派发作业队列和完成作业队列注册到网络上
        QueueManager.register('get_dispatched_job_queue')
        QueueManager.register('get_finished_job_queue')
        # 连接master
        server = '127.0.0.1'
        print('Connect to server %s...' % server)
        manager = QueueManager(address=(server, 9999), authkey=b'jobs')
        manager.connect()

        # 使用上面注册的方法获取队列
        dispatched_jobs = manager.get_dispatched_job_queue()
        finished_jobs = manager.get_finished_job_queue()

        # 运行作业并返回结果，这里只是模拟作业运行，所以返回的是接收到的作业
        while True:
            job = dispatched_jobs.get(timeout=1)
            print('Run job: %s ' % job.job_id)
            time.sleep(1)
            finished_jobs.put(job)


if __name__ == '__main__':
    slave = Slave()
    slave.start()
