# -*- coding utf-8 -*-

L = ['adam', 'LISA', 'barT']

def normalize(name):
    return name.capitalize()

res = list(map(normalize, L))
print(res)


L1 = [1,2,3,4,5]

from functools import reduce
def multi(x, y):
    return x * y

def prod(l):
    return reduce(multi,l)

print(prod(L1))
