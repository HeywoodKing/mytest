s = set([10,2,3])
print(s)



s = set([1,2,2,2,2,3,3,3])
s.add(45)
s.remove(3)
print(s)

s1 = set([2,3,3,4,4,5,5])

# 交集
print(s & s1)  

print(s | s1)

# L = [23,'ching', 56]
# s.add(L)

tuple1 = (1,2,3)
tuple2 = (1,[2,3])
s = set(tuple1)
print(s)

# 不可以的
# s = set(tuple2)
# print(s)
