# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd


dates = pd.date_range('20180101', periods=3)
df = pd.DataFrame(np.random.randn(3, 4), index=dates, columns=list('ABCD'))
print(df)

