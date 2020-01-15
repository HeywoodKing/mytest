
# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
# 定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n +1
    return 'done'

# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib2(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a + b
        n = n +1
    return 'done'

# fib(10)
fib2(10)