# -*- coding: utf-8 -*-


def extendList(val, list=[]):
    list.append(val)
    return list


def extendList2(val):
    list = []
    list.append(val)
    return list


list1 = extendList(10)
print(list1)

list2 = extendList(123, [])
print(list2)

list3 = extendList('a')
print(list3)

list4 = extendList2(10)
print(list4)

list5 = extendList2(123)
print(list5)

list6 = extendList2('b')
print(list6)




