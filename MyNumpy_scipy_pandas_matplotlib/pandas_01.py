# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd


# Series 一维数组
# DataFrame 二维数组
# Panel 三维数组

s = pd.Series([1, np.nan, 6, 8])
s.index = ['one', 'two', 'three', 'four']
print(s)
print(s.index)

