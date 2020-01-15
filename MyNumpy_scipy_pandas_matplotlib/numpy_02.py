# -*- coding: utf-8 -*-


import numpy as np
import copy


# 访问数组元素
a = np.array([[1, 2, 4, 5], [2, 4, 7, 3], [2, 5, 3, 9]])
print('第1行', a[0])
print('第1列', a[:, 0])
print('第2列', a[:, 1])
print('切片：第1行的1-3索引元素', a[0][1:3])
print('切片：第1列的1-3索引元素', a[:, 0][1:3])
print('切片：第3列的1-3索引元素', a[:, 2][1:3])
print('切片：第2行第1列', a[1, 0])
print('切片：第2行第3列', a[1, 2])
print('切片：第3行第4列', a[2, 3])
print('切片：', a[0][:-2])
print('切片：', a[2][::2])

b = a > 3  # 返回bool数组
print(b)

c = copy.copy(a[a > 3])  # 利用bool数组选取元素
print(a, c)

c[0] = 14
print(a, c)

