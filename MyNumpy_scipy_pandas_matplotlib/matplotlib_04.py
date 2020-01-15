# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt

# 柱状图
population_ages = [
    22, 55, 62, 45, 21, 22, 34, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80,
    75, 64, 89, 23, 54, 44, 42, 28, 33, 69, 70, 36, 22, 56
]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph')

plt.savefig('matplotlib_04.png')
plt.show()
