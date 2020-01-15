# -*- coding: utf-8 -*-


import time


# 堆排序
"""
"""


def heap_sort(alist):
    return alist


if __name__ == "__main__":
    ls = [33, 100, 4, 56, 39, 78, 12, 0]
    start_time = time.time()
    res = heap_sort(ls)
    end_time = time.time()
    print("耗时：%s" % (end_time - start_time))
    print(res)


