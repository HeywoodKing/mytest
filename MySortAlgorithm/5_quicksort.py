# -*- coding: utf-8 -*-


import time


"""
快速排序 （默认从小到大排序） 两边夹击
对于一个无序序列，取出第一个元素作为标志元素，剩下的元素定义两个头，一个低头，一个高头两个指针，从低指针开始和
标志元素比较，如果小于标志元素，继续查找，如果大于标志元素，停止低指针继续，从高指针一端开始查找，如果大于标志元素，
继续查找，如果小于标志元素，则将该元素和低指针的大于标志元素的交换位置，然后继续从低指针一端继续查找，知道两个指针相遇
，此位置插入标志元素，第一次遍历结束，在重复上述动作，以此类推
"""


# if alist[high] < mid_value:
#     alist[low] = alist[high]
#     low += 1
# elif :
#     high -= 1
#
# if alist[low] < mid_value:
#     low += 1
# elif alist[low] > mid_value:
#     alist[high] = alist[low]
#     high -= 1


# 最优时间复杂度O(nlog以2为底的n)  最坏时间复杂度O(n平方)  空间复杂度增加了  稳定性：不稳定
def quick_sort(alist, first=0, last=0):
    # n = len(alist)
    if last <= first:
        return alist

    mid_value = alist[first]
    low = first
    high = last

    # if high == 0:
    #     high = n - 1

    while low < high:

        # 高指针方向开始移动（向左移动）
        while low < high and alist[high] >= mid_value:
            high -= 1

        alist[low] = alist[high]
        # low += 1

        # 低指针方向开始移动（向右移动）
        while low < high and alist[low] < mid_value:
            low += 1

        alist[high] = alist[low]
        # high -= 1

    alist[low] = mid_value

    # llist = quick_sort(alist[:low - 1])  # 左侧序列
    # rlist = quick_sort(alist[low + 1:])  # 右侧序列
    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, last)

    return alist


if __name__ == "__main__":
    ls = [33, 100, 4, 56, 39, 78, 12, 0, 20, 16]
    start_time = time.time()
    res = quick_sort(ls, 0, len(ls) - 1)
    end_time = time.time()
    print("耗时：%s" % (end_time - start_time))
    print(res)

