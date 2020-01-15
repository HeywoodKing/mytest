# -*- coding: utf-8 -*-


import time


"""
希尔排序是插入排序的改进算法 （默认从小到大排序）
本质还是插入排序算法，只是做了改进，对于一个无序序列，首先根据序列长度计算出缝隙，按照缝隙产生的序列，
从该序列的第二个元素开始比较间隔缝隙元素的大小，小于则交换位置，依次类推比较完产生的新序列的前面所有元素，
缝隙+1，下一个新序列，然后比较从第二个元素之前的所有元素，小于则交换位置，以此类推，接着缝隙减半，直到
缝隙值为1，即最后依次循环
"""


# 最优：根据序列长度不同而不同  时间复杂度O(nlogn~n平方)  稳定性：不稳定
def shell_sort(alist):
    n = len(alist)
    gap = n // 2

    while gap >= 1:  # gap > 0:
        # 插入算法
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break

        # 缩短gap步长
        gap //= 2

    return alist


if __name__ == "__main__":
    ls = [33, 100, 4, 56, 39, 78, 12, 0]
    start_time = time.time()
    res = shell_sort(ls)
    end_time = time.time()
    print("耗时：%s" % (end_time - start_time))
    print(res)


