# _*_ coding: utf-8 _*_

def calc_sum(*args):
    ax = 0
    for x in args:
        ax = ax + x
    return ax

# 这种称为闭包
def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    return sum


func = lazy_sum(1,2,3,4,5)
res = func()
print(res)


def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
f1,f2,f3 = count()



# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变
# 缺点是代码较长，可利用lambda函数缩短代码。
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    # fs.append(f(lambda i: (i for i in range(1,4))))
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count()

print(f1(),f2(),f3())


# def createCounter():
#     ans = [0]
#     def counter():
#         ans[0] += 1
#         return ans[0]
#     return counter

# 原来在python的函数中和全局同名的变量，如果你有修改变量的值就会变成局部变量，
# 在修改之前对该变量的引用自然就会出现没定义这样的错误了，
# 如果确定要引用全局变量，并且要对它修改，必须加上global关键字
def createCounter():
    global i
    i = 0
    def counter():
        global i
        i += 1
        return i
    return counter

# def createCounter():
#     a = 0
#     def counter():
#         nonlocal a
#         a += 1
#         return a
#     return counter

countA = createCounter()
countB = createCounter()
countC = createCounter()
# print(countA())
print(countA(), countB(), countB(),countC())