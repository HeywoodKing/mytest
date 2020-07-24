# -*- coding: utf-8 -*-


import numpy as np

# ufunc 函数具有向量化特性
x = np.linspace(0, np.pi, 5)
y = np.sin(x)  # 作用到x的每一个元素
print(x)
print(y)

# np.sin(x, x)  # 第二个参数表示将返回值赋给x本身

print(x)


def f(x):
    y = x if x >= 0 else 0
    return y

# frompyfunc函数可将普通Python函数转换成ufunc函数
# 三个参数依次分别为pyfun, nin, nout
uf = np.frompyfunc(f, 1, 1)

# 返回结果数据元素类型是object
z = uf([1, 2, -1])
print(z)
# 使用array对象的astype方法将其转换成np.float32
z.astype('f4')
print(z)

