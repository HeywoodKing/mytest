# -*- coding: utf-8 -*-

from greenlet import greenlet


def test1(x, y):
    z = gl2.switch(x + y)
    print('z =', z)


def test2(w):
    print(w)
    gl1.switch(42, '100')


gl1 = greenlet(test1)
gl2 = greenlet(test2)

gl1.switch('hello', ' world')