# -*- coding utf-8 -*-

import math

# n1 = 255
# n2 = '1000'

# print(hex(n1))
# print(int(n2, 2))

def quadratic(a, b, c):
	# a * math.pow(x, 2) + b * x + c = 0
	if a==0:
		TypeError('a不能为0')
	if not isinstance(a, (int,float)) or not isinstance(b, (int,float)) or not isinstance(c, (int,float)):
		raise TypeError('Bad operand type')
	delta = math.pow(b, 2) - 4*a*c
	if delta < 0:
		return '无实根'
	x1 = (math.sqrt(delta)-b)/(2*a)
	x2 = -(math.sqrt(delta)+b)/(2*a)
	return x1, x2

print(quadratic(2,3,1))
print(quadratic(1,3,1))


# 关键字参数
def person(name, age,**kw):
	print(name, age, kw)

person('Flack', 20)

person('Flack', 20, city = 'xi‘an')
person('Flack', 20, country = 'china')

extra = {'city': 'beijing', 'country': 'china'}
person('Flack', 30, **extra)


# 命名关键字参数
def getPerson(name, age,*, city, job):
	print(name, age, city, job)


getPerson('Jack', 24, city='Beijing', job='Engineer')
