# Filename:zoo

# 元组 元组和列表十分类似，只不过元组是不可以改变的，即不能被修改
# 元组是用一对圆括号()表示，每项数据之间也是用逗号隔开。
# 元组通常用在使语句或用户定义的函数能够安全地采用一组值的时候，
# 即被使用的元组的值不会改变。
zoo = ("wolf", "elephant", "penguin")
print("Number of animals in the zoo is",len(zoo))

new_zoo = ("monkey", "dolphin", zoo)
print("Number of animals in the new zoo is",len(new_zoo))

print("All animals in new zoo are", new_zoo)
print("Animals brought from old zoo are", new_zoo[2])
print("Last animal brought form old zoo is", new_zoo[2][2])

# 元组最通常的用法是用在打印语句中。
age = 22
name = "Ching"
print("%s is %d years old" % (name, age))
print("Why is %s playing with that python?" % name)
