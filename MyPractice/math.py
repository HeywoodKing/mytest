# -*- coding utf-8 -*-

print(abs(-10))

def add(x, y, f):
    return f(x) + f(y)

print(add(5, -6, abs))

# map
# 比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现
def f(x):
    return x*x

r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r))

r1 = list(map(str, [1,2,3,4,5,6,7,8,9]))
print(r1)


def add(x, y):
    return x + y

from functools import reduce
r2 = reduce(add, [1,3,5,7,9])
print(r2)

def fn(x, y):
    return x * 10 + y

r3 = reduce(fn, [1,3,5,7,9])
print(r3)

def upper_txt(x):
    return x.upper()

def first_upper_txt(x):
    return x.capitalize()

def title_txt(x):
    return x.title()

def lower_txt(x):
    return x.lower()

def swapcase_txt(x):
    return x.swapcase()

L1 = ['adam', 'LISA', 'barT', 'abDerce word']
r4 = list(map(upper_txt, L1))
print(r4)

r5 = list(map(first_upper_txt, L1))
print(r5)

r6 = list(map(title_txt, L1))
print(r6)

r7 = list(map(lower_txt, L1))
print(r7)

r8 = list(map(swapcase_txt, L1))
print(r8)
