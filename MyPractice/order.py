# Filename:order.py

shoplist = ["apple", "mango", "carrot", "orange", "banana", "peanut"]

# 序列
# 索引操作符
print("Item 0 is", shoplist[0])
print("Item -1 is", shoplist[-1])
print("Item -2 is", shoplist[-2])

# 切片操作符
print("Item 1 to 3 is", shoplist[1:3])
print("Item 2 to end is", shoplist[2:])
print("Item start to end is", shoplist[:])

name = "known"
print("charactor 1 to 3 is", name[1:3])

# 索引同样可以是负数，在那样的情况下，位置是从序列尾开始计算的。
# 因此，shoplist[-1]表示序列的最后一个元素而shoplist[-2]抓取序列的倒数第二个项目

# 切片操作符是序列名后跟一个方括号，方括号中有一对可选的数字，并用冒号分割。
# 注意这与你使用的索引操作符十分相似。记住数是可选的，而冒号是必须的

# 切片操作符中的第一个数（冒号之前）表示切片开始的位置，
# 第二个数（冒号之后）表示切片到哪里结束。如果不指定第一个数，
# Python就从序列首开始。如果没有指定第二个数，则Python会停止在序列尾。
# 注意，返回的序列从开始位置 开始 ，刚好在 结束 位置之前结束。
# 即开始位置是包含在序列切片中的，而结束位置被排斥在切片外。

# 对象与引用
print("Simple Assignment")
mylist = shoplist

del shoplist[0]
print("shoplist is", shoplist)
print("mylist is", mylist)

print("Copy by making a full slice")
mylist = shoplist[:]
print("shoplist is", shoplist)
print("mylist is", mylist)

# 字符串函数
name = "Swaroop"
if name.startswith("Swa"):
    print("Yes, the string starts with 'Swa'")

if "a" in name:
    print("Yes, it contains the string 'a'")

if name.find("war") != -1:
    print("Yes, it contains the string 'war'")

delimiter = "-*-"
mylist = ["Brazil", "Russia", "India", "China"]
print(delimiter.join(mylist))




