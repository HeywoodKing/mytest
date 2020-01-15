# -*- coding: utf-8 -*-

import _thread
import time


def do_work(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(do_work, ('Thread-1', 10))
    _thread.start_new_thread(do_work, ('Thread-2', 5))
except:
    print("Error: unable to start thread")

