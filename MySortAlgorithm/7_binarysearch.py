# -*- coding: utf-8 -*-


import time


# 最优时间复杂度O(1)  最坏时间复杂度O(log以2为底的n)  稳定性：不稳定
# 搜索 二分查找，折半查找
# 递归
def binary_search(alist, item):
    """
    二分查找
    :param alist:
    :return:
    """
    n = len(alist)
    mid = n // 2
    if n > 0:
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        elif item > alist[mid]:
            return binary_search(alist[mid + 1:], item)
    else:
        return False
    return alist


# 非递归
def binary_search2(alist, item):
    n = len(alist)
    if n > 0:
        first = 0
        last = n - 1

        while first <= last:
            mid = (first + last) // 2

            if alist[mid] == item:
                return True
            elif item > alist[mid]:
                first = mid + 1
                pass
            elif item < alist[mid]:
                last = mid - 1

    return False


if __name__ == "__main__":
    ls = [17, 33, 45, 67, 89, 99, 100]
    start_time = time.time()
    # res = binary_search(ls, 33)
    res = binary_search(ls, 35)
    end_time = time.time()
    print("耗时：%s" % (end_time - start_time))
    print(res)
