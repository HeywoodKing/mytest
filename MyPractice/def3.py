# -*- coding utf-8 -*-
#
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

# res = fact(1)
# print(res)
#
# res = fact(2)
# print(res)
#
# res = fact(3)
# print(res)
#
# res = fact(4)
# print(res)
#
# res = fact(5)
# print(res)
#
# res = fact(6)
# print(res)
#
# res = fact(7)
# print(res)
#
# res = fact(8)
# print(res)
#
# res = fact(9)
# print(res)
#
# res = fact(10)
# print(res)

# res = fact(1000)
# print(res)




# 解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
# 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
#
# def fact2(n):
#     return fact_iter(n, 1)
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#
#     return fact_iter(num - 1, num * product)

# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出
# res = fact2(1000)
# print(res)


def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        # 将A柱子上的n-1个移动到B柱子上
        hanoi(n - 1, a, b, c)
        # 将A柱子上最底下的一个移动到C柱子上
        print(a, '-->', c)
        # 最后将B柱子上的移动到C柱子上
        hanoi(n - 1, b, a, c)


hanoi(2, 'A', 'B', 'C')