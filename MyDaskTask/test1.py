# -*- encoding: utf-8 -*-
"""
@File           : test1.py
@Time           : 2019/11/18 20:06
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
from setting import *
import numpy as np

from operator import add
from dask.distributed import Client


def main():
    client = Client(address=DASK_SCHEDULER_URL)  # , asynchronous=True
    print(client)
    # client.restart()
    # client.close(10)
    # scheduler_info = client.scheduler_info()
    # from pprint import pprint
    # pprint(scheduler_info)
    x = client.submit(add, 1, 2)
    # print("status:{},key:{},done():{},result:{}".format(x.status, x.key, x.done(), x.result()))
    print("status:{},key:{},done():{}".format(x.status, x.key, x.done()))

    y = client.submit(np.random.random, 1000, pure=False)
    print(y.key)
    z = client.submit(np.random.random, 1000, pure=False)
    print(z.key)


if __name__ == '__main__':
    main()

