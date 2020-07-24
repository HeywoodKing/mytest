# -*- coding: utf-8 -*-


# import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt

# 条形图
plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label='Example one')
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label='Example two', color='g')
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('graph')
plt.legend()

plt.savefig('matplotlib_03.png')
plt.show()



