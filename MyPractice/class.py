# Filename:class.py

class Person:
    def __init__(self,name):
        self.name = name
        
    def sayHi(self):
        print("Hello,how are you?")

    def sayHello(self):
        print("Hello,my hello!")


p = Person("Known")
p.sayHi()
p.sayHello()

