# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

# 折线图
# 设置图片大小和像素
myfig = plt.figure(2, figsize=(14, 10), dpi=70)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 使用图像坐标添加子图对象位置
ax1 = myfig.add_axes([0.05, 0.2, 0.5, 0.5])
# [x坐标起点，y坐标起点，x图宽，y图宽]
ax2 = myfig.add_axes([0.5, 0.4, 0.5, 0.5])

x = np.linspace(0, 2*np.pi, 100, endpoint=True)
y = np.sin(x)

ax1.plot(x, np.sin(x), label='$sin(x)$')
ax1.set_title('正弦曲线', color='red', fontsize=18)
ax1.legend(loc='best', fontsize=16)

ax2.plot(x, np.cos(x), label='$cos(x)$')
ax2.set_title('余弦曲线', color='red', fontsize=18)
ax2.legend(loc='best', fontsize=16)

myfig.set_facecolor([0, 1, 0, 0.5])

myfig.savefig('matplotlib_02.png')
myfig.show()
