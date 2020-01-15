# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt

# 散点图
x = [1, 2, 4, 5, 6, 7, 8, 9]
y = [5, 2, 6, 4, 7, 6, 8, 5]

plt.scatter(x, y, label='skitscat', color='b', s=25)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

