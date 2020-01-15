# Filename:package.py

def func(*name):
    print type(name)
    print name

func(1,4,6)
func(5,6,7,1,2,3,4)


def func2(**dict):
    print type(dict)
    print dict

func2(a = 1,b = 3)
func2(m = 2,c = 9, b = 1)

def func3(a,b,c):
    print a,b,c

args = (1,3,4)
func3(*args)  #½â°ü¹ü

def func4(a,b,c,d):
    print a,b,c,d

dict = {'a':1,'b':2,'c':3,'d':4}
func4(**dict)

