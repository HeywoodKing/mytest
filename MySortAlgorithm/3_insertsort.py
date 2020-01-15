# -*- coding: utf-8 -*-


import time


"""
插入排序 （默认从小到大排序）
对于一个无序序列，我们认为序列的左侧是有序的，右侧是无序的，第一个元素我们认为是有序的元素，从第二个元素
开始遍历，第二个元素和他的前一个元素比较，如果他比前一个元素小，则交换位置（插入），
然后第三个元素和他的前两个元素比较，如果小于则交换（插入），直到和他左侧的所有元素比较完，以此类推
"""


# 时间复杂度O(n平方)  稳定性：稳定
def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        min_index = i
        for j in range(i - 1, -1, -1):
            # print(alist)
            if alist[j] > alist[i]:  # 升序还是降序，这里控制
                min_index = j
        alist.insert(min_index, alist.pop(i))

    return alist


def insert_sort2(alist):
    n = len(alist)
    for i in range(1, n):
        j = i
        while j > 0:
            if alist[j] < alist[j - 1]:  # 升序还是降序，这里控制
                # alist.insert(min_index, alist.pop(i))
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
                j -= 1
            else:
                # j -= 1
                break

    return alist


if __name__ == "__main__":
    ls = [33, 100, 4, 56, 39, 78, 12, 0]
    start_time = time.time()
    res = insert_sort2(ls)
    end_time = time.time()
    print("耗时：%s" % (end_time - start_time))
    print(res)
