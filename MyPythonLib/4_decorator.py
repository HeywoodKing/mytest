# -*- coding: utf-8 -*-


import time, random


# ================================
# 1.无参装饰器
# ================================
def outer(func):
    def inner():
        print('inner start')
        start_time = time.time()
        func()  # fun = index  即func保存了外部index函数的地址
        end_time = time.time()
        print('执行时间：%s' % (end_time - start_time))
        print('inner end')

    return inner  # 返回inner的地址

# ================================


@outer
def index():
    time.sleep(random.randint(1, 5))
    print('welcome to index page')


# deco_index = outer(index)
# deco_index()
# 等于
# @outer

# index()


# ================================
# 2.有参装饰器
# ================================
def outer(func):  # 将index的地址传递给func
    def inner(*args, **kwargs):
        print('inner start')
        start_time = time.time()
        func(*args, **kwargs)  # fun = info  即func保存了外部info函数的地址
        end_time = time.time()
        print('执行时间：%s' % (end_time - start_time))
        print('inner end')

    return inner  # 返回inner的地址
# ================================


@outer
def info():
    time.sleep(random.randint(1, 5))
    print('welcome to info page')


# info()


# ================================
# 3.有参装饰器（变装后）
# ================================
def timmer(func):
    def wrapper(*args, **kwargs):
        print('timmer start')
        start_time = time.time()
        res = func(*args, **kwargs)  # res来接收home函数的返回值
        end_time = time.time()
        print('执行时间：%s' % (end_time - start_time))
        print('timmer end')
        return res

    return wrapper


def auth(func):
    def wrapper(*args, **kwargs):
        print('auth start')
        username = input('username:')
        password = input('password:')
        if username == 'admin' and password == '123456':
            func(*args, **kwargs)
            print('login successful')
        else:
            print('login fail')
        print('auth end')

    return wrapper

# ================================


# 多个装饰器装饰一个函数的时候是从下往上执行的
@auth
@timmer
def home(name):
    time.sleep(random.randint(1, 3))
    print('welcome to %s home page' % name)
    return 'GET 200 OK'


# 在被装饰的函数之前写上@timmer,它的效果就和home = outer(home)是一样的
# r = home('李四')
# print(r)


# 类装饰器
"""
装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法
"""


# class Foo(object):
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self, *args, **kwargs):
#         print('class decorator running')
#         res = self._func()
#         print('class decorator ending')
#         return res
#
#
# # 类装饰器装饰在函数上
# @Foo  # bar = Foo(bar)
# def bar():
#     print('bar ok')
#
#
# bar()


# 类装饰器装饰第二种写法
class Foo(object):
    # def __init__(self):
    #     pass

    def __call__(self, func):
        def _call(*args, **kwargs):
            print('class decorator running')
            res = func(*args, **kwargs)
            print('class decorator ending')
            return res

        return _call


class Bar(object):
    @Foo()
    def bar(self, name, ids):
        print('%s hello world %s' % (name, ids))


Bar().bar('张三', '12345')


# 在Python中有三个内置的装饰器，都是跟class相关的：staticmethod、classmethod 和property。
"""
staticmethod 是类静态方法，其跟成员方法的区别是没有 self 参数，并且可以在类不进行实例化的情况下调用
classmethod 与成员方法的区别在于所接收的第一个参数不是 self （类实例的指针），而是cls（当前类的具体类型）
property 是属性的意思，表示可以通过通过类实例直接访问的信息
"""


class Foou(object):
    def __init__(self, var):
        super(Foou, self).__init__()
        self._var = var

    # 可读
    @property
    def var(self):
        return self._var

    # 可写
    @var.setter
    def var(self, var):
        self._var = var


foou = Foou('var111')
print(foou.var)
foou.var = 'ddddd'
print(foou.var)

