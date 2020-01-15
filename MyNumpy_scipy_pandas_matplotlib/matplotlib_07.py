# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


# 绘制子图
def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)

plt.figure(10, figsize=[8, 6])

# 分成2x2 占用第一个，即第一行第一列的子图
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'r--')

# 分成2x2 占用第二个，即第一行第二列的子图
plt.subplot(222)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')

# 分成2x1 占用第二个，即第二行的子图
plt.subplot(212)
plt.plot([1, 2, 3, 4], [1, 4, 9, 15])

plt.suptitle('Interesting Graph', fontsize=15)
plt.show()
