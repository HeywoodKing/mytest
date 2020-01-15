# -*- coding: utf-8 -*-

a = 1


def func(obj):
    b = 2
    print(a, obj, b)
    if a == 1:
        c = 3
        print(b)

    def inner(*args, **kwargs):
        d = 5
        print(c)

    inner()
    print(d)

func('cc')

