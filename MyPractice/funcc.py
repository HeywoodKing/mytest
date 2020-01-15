# Filename:funcc.py

def f(x):
    x = 100
    print x

def ff(x):
    x[0] = 100
    print x
    

a = 1
f(a)
print a

b = [1,2,3]
ff(b)
print b
