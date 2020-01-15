# Filename:pratice.py

print 1 + 9
print 1.3 - 4
print 3 * 5
print 6 / 5
print 3 ** 2
print 10 % 3

print 5 == 6
print 8.0 != 8.0
print 3 < 3, 3 <= 3
print 4 > 5, 4 >= 0
print 5 in [1, 3, 5]
print 6 is int
print 3.0 is not float
print 3.1 is int

print True and True, True and False
print True or True
print not True

print  5 == 6 or 3 >= 3

print 10.0 / 3
print 10 / 3.0
print 10 / 3
print 3 / 8.0
print 3.0 / 8
print 3 / 8

i = 1
if i > 0:
    x = 1
    y = 2

print x,y

for a in [3, 4, 4.5, 'life']:
    print a

idx = range(5)
print idx

for a in range(10):
    print a ** 2

while i < 10:
    print i
    i = i + 1
    if i == 6:
        continue
    elif i > 7:
        break

def square_sum(a, b):
    c = a ** 2 + b ** 2
    return c

print square_sum(3 ,4)

def change_integer(a):
    a = a + 1
    return a
print change_integer(a)
print a

b = [1, 2, 3]
def change_list(b):
    b[0] = b[0] + 1
    return b
print change_list(b)
print b



