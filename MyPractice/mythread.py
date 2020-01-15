# -*- coding: UTF-8 -*-

import threading
import time

exitFlag = 0


class MyThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print('Starting %s' % self.name)
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        # 释放锁
        threadLock.release()
        print('Exiting %s' % self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print('%s: %s' % (thread_name, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = MyThread(1, 'Thread1', 1)
thread2 = MyThread(2, 'Thread2', 2)

# 开启线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print('Exiting Main Thread')






