# -*- coding: utf-8 -*-


from array import *


arr = array('i', [10, 20, 40, 80, 160])

# for x in arr:
#     print(x)

arr.insert(1, 60)
print(arr[0], arr[2])
arr.remove(40)
print(arr)

print(arr.index(20), arr[arr.index(20)])

arr[0] = 100
print(arr)
