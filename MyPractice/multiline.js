print('''
line1
line2
line3
''')

# -*- coding: utf-8 -*-
print(ord('a'))
print(ord('b'))
print(ord('c'))
print(ord('d'))
print(ord('e'))
print(ord('f'))

print(ord('A'))
print(ord('B'))
print(ord('C'))


print(chr(65))

print(chr(20013),chr(25991))


print('ABC'.encode('ascii'))

print('中文'.encode('utf-8'))
# print('中文'.encode('ascii', errors='ignore'))
print(len('中文'))

msg = 'Hi, %s, you have $%d. rest $%.2f, age is %x, date is %02d' % ('Michael', 10000, 235.526, 0x13, 1)
print(msg)
