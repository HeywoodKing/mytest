# Filename:sayHello.py
# 函数
def sayHello():
    print("Hello world!")

#调用函数
sayHello()

# 带形参函数
def printMax(a, b):
    if a > b:
        print(a, "is maximum.")
    else:
        print(b, "is maximum.")

printMax(10, 30)

# 局部变量
def func(x):
    print("x is ", x)
    x = 2
    print("Changed local x to ", x)
x = 50
func(x)
print("x is still ", x)


# 默认参数值
def say(message, times = 1):
    print(message * times)

say("ha")

say("ha", 2)


# 关键参数
def func(a, b = 5, c = 10):
    print("a is", a, "and b is", b, " and c is", c)

func(3, 7)
func(25,c = 24)
func(c = 50, a = 100)


# return语句
def maximum(x, y):
    if x > y:
        return x
    else:
        return y

print(maximum(2, 3))


# 文档字符串DocStrings
# Python有一个奇妙的特性，就是文档字符串（DocStrings），
# 它的主要作用就是帮助你的程序文档更加简单易懂。

def printMax2(x, y):
    '''Prints the maximum of two numbers.
The two values must be integers.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, "is maximum.")
    else:
        print(y, "is maximum.")

printMax2(3, 5)
print(printMax2.__doc__)
help(printMax2)



