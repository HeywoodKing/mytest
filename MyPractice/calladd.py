# Filename:calladd.py

class SampleMore(object):
    def __call__(self,a):
        return a + 5

add = SampleMore()
print(add(2))
print(map(add, [2, 4, 5]))

class student(object):
    def __getattr__(self, name):
        return object.__getattribute__(name)
