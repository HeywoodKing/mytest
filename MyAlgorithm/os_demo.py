# -*- coding: utf-8 -*-

import os
import sys
from pprint import pprint

# print(os.remove('./temp/1.txt'))
# os.rename('./temp/2.txt', './temp/1.txt')
# print(os.walk('./temp'))
# for root, dirs, files in os.walk('./temp'):
#     print(root)
#     print(dirs)
#     print(files)
#     for line in files:
#         # print(line)
#         with open(root + '/' + line, 'a+', encoding='utf-8') as f:
#             if len(f.read()) <= 0:
#                 f.write('test')
#             else:
#                 print(f.read())

# os.chdir('./temp')

pprint(dir(sys))
# print(sys.__doc__)
print(sys.path, sys.platform, sys.prefix)
