# 第一种方法很简单，只要把一个列表生成式的[]改成()

L= [x * x for x in range(10)]
print(L)


G = (x * x for x in range(10))
print(G)

# print(next(G))
# print(next(G))
# print(next(G))

for x in G:
    print(x)

