# list to str

l = [1,2,3,34,54]
# 对于数字型列表，先将数字转为字符，再讲字符转为字符串
s = "".join(str(x) for x in l)
print(s)

l = ['1','2','3','4','5']
s = "".join(l)
print(s)

# str to list

s = "abcdef"
l = list(s)
print(l)

s = "123456"
l = list(s)
print(l)

l = list(int(x) for x in l)
print(l)


s = "333"
i = int(s)
print(i)

i = 432
s = str(i)
print(s)

import random
# 给随机数对象一个种子值，用于产生随机序列。
random.seed(10)
# 随机浮点数
print(random.random())
print(random.random())
print(random.random())

random.seed()
print(random.random())
print(random.random())

# 返回指定范围的一个随机整数，包含上下限
print(random.randint(1,10))

# 随机正态浮点数

print(random.uniform(1,10))


# 按步长随机在上下限范围内取一个随机数
print(random.randrange(1,10,1))


# 对list列表随机打乱顺序，也就是洗牌
item = [1,2,3,4,5,6,7]
random.shuffle(item)
print(item)

item2 = ['1','2','3','5','6','7']
random.shuffle(item2)
print(item2)


item3 = ['a','b','c','d','e','f']
random.shuffle(item3)
print(item3)






