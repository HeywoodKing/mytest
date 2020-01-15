# -*- coding: utf-8 -*-


import re
import pickle


res = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(res)

res = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(res)

s = 'tea for too'
new_s = s.replace('too', 'two')
print(new_s)

