# -*- coding: utf-8 -*-


s = ' hello world, my name is king. '
print(s.find('name'), s.rfind('hello'))
# print(s.index('nameking'), s.rindex('king'))
print(s.count('m'))
print(s.replace('he', 'ha'))
print(s.split())
print(s.lstrip().capitalize())
print(s.strip().title())
print(s.startswith('hello'), s.startswith(' hello'))
print(s.endswith('.'), s.endswith(' '))
print(s.lower(), s.upper())
print(s.strip().ljust(10, '*'), s.strip().rjust(40, '*'))
print(s.lstrip().center(50, '+'))
print(s.rstrip().center(50, '+'))
print(s.partition('my'), s.rpartition('name'))

s1 = 'ok\r\nthis is balar\r\b123'
s2 = 'aaabbbccc'
s3 = '123456'
s4 = s2 + '666'
s5 = ' '
print(s1.splitlines())
print(s2.isalpha(), s1.isalpha())
print(s1.isdigit(), s3.isdigit(), s4.isalnum())
print(s.isspace(), s5.isspace())
s6 = s2.join('_')
print(s6)

test_str = 'haha hoa nihao \t heihei \t wo shishui a hao people'
print(test_str.split(), test_str.split()[-2])


dicts = {
    'name': 'king',
    'age': 34,
    'work': 'enginer',
    'addr': '甘肃天水'
}

for k in dicts.keys():
    print(k)

for v in dicts.values():
    print(v)

for item in dicts.items():
    print(item)

for k, v in dicts.items():
    print(k, v)

for index, key in enumerate(dicts):
    print(index, key, dicts[key]*2)

if 'name' in dicts:
    print('ok')
else:
    print('error')

# if 'king' in dicts:
#     print('ok')
# else:
#     print('error')
