# Filename:class_domain.py

class Person:
    population = 0

    def __init__(self,name):
        self.name = name
        print("(Initializing %s)" % self.name)

        Person.population += 1

    def __del__(self):
        print("%s says bye." % self.name)

        Person.population -= 1

        if Person.population == 0:
            print("I am the last one.")
        else:
            print("There are still %d people left." % Person.population)

    def sayHi(self):
        print("Hi,my name is %s." % self.name)

    def howMany(self):
        if Person.population == 1:
            print("I am the only person here.")
        else:
            print("We are %d person here." % Person.population)
    

ching = Person("Ching")
ching.sayHi()
ching.howMany()


admin = Person("Admin")
admin.sayHi()
admin.howMany()

del admin
del ching
