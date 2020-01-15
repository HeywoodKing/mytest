# -*- coding utf-8 -*-

ss = "abcdefg"

print(ss)
# 1.使用字符切片
print(ss[::-1])

# 2.使用列表的reverse方法
l = list(ss)
# print(l)
# l.reverse()
# # print(l)
# rr = "".join(l)
# print(rr)


res = "".join(l[::-1])
print(res)

# 3.使用reduce
# res = reduce(lambda x,y : y+x,s)

# 4.使用递归函数
# def func(s):
#     if len(s) < 0:
#         return s
#     return func(s[1:]) + s[0]
# res = func('abcdefg')

# 5.使用栈
# def func(s):
#     l = list(s)
#     res = ""
#     while len(l) > 0:
#         res += l.pop()
#     return res
#
# res = func("abcdefg")

# 6.for循环
# def func(s):
#     res = ""
#     max_index = len(s) - 1
#     for index,value in enumerate(s):
#         res += s[max_index - index]
#     return res
#
# res = func("abcdefg")



