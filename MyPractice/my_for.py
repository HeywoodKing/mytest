# -*- coding: utf-8 -*-


fruit = ['apple', 'pear', 'pitch', 'bananer', 'soup']
for item in fruit:
    print(item)


for item in range(0, 6):
    print(item, '\b')

print('%G' % 10)

a, b = 10, 3
print('a/b = %s' % (a / b))
print('a*b = %s' % (a * b))
print('a**b = %s' % (a ** b))
print('a//b = %s' % (a // b))
print('a%b = ', a % b)

la = ['aaa']
lb = ['bbb']
la.extend(lb)
lc = [123, 456]
ld = [str(i) for i in lc]
# print(la)
la.extend(ld)
# print(la + lb)


my_str = '-->'.join(la)
print(my_str)






















