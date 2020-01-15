# -*- coding: utf-8 -*-


import time


"""
选择排序 （默认从小到大排序）
对于一个无序序列，默认第一个元素作为最小值，然后从剩余的序列中比较，计算出剩余序列中的最小值，
如果设定的最小值大于剩余序列中的最小元素，则交换位置，否则设置的最小值就是最小值，
直到序列所有元素都遍历到n-1结束
"""


# 时间复杂度为O(n平方)  稳定性：不稳定的
def select_sort(alist):
    for i in range(len(alist)):
        blist = alist[i:]
        # print(alist, blist)
        min_value = min(blist)
        min_index = blist.index(min_value) + i
        alist[i], alist[min_index] = alist[min_index], alist[i]
        # print(min_index, min_value)
    return alist


def select_sort2(alist):
    for i in range(len(alist)):   # n
        # print(alist)
        min_value = min(alist[i:])  # n
        min_index = alist.index(min_value)
        alist[i], alist[min_index] = alist[min_index], alist[i]
        # print(min_index, min_value)
    return alist


def select_sort3(alist):
    n = len(alist)
    for j in range(0, n - 1):
        # min_index = j
        for i in range(j + 1, n):
            if alist[j] > alist[i]:
                # min_index = i
                alist[j], alist[i] = alist[i], alist[j]

    return alist


def select_sort4(alist):
    n = len(alist)
    for j in range(0, n - 1):  # n
        min_index = j
        for i in range(j + 1, n):  # n
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]

    return alist


if __name__ == "__main__":
    ls = [1, 33, 99, 30, 4, 56, 39, 78, 12, 100]
    start_time = time.time()
    res = select_sort4(ls)
    end_time = time.time()
    print("耗时：%s" % (end_time - start_time))
    print(res)
