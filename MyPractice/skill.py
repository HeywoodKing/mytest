# Filename:skill.py

nfc = ["Packers", "49ers"]
afc = ["Ravens", "Patriots"]
print nfc + afc
print str(1) + " world"
print `1` + " world"
print 1, "world"
print nfc, 1
for teama, teamb in zip(nfc, afc):
     print teama + " vs. " + teamb


teams = ["Packers", "49ers", "Ravens", "Patriots"]
for index, team in enumerate(teams):
    print index, team

numbers = [1,2,3,4,5,6]
even = []
for number in numbers:
    if number%2 == 0:
        even.append(number)

numbers = [1,2,3,4,5,6]
even = [number for number in numbers if number%2 == 0]

teams = ["Packers", "49ers", "Ravens", "Patriots"]
print {key: value for value, key in enumerate(teams)}

items = [0]*3
print items

teams = ["Packers", "49ers", "Ravens", "Patriots"]
print ", ".join(teams)

data = {'user': 1, 'name': 'Max', 'three': 4}
try:
   is_admin = data['admin']
except KeyError:
   is_admin = False

data = {'user': 1, 'name': 'Max', 'three': 4}
is_admin = data.get('admin', False)

#除后向下取整
print 5.0//2

# 2的5次方
print 2**5

print .3/.1
print .3//.1

x = 2
if 3 > x > 1:
   print x

if 1 < x > 0:
   print x


x = 6
y = 5
 
x, y = y, x
 
print x
print y


print "Hello" if True else "World"

x = [1,2,3,4,5,6]
#前3个
print x[:3]
#>>> [1,2,3]
#中间4个
print x[1:5]
#>>> [2,3,4,5]
#最后3个
print x[-3:]
#>>> [4,5,6]
#奇数项
print x[::2]
#>>> [1,3,5]
#偶数项
print x[1::2]
#>>> [2,4,6]
#写一个程序，打印数字1到100，3的倍数打印“Fizz”来替换这个数，
#5的倍数打印“Buzz”，对于既是3的倍数又是5的倍数的数字打印“FizzBuzz”。
for x in range(101):print"fizz"[x%3*4::]+"buzz"[x%5*4::]or x


from collections import Counter
print Counter("hello")
#>>> Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

from itertools import combinations
teams = ["Packers", "49ers", "Ravens", "Patriots"]
for game in combinations(teams, 2):
    print game
#>>> ('Packers', '49ers')
#>>> ('Packers', 'Ravens')
#>>> ('Packers', 'Patriots')
#>>> ('49ers', 'Ravens')
#>>> ('49ers', 'Patriots')
#>>> ('Ravens', 'Patriots')


False = True
if False:
   print "Hello"
else:
   print "World"
#>>> Hello
