# _*_ coding: utf-8 _*_

l = list(map(lambda x: x*x,[1,2,3,4,5,6,7,8,9]))
print(l)

def build(x, y):
    return lambda: x*x + y*y

res = build(3,4)
print(res())


# 奇数
def is_odd(n):
    return n % 2 == 1

# 偶数
def is_even(n):
    return n % 2 == 0
o = list(filter(is_odd, range(1,20)))
e = list(filter(is_even, range(1,20)))
print(o,e)

# 改造上述函数为匿名函数
o = list(filter(lambda x:x%2 == 1, range(1,20)))
e = list(filter(lambda x:x%2 == 0, range(1,20)))
print(o,e)

