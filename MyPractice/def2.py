# -*- coding utf-8 -*-

import math

# 默认参数
# =================================================================================
def enroll(name, gender, age, city='xi\'an', job='IT engineer'):
    print(name, gender, age, city, job)

enroll('flack', 'IT行业', 30)

enroll('flack', '餐饮行业', 30, 'beijing', '高级厨师')



def calc(numbers):
    sum = 0
    for x in numbers:
        sum += math.pow(x, 2)

    return sum

res = calc([1,2,3])
print(res)

res = calc((1,2,3))
print(res)

res = calc({1,2,3})
print(res)
# =================================================================================


# 可变参数 自动将*numbers组装为一个tuple，可以传入0个或任意个参数
# =================================================================================
def calcs(*numbers):
    sum = 0
    for x in numbers:
        sum += math.pow(x, 2)

    return sum


res = calcs(1,2,3)
print(res)

res = calcs()
print(res)


nums = [1,2,3]
# res = calcs(nums[0],nums[1],nums[2])
# *nums表示把nums这个list的所有元素作为可变参数传进去
res = calcs(*nums)
print(res)

nums=(1,2,3)
res = calcs(*nums)
print(res)


# 不支持
# nums={'k1':1, 'k2':2, 'k3':3}
# res = calcs(*nums)
# print(res)


def person(name, age, *kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Michael', 30, (1,2,3))
# =================================================================================


# 关键字参数 自动将*numbers组装为一个dict，可以传入0个或任意个关键字参数
# =================================================================================
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Michael', 30, kw = (1,2,3))
person('Michael', 30, kw = '高精尖科技')
person('Michael', 30,  city = '成都')
person('Michael', 30,  city = '西安')
person('Michael', 30,  city = '北京')
person('Michael', 30,  city = '上海')
person('Michael', 30,  city = '深圳')
person('Michael', 30,  city = '大连')
person('Michael', 30,  province = '甘肃')
person('Michael', 30,  province = '陕西')

person('Michael', 30,  province = '陕西',city='西安')
person('Michael', 30,  province = '甘肃',city='天水')

person('Michael', 30,  province = '甘肃',city='天水',address='西口镇')
person('Michael', 30,  province = '北京',city='北京',address='海淀区')


extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 40, city=extra['city'], job=extra['job'])
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person('Jack', 40, **extra)
# =================================================================================


# 命名关键字参数
# =================================================================================
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数只接收city和job作为关键字参数
def getPerson(name, age, *, city, job):
    print(name, age, city, job)

# getPerson('flack', 30) 这种调用发无效
# getPerson('flack', 30, city='西安')  这种调用发无效

getPerson('flack', 30, city='西安', job='IT')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def getPerson2(name, age, *args, city, job):
    print(name, age, args, city, job)


getPerson2('flack', 30, city='西安', job='it')
getPerson2('flack', 30, [1,2,3], city='西安', job='it')
getPerson2('flack', 30, (1,2,3), city='西安', job='it')
getPerson2('flack', 30, {1,2,3}, city='西安', job='it')


def getPerson3(name, age, *, city='西安', job):
    print(name, age, city, job)

getPerson3('flack', 30, job='it 222')
getPerson3('flack', 30, city='北京',job='it 222')
getPerson3('flack', 30, job='it 222', city='北京')

# =================================================================================


# 参数组合
# =================================================================================
# 必选参数，默认参数，可变参数，关键字参数，命名关键字参数
# (a)      (a='123')  (*a)      (**a)    (a, *, city)
# 参数定义的顺序必须是：必选参数>默认参数>可变参数>命名关键字参数和关键字参数

def f1(a,b,c):
    pass

def f2(a, b, c=0):
    pass

def f3(a,b,c=0, *args):
    pass

def f4(a,b,c=0, *args, **kw):
    pass

def f5(a,b,c=0, **kw):
    pass

def f6(a,b,c=0,*, d, e):
    pass

def f7(a,b,c=0,*,d, **kw):
    pass

def f8(*args, **kw):
    pass
# =================================================================================


# summary:
'''
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法
*args是可变参数，args接收的是一个tuple
**kw是关键字参数，kw接收的是一个dict
以及调用函数时如何传入可变参数和关键字参数的语法
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数
'''
