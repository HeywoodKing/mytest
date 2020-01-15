# -*- coding: utf-8 -*-

# 继承
class Animal(object):
    def run(self):
        print('Animal is running')

    def __len__(self):



# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，
# 总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态
class Dog(Animal):
    def run(self):
        print('Dog is running')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')


def run_twice(animal):
    animal.run()
    animal.run()

animal = Animal()
run_twice(animal)

dog = Dog()
# dog.run()
run_twice(dog)

cat = Cat()
# cat.run()
run_twice(cat)

tortoise = Tortoise()
run_twice(tortoise)

