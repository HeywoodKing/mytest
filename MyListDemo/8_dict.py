# -*- coding: utf-8 -*-


from collections import defaultdict


# student = defaultdict(str)
# print(student['name'])

student1 = {}
a = student1.setdefault('tb', 0)
b = student1.setdefault('name', [])
print(student1['name'])
print(a, b)


result = {}
data = [("p", 1), ("p", 2), ("p", 3),
        ("h", 1), ("h", 2), ("h", 3)]
for (key, value) in data:
    # print(key, value)
    result.setdefault(key, []).append(value)

print(result)


result = defaultdict(list)
for (key, value) in data:
    result[key].append(value)

print(result)

result.clear()
# del result
print(result)



