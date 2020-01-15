# -*- coding: utf-8 -*-

from gevent import monkey
import gevent
import random
import time


# 有耗时操作时需要
# 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块
monkey.patch_all()


def do_work(work_name):
    for i in range(10):
        print(work_name, i)
        time.sleep(random.random())


gevent.joinall([
    gevent.spawn(do_work, '爬取数据任务'),
    gevent.spawn(do_work, '清洗数据任务'),
    gevent.spawn(do_work, '再虑数据任务'),
    gevent.spawn(do_work, '装载数据任务'),
])

