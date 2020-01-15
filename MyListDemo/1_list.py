# -*- coding: utf-8 -*-


# import pprint

#                   列                   行
ls = [[i + j for i in range(6)] for j in range(3)]
print(ls)
# print(ls[0][5])
# print(ls[2][3])
# print(ls[1][1:4])
# print(ls[0:2])
# print(ls[1:2])
# print(ls[1:])
# print(ls[1:][0:])
# print(ls[1:][1])

res = []
# for i in ls:
#     for j in i[2:5]:
#         res.append(j)

# for i in ls:
#     res.append(i[2:5])

res = [i[2:5] for i in ls]*2

print(res)
