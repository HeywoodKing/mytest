# -*- coding: utf-8 -*-


import time


# 最优时间复杂度O(nlog以2为底n) 最坏时间复杂度O(nlog以2为底n)  稳定性：稳定
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist

    mid = n // 2
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0
    result = []

    print(left_list, right_list)
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        # print(left_pointer, right_pointer)
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1

    result.extend(left_list[left_pointer:])
    result.extend(right_list[right_pointer:])

    return result


def merge_sort2(alist):
    n = len(alist)
    if n <= 1:
        return alist

    mid = n // 2
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0
    result = []

    # print(left_list, right_list)
    while left_list and right_list:
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list.pop(left_pointer))
            # left_pointer += 1
        else:
            result.append(right_list.pop(right_pointer))
            # right_pointer += 1

    result.extend(left_list)
    result.extend(right_list)

    return result


if __name__ == "__main__":
    ls = [33, 100, 4, 56, 39, 78, 12, 0]
    start_time = time.time()
    res = merge_sort2(ls)
    end_time = time.time()
    print("耗时：%s" % (end_time - start_time))
    print(res)

