# -*- coding: utf-8 -*-


import time


"""
冒泡排序 （默认从小到大排序）
对一个无序序列，循环比较相邻两个元素大小，第一遍循环比较得出一个最大值并且移动到序列的末端，即冒出一个最大，
第二遍循环冒出一个次大值，以此类推，知道所有序列都有序
"""


# 时间复杂度O(n平方)  稳定性：稳定的
def bubble_sort(alist):
    n = len(alist)
    for i in range(n - 1):  # n-1
        count = 0
        for j in range(i + 1, n):  #n-1
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
                count += 1

        if 0 == count:
            break

    return alist


def bubble_sort2(alist):
    n = len(alist)

    for j in range(0, n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

        if 0 == count:
            break

    return alist


def bubble_sort3(alist):
    n = len(alist)
    for j in range(n - 1, 0, -1):
        count = 0
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

        if 0 == count:
            break

    return alist


if __name__ == "__main__":
    ls = [33, 4, 56, 39, 78, 12]
    start_time = time.time()
    res = bubble_sort(ls)
    end_time = time.time()
    print("耗时：%s" % (end_time - start_time))
    print(res)
