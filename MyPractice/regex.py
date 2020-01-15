# -*- coding: UTF-8 -*-

import re

print(re.match('www', 'www.aforge.cn').span())
print(re.match('cn', 'www.aforge.cn'))

line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print('group:', matchObj.group())
    print('group(1):', matchObj.group(1))
    print('group(2):', matchObj.group(2))
else:
    print('No match!')


print(re.search('www', 'www.aforge.cn').span())
print(re.search('cn', 'www.aforge.cn').span())


searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print('group:', searchObj.group())
    print('group(1):', searchObj.group(1))
    print('group(2):', searchObj.group(2))
else:
    print('Nothing found!')

phone = "2004-599-959 # 这是一个国外的电话号码"

num = re.sub(r'#.*$', "", phone)
print('电话号码：', num)

num = re.sub(r'\D', "", phone)
print('电话号码：', num)


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))



