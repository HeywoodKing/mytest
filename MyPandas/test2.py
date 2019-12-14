# -*- encoding: utf-8 -*-
"""
@File           : test2.py
@Time           : 2019/11/21 20:47
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import numpy as np
import pandas as pd


def series_test():
    my_list = list('abcdefghijklmnopqrstuvwxyz')
    my_arr = np.arange(26)
    my_dict = dict(zip(my_list, my_arr))

    ser1 = pd.Series(my_list)
    ser2 = pd.Series(my_arr)
    ser3 = pd.Series(my_dict)
    # print(my_dict)
    print(ser3.head())

    ser = pd.Series(my_dict)
    # 将series转化为DataFrame
    df = ser.to_frame()
    # 索引列转换为dataframe的列
    df.reset_index(inplace=True)
    print(df.head())

    # axis=1表示列拼接，axis=0表示行拼接
    df = pd.concat([ser1, ser2], axis=1)
    print(df.head())

    # 设置列名
    df = pd.DataFrame({'col1': ser1, 'col2': ser2})
    print(df.head())

    ser1.name = 'daphne'
    print(ser1.head())


if __name__ == '__main__':
    series_test()
