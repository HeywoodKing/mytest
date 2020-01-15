# -*- coding: utf-8 -*-

from pprint import pprint
from collections import defaultdict

dict1 = {
    'aaa': 123,
    'bbb': 345,
    'ccc': 'asfsdf',
    'dd': 34,
    23: '434',
    87: 'dfsdf'
}

# print(dict1)
# pprint(dict1)

# print(dict1.items, dict1.items())
for item in dict1.items():
    print(item)

for index, key in enumerate(dict1):
    print(index, key, dict1[key])
    # print(index, key)
    
dict2 = defaultdict(lambda: 100)
print(dict2[12])
dict2[12] = '120'
print(dict2[12])

