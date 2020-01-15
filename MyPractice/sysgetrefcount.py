# Filename:sysgetrefcount.py

from sys import getrefcount

a = [1,2,3]
print(getrefcount(a))


b = a
print(getrefcount(b))


class from_obj(object):
    def __init__(self,to_obj):
        self.to_obj = to_obj

a = from_obj(b)
print(id(a.to_obj))
print(id(b))

b = [a, a]
print(getrefcount(a))
