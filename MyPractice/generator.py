# Filename:generator.py

def gen():
    a = 100
    yield a
    a = a * 8
    yield a
    yield 1000


#print gen()

for i in gen():
    print i


def gen2():
    for i in range(4):
        yield i

#���������ʽ
#G = (x for x in range(4))

