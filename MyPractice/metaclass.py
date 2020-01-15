# -*- coding: utf-8 -*-

# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# metaclass，直译为元类
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    # __new__()
    # 方法接收到的参数依次是：
    #
    # 当前准备创建的类的对象；
    #
    # 类的名字；
    #
    # 类继承的父类集合；
    #
    # 类的方法集合。
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass
class MyList(list, metaclass=ListMetaclass):
    pass


myList = MyList()
myList.add(1)
myList.add(34)
print(myList)




