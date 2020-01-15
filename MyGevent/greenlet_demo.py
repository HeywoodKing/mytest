# -*- coding: utf-8 -*-
from greenlet import greenlet
import time


def test1():
    while True:
        print('------真1------')
        gl2.switch()
        time.sleep(.5)


def test2():
    while True:
        print('------真2------')
        gl1.switch()
        time.sleep(.5)


gl1 = greenlet(test1)
gl2 = greenlet(test2)


# 切换到gl1中运行
gl1.switch()

# 最简单的协程手工切换方式
