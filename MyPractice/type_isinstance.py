# -*- coding: utf-8 -*-

print(type('abc'))


a = [2,3,4]
if isinstance(a, list):
    print('true')
else:
    print('false')

if isinstance(a, (list, tuple)):
    print('true')

# print(dir('abc'))
print(dir(str))


print(dir(int))

a = 120
b = a.__sub__(10)
c = a.__rsub__(10)
print(a, b, c)
