
print('可变的List')

list1 = ['a', 'b', 'c', 'd'];
list2 = ['ching', 1997, 2001, 2017];

print('list1[0]:', list1[0]);
print('list2[3]:', list2[3]);
print('list2[1:3]:', list2[1:3]);

print(list1[-1])
print(list2[-4])

list2.append(2018);

list2.insert(1, 'flack')

print('list2[4]:', list2[4]);

print('list2[0:]:', list2[0:]);

# cmp(list1, list2)
list2.pop();

print('list2[0:]:', list2[0:]);

print(len(list2));
# print(max(list2));
# print(min(list2));



L = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]

# L.pop()

print(len(L))

print(L[0][0])

print(L[1][1])

print(L[2][2])

m = 0
n = 0
for x in L:
	for y in x:
		print('L[%d][%d] = %s' % (m, n, y))
		n += 1
	m += 1
	n = 0


LL = ['Apple', 'Bart', 'Flack', 'Lisa', 'Adam']
for x in LL:
	print('Hello, %s!' % x)
