# -*- coding: utf-8 -*-


from numpy import *

a = array([
    ['Mon', 18, 20, 22, 17],
    ['Tue', 11, 18, 21, 18],
    ['Wed', 15, 21, 20, 19],
    ['Thu', 11, 20, 22, 21],
    ['Fri', 18, 17, 23, 22],
    ['Sat', 12, 22, 20, 18],
    ['Sun', 13, 15, 19, 16]
])
# 使用数组numpy中可用的重塑方法以7*5矩阵形式
m = reshape(a, (7, 5))
print(m)
print(m[4][3])

