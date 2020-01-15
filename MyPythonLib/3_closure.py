# -*- coding: utf-8 -*-


# ================================
# 1.函数名可以作为返回值
# ================================
def outer():
    def inner():
        pass

    return inner


res = outer()
print(res)
# ================================


# ================================
# 2.函数可以作为一个参数
# ================================
def index():
    print('index function')


def outer(index):
    index()


outer(index)
# ================================
# 所以满足上面两个条件中的一个,都可以称为高级函数.


# 闭包函数
# 闭包函数必须满足两个条件:
# 1.函数内部定义的函数
# 2.包含对外部作用域而非全局作用域的引用
# ================================
# 非闭包函数
# ================================
def outer():
    def inner():
        print('inner func excuted')

    inner()  # 调用执行inner()函数
    print('outer func excuted')


# 调用执行outer函数
outer()
# ================================


# ================================
# 非闭包函数
# ================================
x = 1


def outer():
    def inner():
        print('inner func excuted')
        print('x=%s' % x)  # 引用了一个非inner函数内部的变量

    inner()  # 执行inner函数
    print('outer func excuted')


outer()
# ================================


# ================================
# 闭包函数
# ================================
def outer():
    x = 10

    def inner():
        print('inner func excuted')
        print('x=%s' % x)  # 引用了一个非inner函数内部的变量

    inner()  # 执行inner函数
    print('outer func excuted')


outer()
# ================================


# ================================
# 闭包函数
# ================================
def outer():
    x = 100
    y = 200

    def inner():
        print('inner func excuted')
        print('x=%s, y=%s' % (x, y))  # 引用了一个非inner函数内部的变量

    print('outer func excuted')
    # 一个闭包函数有多少个外部引用变量
    print(inner.__closure__)
    return inner  # 返回内部函数名


res = outer()
res()
print(res)
# 闭包函数的特点：1.自带作用域 2.延迟计算
# ================================


# ================================
# 这个也是闭包函数
# ================================
def index(url):
    def get():
        # print('url=%s' % url)
        return url

    return get


a = index('www.baidu.com')
print(a, a())
# ================================
