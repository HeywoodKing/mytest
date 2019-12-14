# -*- encoding: utf-8 -*-
"""
@File           : test3.py
@Time           : 2019/11/21 20:48
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import numpy as np
import pandas as pd


def main():
    ser1 = pd.Series([1, 2, 3, 4, 5, 6])
    ser2 = pd.Series([4, 5, 6, 7, 8, 9])
    # ser1和ser2交集
    ser3 = ser1.isin(ser2)
    # print(ser3)
    print("ser3=ser1和ser2交集:")
    print(ser1[ser3])

    # 并集
    ser_u = pd.Series(np.union1d(ser1, ser2))
    print("ser_u=ser1和ser2并集:")
    print(ser_u)

    # 交集
    ser_i = pd.Series(np.intersect1d(ser1, ser2))
    print("ser_i=ser1和ser2交集:")
    print(ser_i)

    # ser_i在ser_u的补集就是ser1和ser2不相同的项
    ser_c = ser_u[~ser_u.isin(ser_i)]
    print("ser_c=ser_i在ser_u的补集:")
    print(ser_c)


if __name__ == '__main__':
    main()
