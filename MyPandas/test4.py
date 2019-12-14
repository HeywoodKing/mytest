# -*- encoding: utf-8 -*-
"""
@File           : test4.py
@Time           : 2019/11/22 20:10
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""

import numpy as np
import pandas as pd
from collections import namedtuple


def miter(df, cols=None):
    """
    迭代器(相当于pd.DataFrame.itertuples，但是效率更高)
    :param df: pandas 的 DataFrame
    :param cols:
    :return:
    eg:
    list(miter(df))
    [MyTuple(c1=10, c2=100), MyTuple(c1=11, c2=110), MyTuple(c1=12, c2=120)]

    list(df.itertuples(index=False))
    [Pandas(c1=10, c2=100), Pandas(c1=11, c2=110), Pandas(c1=12, c2=120)]
    """
    if cols is None:
        v = df.values.tolist()
        cols = df.columns.values.tolist()
    else:
        j = [df.columns.get_loc(c) for c in cols]
        v = df.values[:, j].tolist()

    print(cols)
    # n = namedtuple('MyTuple', cols)
    n = namedtuple('t', cols)

    for line in iter(v):
        yield n(*line)


def main():
    # df = pd.DataFrame(
    #     index=[10, 30, 100, 300, 1000, 3000, 10000, 30000],
    #     columns='iterfullA iterfullB itersubA itersubB'.split(),
    #     dtype=float
    # )

    df = pd.DataFrame([[123, 456, 789], ['abc', 'def', 'ghi'], ['rst', 'uvw', 'xyz']])
    for item in list(miter(df)):
        print(item)


if __name__ == '__main__':
    main()
