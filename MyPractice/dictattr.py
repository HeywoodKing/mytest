# Filename:dictattr.py

class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age
    def getAdult(self):
        if self.age > 1.0:
            return True
        else:
            return False
    adult = property(getAdult)

    def __getattr__(self, name):
        if name == 'adult':
            if self.age > 1.0:
                return True
            else:
                return False
        else:
            try:
                raise AttributeError(name)
            except:
                print("raise exception error!")

class num(object):
    def __init__(self,value):
        self.value = value
    def getNeg(self):
        return -self.value
    def delNeg(self):
        print('value also deleted.')
        del self.value
    def setNeg(self,value):
        self.value = -value
    neg = property(getNeg,setNeg,delNeg,"I'm negative.")

summer = chicken(2)

print(bird.__dict__)
print(chicken.__dict__)
print(summer.__dict__)


summer.__dict__['age'] = 30
print(summer.__dict__['age'])

summer.age = 0.5
print(summer.age)

print(summer.__class__.__base__.__base__)
print(summer.__class__.__base__.__class__)

print("adult:" + str(summer.adult))

print("male:" + str(summer.male))


x = num(1.1)
print("x:" + str(x.neg))
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg
