# Filename:queue_advance.py

s = ('a','bb','ccc')

print(len(s))
print(min(s))
print(max(s))
print(all(s))
print(any(s))

a = [10,2,23,4,58,6]
print(sum(a))
print(a.count(2))
print(a.index(23))
b = [12]
a.extend(b)
print(a)
a.append(15)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.pop()
print(a)
del a[0]
print(a)
