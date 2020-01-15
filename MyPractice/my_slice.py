# -*- coding: utf-8 -*-

my_list = [1, 'abc', 'gg', 'mm', 10]
#          0    1     2     3     4
#         -5   -4    -3    -2    -1


print('my_list[0]: %s' % my_list[0])
print('my_list[4]: %s' % my_list[4])
print('my_list[1:2]: %s' % my_list[1:2])
print('my_list[0:]: %s' % my_list[0:])
print('my_list: %s' % my_list)
print('my_list[0::2]: %s' % my_list[0::2])
print('my_list[0::3]: %s' % my_list[0::3])
print('my_list[0::-2]: %s' % my_list[0::-2])
print('my_list[4::-1]: %s' % my_list[4::-1])
print('my_list[len(my_list) - 1::-1]: %s' % my_list[len(my_list) - 1::-1])
print('my_list[-2:]: %s' % my_list[-2:])
print('my_list[-3:]: %s' % my_list[-3:])
print('my_list[-3:-1]: %s' % my_list[-3:-1])
print('my_list[-3::-1]: %s' % my_list[-3::-1])
print('my_list[-3::-2]: %s' % my_list[-3::-2])
print('my_list[-3::2]: %s' % my_list[-3::2])


a = 3
if a > 1:
    print(1)
elif a > 2:
    print(2)
elif a > 3:
    print(3)
else:
    print(a)

