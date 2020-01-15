# _*_ coding: utf-8 _*_

i = int('12345')
print(type(i),i)

i = int('12345', base=8)
print(type(i), i)

i = int('12345', base=16)
print(type(i), i)

i = int('12345', base=10)
print(type(i), i)

def int2(x, base=2):
    return int(x, base)

i_byte = int2('111001')
print(i_byte)

i_byte = int2('1000')
print(i_byte)

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
import functools
int2 = functools.partial(int, base=2)
i = int2('1110')
print(i)
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单


