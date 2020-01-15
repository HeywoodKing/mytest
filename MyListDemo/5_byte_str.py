# -*- coding: utf-8 -*-


# bytes to str
b = b'example'
s = str(b, encoding='utf-8')
print(s)

s = bytes.decode(b)
print(s)

s = "我爱中国"
b = bytes(s, encoding='utf-8')
print(b)

b = str.encode(s)
print(b)
