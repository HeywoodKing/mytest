# -*- encoding: utf-8 -*-
"""
@File           : run.py
@Time           : 2019/11/16 15:17
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""

import time
from dask.distributed import Client, progress


def square(x):
    return x ** 2


def neg(x):
    return -x


def pdf_to_text(file_path):
    print('{} 打开pdf'.format(file_path))
    print('{} 读取pdf内容'.format(file_path))

    print('{} 关闭pdf'.format(file_path))
    print('{} 解析pdf内容'.format(file_path))
    # time.sleep(1)
    print('{} 过滤pdf内容'.format(file_path))
    print('{} 过滤后的内容写入到txt'.format(file_path))

    print('{} 关闭txt文件'.format(file_path))
    return file_path ** 2


def main():
    client = Client('192.168.1.190:8786')  # , asynchronous=True
    print(client)
    ts = time.time()
    # job_a = client.map(pdf_to_text, range(10000))
    # A = client.map(square, range(10000))
    # B = client.map(neg, A)
    C = client.map(pdf_to_text, range(100000))
    # result = client.submit(sum, C)

    # res = result.result()
    # res = client.gather(result)
    # print(res)

    res = client.gather(C)
    print(res)
    # res = client.gather(B)
    # print(res)
    print('cost time :%s' % (time.time() - ts))


if __name__ == '__main__':
    main()

