# -*- encoding: utf-8 -*-
"""
@File           : test1.py
@Time           : 2019/11/20 10:49
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from sqlalchemy import create_engine
from setting import *


# 工作可大概分为
# 读取数据-数据清洗-分析建模-结果展示


def main():
    try:
        # df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [3, 4, 5, 6]], index=['a', 'b', 'c'], columns=['id1', 'id2', 'id3', 'id4'])
        # print(df)
        # print(df.count(1))
        # print(df.ndim)
        # print(df.mean(1))
        # print(df.std())

        # data = Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'e', 'f', 'g'])
        # data1 = Series([7, 8, 9], index=['e', 'f', 'g'])
        # data.index.name = 'ddd'
        # data.name = 'test'
        #
        # print(data)
        # print(data.index)
        # print(data.values)
        # # print(list(data.values))
        # print('a' in data)
        # # print(data.isnull())
        # # print(data.notnull())
        # print(data.count())
        # print(data + data1)
        #
        # # data_dict = {'a': 1, 'b': 2, 'c': 3}
        # # data = Series(data_dict)
        # # print(data)

        data = {'a': [1, 2, 3], 'b': ['we', 'you', 'they'], 'c': ['btc', 'eos', 'ae']}
        df = DataFrame(data)
        # df.name = 'aaa'
        # df.index.name = 'bbb'
        print(df)
        # print(df.shape, df.index)
        # print(df.values)
        print(df.iloc[1])
        # print(df.iloc[1, 2])
        print(df.iloc[1:, ])
        print(df.iloc[:, 1:])

        pass

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
