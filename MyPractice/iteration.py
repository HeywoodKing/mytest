# -*- coding utf-8 -*-

from collections import Iterable

#
# D= {"name": "flack", "age": 23, "city": "beijing", "job": "IT"}
#
# # 迭代的key
# for x in D:
#     print("%s = %s" % (x, D[x]))
#
# for x in D.values():
#     print("%s" % x)
#
# for x,y in D.items():
#     print("%s = %s" % (x, y))
#
#
#
# print(isinstance('abc', Iterable))
#
# print(isinstance([1,2,3], Iterable))
#
# print(isinstance(132, Iterable))
#
# print(isinstance((1,2,3), Iterable))
#
# print(isinstance({'a':1,'b':2,'c':3}, Iterable))
#
# # python 实现下标索引循环
# L = ['A','B','C','D']
# for i,value in enumerate(L):
#     print(i,value)
#
# T = ('A','B','C','D')
# for i,value in enumerate(T):
#     print(i,value)
#
# D = {'A': 80,'B':90,'C':100,'D':55}
# for i,value in enumerate(D):
#     print(i,value)
#
#
# temp = [(1,1),(2,4),(3,9)]
# for x,y in temp:
#     print(x,y)


L = [32,58,12,56,74,23,96]

def findMinAndMax(L):
    min,max = L[0],L[0]
    for x in L:
        if x < min:
            min = x
        else:
            max = x
    T = (min, max)

    return T

res = findMinAndMax(L)
print(res)


