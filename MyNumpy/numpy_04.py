# -*- coding: utf-8 -*-


import numpy as np

# 创建矩阵
a = np.matrix([[1.0, 2.0], [3.0, 4.0]])
b = np.matrix(np.arange(1, 5))
c = np.matrix(np.arange(1, 3))
print(a)
print(b)
print('转置a.T=', a.T)
print('a的逆a.I=', a.I)
print('矩阵乘法a*a=', a*a)
print('b的逆b.I=', b.I)
print(c, 'c的逆c.I=', c.I)

"""
a = [
    [1, 2],
    [3, 4]
]
a = [
    [1, 2],
    [3, 4]
] 
a**a = [
    [1*1 + 2*3, 1*2 + 2*4],
    [3*1 + 4*3, 3*2 + 4*4]
]
结果：
[
    [7, 10],
    [15, 22]
]

"""


# 矩阵乘法
"""
A = [
    [a1, a2, a3],
    [a4, a5, a6]
]
B = [
    [b1, b2],
    [b3, b4],
    [b5, b6]
]

C = AB

C = [
    [a1*b1 + a2*b3 + a3*b5, a1*b2 + a2*b4 + a3*b6],
    [a4*b1 + a5*b3 + a6*b5, a4*b2 + a5*b4 + a6*b6]
]
"""



