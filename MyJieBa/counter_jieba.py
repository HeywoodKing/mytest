
import collections
import pprint
from jieba import cut


a = 'hello world, my name is ok, how are you? you are dader'
res = collections.Counter(a,)
print(res)

res = collections.Counter(cut(a))
print(res)
