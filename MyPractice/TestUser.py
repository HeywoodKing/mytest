# Filename:TestUser.py
# coding=utf8
#-*- coding: UTF-8 -*-

print("您好！！！")

#import TestLib
#print(TestLib.lib_func(120))

#import TestLib as test
#print(test.lib_func(120))

#from TestLib import lib_func
#print(lib_func(150))

from TestLib import *
print(lib_func(110))

import inspect
print(inspect.getargspec(lib_func))
print(inspect.getargspec(lib_func_another))

a = [1,2,3]
print(hasattr(a,'append'))
b = (1,2,3)
print(hasattr(b,'append'))

print a.__class__
print a.__class__.__name__

print b.__class__
print b.__class__.__name__

print(list.__base__)


print(0b1110)
print(0o10)
print(0x2A)
print("============================")
print(int("1110",2))
print(int("10",8))
print(int("2A",16))
'''
就这样了，没事的啦
'''

"""
OK 啦，一样的啦
"""

def func():
    print("Hello world!")

func()


import sys
print(sys.path)
