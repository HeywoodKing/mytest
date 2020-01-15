L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L)


# 取前10个元素
r = []
m = 10
for i in range(10):
    r.append(L[i])
print(r)


# 取前10个元素 从0开始取，取10个
print(L[0:10])
print(L[:10])
# 前5-10个
print(L[5:10])
# 后10个数
print(L[-10:])
# 前10个元素，每两个取一个
print(L[:10:2])

# 所有数字，每5个取一个
print(L[::5])

print(L[:])



T = (0,1,2,3,4,5,6,7,8,9)
print(T[:])
print(T[0:5])
print(T[0:5:2])
print(T[:5])
print(T[-10:5])
print(T[::3])



