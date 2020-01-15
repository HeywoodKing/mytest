# -*- coding: utf-8 -*-

"""
选择排序的第一趟处理是从数据序列所有n个数据中选择一个最小的数据作为有序序列中的第1个元素
并将它定位在第一号存储位置，第二趟处理从数据序列的n-1个数据中选择一个第二小的元素作为有序序列中的第2个元素
并将它定位在第二号存储位置，依此类推，当第n-1趟处理从数据序列的剩下的2个元素中选择一个较小的元素
作为有序序列中的最后第2个元素并将它定位在倒数第二号存储位置，至此，整个的排序处理过程就已完成。
"""


def solution():
    ls = [34, 22, 1, 45, 67, 12]
    res = []

    while ls:
        min_index = ls.index(min(ls))
        min_val = ls.pop(min_index)
        print(min_index, min_val)
        res.append(min_val)

    print(res)
    return res


def solution2():
    ls = [34, 22, 1, 45, 67, 12]
    res = []

    while ls:
        max_index = ls.index(max(ls))
        max_val = ls.pop(max_index)
        print(max_index, max_val)
        res.insert(0, max_val)

    print(res)
    return res


solution()
solution2()
