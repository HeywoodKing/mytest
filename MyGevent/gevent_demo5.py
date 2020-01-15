# -*- coding: utf-8 -*-

import gevent
from gevent.queue import Queue


def func1():
    for i in range(10):
        print('func1 put start')
        q.put(str(i) + 'func1')
        gevent.sleep(0)
        print('func1 put end')


def func2():
    for i in range(10):
        print('func2 start')
        res = q.get()
        print('func2 end', '----->', res)


q = Queue()
gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
])

