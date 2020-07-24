# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


# 折线图---函数式绘图例子 % matplotlib inline

x = np.linspace(0, 2*np.pi, 100, endpoint=True)
y = np.sin(x)

x2 = x
y2 = np.cos(x2)

plt.plot(x, y, 'b-d', label='中文$sin(x)$')
plt.plot(x2, y2, 'r-*', label='$cos(x)$')

plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)

plt.grid(color='b', linewidth='0.1', linestyle='--')

plt.title('wave graph', fontsize=18, color='r', weight='light')

plt.xlim(min(x) - 0.1, max(x) + 0.1)
plt.ylim(min(y) - 0.1, max(y) + 0.1)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 最优化标签位置
plt.legend(loc='best', fontsize=15)
plt.annotate('波峰', xy=[np.pi/2, 1], xycoords='data', xytext=(-0, -80),
             arrowprops=dict(color='red', shrink=0.1), textcoords='offset points',
             fontsize=15, color='black')
plt.savefig('matplotlib_01.png')
plt.show()

