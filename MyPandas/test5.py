# -*- encoding: utf-8 -*-
"""
@File           : test5.py
@Time           : 2019/11/29 19:24
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import numpy as np
import pandas as pd


def main():
    df = pd.read_excel('abc.xlsx')
    print(df.head())
    # print(df[['Part_Number', 'Manufacturer_Part_Number']])
    # print(df.iloc[1, 1])
    # print(df.loc[0])
    # print('*' * 100)
    # print(df.iloc[1])
    print('*' * 100)
    print(df.loc[:, 'Part_Number'])
    print(df.dtypes)
    # df['Part_Number'] = df['Part_Number'].astype['string']
    df.loc[:, df.columns[1:-1]] = df.loc[:, df.columns[1:-1]].apply(pd.to_numeric, errors='ignore')
    print(df.dtypes)


if __name__ == '__main__':
    main()
