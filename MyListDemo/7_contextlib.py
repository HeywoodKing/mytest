# -*- coding: utf-8 -*-


from contextlib import contextmanager


class A(object):
    def __init__(self):
        pass

    def __enter__(self):
        print('__enter__() called')
        return self

    def print_hello(self):
        print('hello world')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__() called')


with A() as a:  # 这里a是__enter__()的返回值
    a.print_hello()  # 返回self，调用self的print_hello()方法
    print('got instance')




@contextmanager
def B():
    print('start')
    a = A()
    yield a
    print('Over')


with B() as a:
    a.print_hello()




@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("p1"):
    print("hello")
    print("world")

