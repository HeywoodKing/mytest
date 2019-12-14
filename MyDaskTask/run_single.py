# -*- encoding: utf-8 -*-
"""
@File           : run_single.py
@Time           : 2019/11/16 15:04
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import time
from dask.distributed import Client
from multiprocessing import freeze_support

client = Client(asynchronous=True)  #


def square(x):
    return x**2


def neg(x):
    return -x


def run():
    ts = time.time()
    A = client.map(square, range(10000))
    B = client.map(neg, A)
    result = client.submit(sum, B)
    res = result.result()
    # res = client.gather(result)
    print(res)
    # print(res)

    res = client.gather(A)
    print(res)
    res = client.gather(B)
    print(res)
    print('cost of time: %s' % (time.time() - ts))


if __name__ == '__main__':
    # freeze_support()
    run()
