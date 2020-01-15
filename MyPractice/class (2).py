# -*- coding:utf-8 -*-

class Animal(object):

    def run(self):
        print('running always')

class Dog(Animal):
    def run(self):
        print('dog is running')

    def eat(self):
        print('dog is eating')


class Cat(Animal):
    def run(self):
        print('cat is running')

    def eat(self):
        print('cat is eating')


# animal = Animal()
# if(isinstance(animal,Animal)):
#     print('OK')
# else:
#     print('Not')


def run_a(animal):
    animal.run()


dog = Dog()
# dog.run()
run_a(dog)

cat = Cat()
run_a(cat)


# 对扩展开放:允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_a()等函数
# 继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。
# 而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树

# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
class Timer(object):
    def run(self):
        print('Start...')

# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
# 你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象