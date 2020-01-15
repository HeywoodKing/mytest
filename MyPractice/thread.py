# -*- coding: UTF-8 -*-

import threading
import _thread
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s: %s' % (threadName, time.ctime(time.time())))

    print(threadName, '线程结束了')


# 创建两个线程
try:
    threading._start_new_thread(print_time, ("Thread1", 2))
    threading._start_new_thread(print_time, ("Thread2", 4))
except:
    print('Error: unable to start thread')

while 1:
    pass

