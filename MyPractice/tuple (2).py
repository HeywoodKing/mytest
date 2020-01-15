
print('不可变的Tuple')

tuple1 = (1, 2, 'aa', 'flack')

print(tuple1[2])

print(tuple1[0:])

dic = {12, 32, 'chook'}

print(dic.pop())

for x in tuple1:
	print('tuple:', x)

age = 25
# if age >= 18:
# 	print('您已经成年了')
# else:
# 	print('您还未成年')


if age >= 18:
	print('您已经成年了')
elif age >= 12:
	print('您已经长大了')
elif age >= 6:
	print('您该上小学了')
elif age >= 3:
	print('您该上幼儿园了')
else:
	print('您还小，多吃饭，快快成长')

sum = 0
for x in range(101):
	sum += x
print(sum)

sum = 0
n = 99
while n > 0:
	sum += n
	n -= 2
print(sum)