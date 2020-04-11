# -*- coding: utf-8 -*-


import numpy as np

# 常见运算符
a = np.array([[1, 2, 4], [2, 4, 5], [3, 5, 2]])
b = np.array([1, 2, 3])
c = np.array([2, 3, 4])
print(a + b)
print(b + c)
print(b - c)
print(b * c)
print(b / c)
print(b // c)
print(b ** 2)
print(b % 2)

# 查看维度
print(np.ndim(a))
# 查看大小
print(np.shape(a))
# 最大，最小值
print(a.max(), a.min())
# 点积
print(np.dot(b, c))
# 数组矩阵乘法
print(np.dot(a, b))
