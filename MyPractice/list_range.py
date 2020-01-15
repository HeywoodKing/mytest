# -*- coding utf-8 -*-

L = list(range(1, 11))
print(L)


L = []

for x in range(1,11):
    L.append(x*x)

print(L)


L = [x * x for x in range(1,11)]
print(L)

L = [x * x for x in range(1,11) if x % 2 == 0]
print(L)

L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)
