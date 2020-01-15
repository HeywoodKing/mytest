# -*- coding utf-8 -*-

L = ['123', 18, 'Hello', 'World', 'IBM', None]

# 根据条件迭代，下面语句解决非字符串类型没有lower()方法而报错的问题
[s.lower() for s in L if isinstance(s, str)]
