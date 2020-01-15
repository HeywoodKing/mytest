# -*- coding: utf-8 -*-

"""
直接插入排序法的排序原则是：将一组无序的数字排列成一排，左端第一个数字为已经完成排序的数字，
其他数字为未排序的数字。然后从左到右依次将未排序的数字插入到已排序的数字中。
"""


def solution():
    ls = [2, 34, 5, 33, 67, 90, 21, 3]
    res = []
    res.append(ls.pop(0))

    for i in range(len(ls) - 1):
        for j in range(i, len(ls)):
            if ls[i] > ls[j]:
                v = ls.pop(j)
                ls.insert(i, v)
                print(ls)

    res.extend(ls)
    print(res)


def solution2():
    ls = [2, 34, 5, 33, 67, 90, 21, 3]
    res = []
    first = ls.pop(0)
    res.append(first)

    for i in ls:
        # max_index = res.index(max(res))
        # max_v = max(res)
        # min_index = res.index(min(res))
        # min_v = min(res)
        #
        # if i > max_v:
        #     res.insert(max_index + 1, i)
        # elif i <= min_v:
        #     res.insert(min_index, i)
        # else:
        #     res.insert(min_index + 1, i)



    print(res)


# solution()
solution2()
