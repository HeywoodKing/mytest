# -*- coding utf-8 -*-
# 素数为在大于1的自然数中，除了1和它本身以外不再有其他因数。
# 质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数。
# 质数（prime number）又称素数，有无限个
# 求质数（素数）的方法
#
# def get_odd(n, L):
#     R = []
#     E = []
#     for x in L:
#         if(x % n == 0):
#             R.append(x)  # 非素数
#         else:
#             E.append(x)  # 素数
#
#     return E
#
# def get_filter(n):
#     res = []
#     L = list(range(2, n))
#     print(L)
#     while len(L) > 0:
#         res.append(L[0])
#         L = get_odd(L[0], L[1:])
#
#     print(res)
#
# get_filter(1000)


# for y in tmp:
#     res.append(y)
# l1 = res
# l2 = list(set(l1))
# l2.sort(key = l1.index)
# print(l2)


def get_prime_number(n):
    res = []
    # L = list(range(2, n))
    L = [x for x in range(2, n)]
    print("源数据：", L)
    while len(L) > 0:
        res.append(L[0])
        NP = []
        P = []
        for x in L:
            if (x % L[0] == 0):
                NP.append(x)  # 非素数
            else:
                P.append(x)  # 素数
        L = P

    print("素数：", res)

get_prime_number(100)



# 筛选出回数
def get_palindrome_number(n):
    res = []
    L = [x for x in range(2, n)]
    print("源数据：", L)
    for x in L:
        if x > 10:
            s1 = str(x)
            s2 = s1[::-1]
            # print("s1=",s1, "s2=", s2)
            if s1 == s2:
                res.append(x)
    print("回数：", res)


get_palindrome_number(100)


# 字符串翻转
# ========================================================
# 第一种使用字符串切片
s = "abcdef123"
# res = s[::-1]
# print(res)


# 第二种使用列表的reverse方法
# l = list(s)
# r = list(reversed(l))
# res = "".join(r)
# print(res)


# 第三种
# l = list(s)
# res = "".join(l[::-1])
# print(res)


# 第四种使用reduce
# from functools import reduce
# res = reduce(lambda x,y:y+x,s)
# print(res)


# 第五种使用递归函数  ???
# def func(s):
#     if len(s) < 1:
#         return s
#     return func(s[1:]) + s[0]
#
# res = func(s)
# print(res)


# 第六种使用栈
# def func_stack(s):
#     l = list(s)
#     res = ''
#     while len(l) > 0:
#         res += l.pop()
#     return res
#
# res = func_stack(s)
# print(res)


# 第七种for循环
# def func_for(s):
#     res = ""
#     max_index = len(s) - 1
#     for index,value in enumerate(s):
#         res += s[max_index - index]
#     return res
#
# res = func_for(s)
# print(res)


# ========================================================



