# -*- coding: utf-8 -*-


import collections


double_ended = collections.deque(['22', 10, 'ddd'])
print(double_ended)

double_ended.append('the')
print(double_ended)

double_ended.appendleft('ok')
print(double_ended)

a = double_ended.pop()
print(double_ended, a)

b = double_ended.popleft()
print(double_ended, b)

double_ended.reverse()
print(double_ended)

