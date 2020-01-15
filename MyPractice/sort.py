# -*- coding: utf-8 -*-

l = sorted([10,23,3,12,66,27,18])
print(l)

l = sorted([36, 5, -12, 9, -21], key=abs)
print(l)

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
l = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(l)

l = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower)
print(l)

# 反向排序
l = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse=True)
print(l)

# 请用sorted()对列表分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    # print(t)
    return t[0]

def by_score(t):
    return t[1]

# 按名字排序
res = sorted(L, key=by_name)
print(res)

# 按成绩排序
res = sorted(L, key=by_score)
print(res)

res = sorted(L, key=by_score, reverse=True)
print(res)



