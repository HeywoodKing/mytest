# Filename:sayHello.py
# ����
def sayHello():
    print("Hello world!")

#���ú���
sayHello()

# ���βκ���
def printMax(a, b):
    if a > b:
        print(a, "is maximum.")
    else:
        print(b, "is maximum.")

printMax(10, 30)

# �ֲ�����
def func(x):
    print("x is ", x)
    x = 2
    print("Changed local x to ", x)
x = 50
func(x)
print("x is still ", x)


# Ĭ�ϲ���ֵ
def say(message, times = 1):
    print(message * times)

say("ha")

say("ha", 2)


# �ؼ�����
def func(a, b = 5, c = 10):
    print("a is", a, "and b is", b, " and c is", c)

func(3, 7)
func(25,c = 24)
func(c = 50, a = 100)


# return���
def maximum(x, y):
    if x > y:
        return x
    else:
        return y

print(maximum(2, 3))


# �ĵ��ַ���DocStrings
# Python��һ����������ԣ������ĵ��ַ�����DocStrings����
# ������Ҫ���þ��ǰ�����ĳ����ĵ����Ӽ��׶���

def printMax2(x, y):
    '''Prints the maximum of two numbers.
The two values must be integers.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, "is maximum.")
    else:
        print(y, "is maximum.")

printMax2(3, 5)
print(printMax2.__doc__)
help(printMax2)



