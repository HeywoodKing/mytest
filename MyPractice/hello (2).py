# -*- coding: UTF-8 -*-

import string
import random
import math
import time
import calendar
import os

print("您好，Python")

str1 = 'Hello World'
print(str1[0])
print(str1[2:5])
print(str1[2:])
print(str1 * 2)
print(str1 + ' Test')


list = ['apple', 'john', 123, 2.23, 70.2]
tinylist = [123, 'john']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)


tuple = ('apple', 'tear', 'ching', 111, 22,2, 33.0)
tinytuple = (123, 'ching')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple * 2)
print(tuple + tinytuple)

# tuple[1] = 100  #非法
list[1] = 200  #合法

print(tuple[1])
print(list[1])

dict = {}
dict['one'] = "This is a one"
dict[2] = "This is a two"
dictionary = {'name':'apple','code': 1112, 'dept': 321, 'mark': 23.1}

print(dictionary['name'])
print(dict['one'])
print(dictionary['code'])
print(dictionary)
print(dictionary.keys())
print(dict.values())

print(int(2.6))
print(float(23))
print(ord('A'))
print(oct(12))
print(hex(10))
print(complex(123))
print(repr(10))
print(type(dict))
print(type(list))
print(type(tuple))
a = 10
print(isinstance(a, int))



a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a % b)
print(a / b)
print(a ** 2)
print(b // a)



x = 60  # 0011 1100
y = 13  # 0000 1101

print('----------')
print(x & y)  # 0000 1100
print(x | b)  # 0011 1101
print(x ^ b)  # 0011 0001
print(~x)   # 1100 0011
print(x << 1)  # 0110 1000
print(x >> 2)  # 0000 1111


print('-----------------')

a = 10
b = 20

print('==============')
if(a and b):
    print('true')
else:
    print('false')

if(a or b):
    print('true')
else:
    print('false')

if(not a):
    print('true')
else:
    print('false')
print('==============')
list = [1, 2, 3, 4, 5];

if(a in list):
    print('true')
else:
    print('false')

if(b not in list):
    print('true')
else:
    print('false')


print('---------------------')

if(a is b):
    print('true')
else:
    print('false')

if(a is not b):
    print('true')
else:
    print('false')

print('---------------------')

var = 100

if var == 100:
    print('变量var的值为100')

print('Good byte')


print('----------------')

count = 0
while count < 9:
    print('The count is:', count)
    count += 1

print('Good bye!')

print('------------------')

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)

print('--------------')

i = 1
while 1:
    print("i =", i)
    i += 1
    if i > 10:
        break


print('---------------')
i = 1
while i < 5:
    print(i, 'is less than 5')
    i += 1
else:
    print(i, 'is not less than 5')

print('for循环')
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:
    print('当前水果', fruit)


for index in range(len(fruits)):
    print('当前水果:', fruits[index])

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d 等于 %d * %d ' % (num, i, j))
            break
    else:
        print(num, '是一个数')









# 打印等腰直角三角形


# rows = int(raw_input('请输入列数：'))
rows = 3


# 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
i = j = k = 1

print('打印等腰直角三角形')
for i in range(0, rows):
    for k in range(0, rows - i):
        print(' * ')  # 注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print('\n')


i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j += 1
    if j > (i / j):
        print(i, '是素数')
    i += 1


print('-----------------------')
for letter in 'python':
    if letter == 'p':
        pass
        print('这是pass块')
    else:
        print('当前字母', letter)

print('Good bye')

num = complex(2, 3)

print(num * 2)

print('-----------------------')

print(int(123))
print(float(12))
print(complex(2, 5))
print(str(123))
print(repr('cccc'))
# print(eval())
# print(tuple('ching'))
# print(list('aaa'))
print(chr(90))
print(ord('k'))
print(hex(123))
print(oct(98))

print('---------------------')

print(abs(-99))
print(math.ceil(4.4))
# print(cmp(5, 2))
print(math.exp(5))
print(math.floor(4.4))
print(math.fabs(-10))
print(math.log(100, 10))
print(math.log10(2))
print(math.log10(100))
print(max(1, 20, 32, 7))
print(min(20, 10, 33))
print(math.modf(10.78))
print(pow(2, 2))
print(round(4.5, 2))
print(math.sqrt(4))

print(random.choice(range(10)))
print(random.randrange(10, 20, 2))
print(random.random() * 100)

# seed(x)
# shuffle(list)
print(random.uniform(2, 8))

print('---------------------')


'''
math.acos(x)
math.asin(x)
math.atan(x)
math.atan2(y, x)
math.cos(x)
math.hypot(x, y)
math.sin(x)
math.tan(x)
math.degrees(x)
math.radians(x)
'''

print(math.pi)
print(math.e)

print(r'\n\r')

print('My name is %s and weight is %d kg, %c %u %f' % ('ching', 68, 88, 100, 201.09))
print('%e %g %x' % (20, 33, 100))

# vvv = 10
# print('%p' % (vvv))

print(string.capwords('ljl'))

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print('list1 =', list1[1])
print('list2 =', list2[1:5])

list2[2] = 10

print(list2[2])
print(list2)
del list2[2]
list2.append(22)
print(list2)


ticks = time.time()

print('当前时间', ticks)

locatime = time.localtime(time.time())

print(time.asctime(locatime))

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

print(time.strftime('%a %b %d %H:%M:%S', time.localtime()))

a = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())

print(time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y')))


cal = calendar.month(2017, 4)
print('2017-04日历')
print(cal)

# print(time.altzone())

print(time.asctime())

print(time.clock())

print(time.ctime(10))

print('gmtime:', time.gmtime())

print(time.localtime())
# time.sleep(3)
print(time.mktime(time.localtime()))

# time.strftime()
# time.strptime()

print(time.timezone)
print(time.time())
print(time.tzname)


def printme(s):
    "打印任何传入的字符串"
    print(s)
    return

printme('你好')

def printinfo(name, age = 25):
    print(name, age)
    return

printinfo(age = 33, name='chin')


def printinfo2(name, *args):
    res = ''
    for var in args:
        res = res + str(var)

    print(name, res)
    return

printinfo2('john', 80, 'fs009', -23)

sum = lambda arg1, arg2: arg1 + arg2

print('sum =', sum(10, 20))

def sum(arg1, arg2):
    total = arg1 + arg2
    print('函数内指：', total)
    return total

total = sum(20, 20)
print('函数外值：', total)

Money = 9999
def addMoney():
    global Money
    Money = Money + 1
    print(Money)

addMoney()

content = dir(math)

print(content)
print(__name__)
print(__file__)
print(globals())
print(locals())


# res = raw_input('请输入')



print(os.getcwd())

try:
    file = open("test.txt", "a+")
    file.write('这是一个测试文件,这些内容是程序自动写入的\r\n')
except IOError:
    print('Error:', '没有找到文件或读取文件失败')
else:
    print('文件内容写入成功')
    file.close()


try:
    file = open("test.txt", "r")
    res = file.read()
    print(res)
finally:
    print('Error', '没有找到文件或读取文件失败')
    file.close()



def timeoutfunc(level):
    if level < 5:
        raise Exception('Invalid level!', level)
    else:
        print(level)

try:
    timeoutfunc(30)
except 'Invalid level':
    print(1)
else:
    print(2)


class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Exception('Bad hostname')
except NetworkError, e:
    print(e.args)




