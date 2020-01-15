# -*- coding: UTF-8 -*-

class Employee:
    "所有员工的基类"
    empCount = 0

    def __init__(self, name, salary):
        # 类的构造函数或初始化方法
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' % Employee.empCount)

    def displayEmployee(self):
        print('Name:', self.name, ',Salary:', self.salary)

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, '销毁')

print(Employee.__doc__)
print(Employee.__class__)
print(Employee.__name__)
print(Employee.__bases__)
print(Employee.__dict__)
print(Employee.__module__)

emp = Employee('gao', 9000)
emp.age = 30
emp.displayCount()
emp.displayEmployee()


emp2 = Employee('liu', 7000)
emp2.age = 29
emp2.displayCount()
emp2.displayEmployee()



class Parent:
    "基类"
    parentAttr = 100

    def __init__(self):
        print('调用父类的构造函数')

    def parentMethod(self):
        print('调用父类的方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('父类属性：', Parent.parentAttr)


class Child(Parent):
    "子类"
    def __init__(self):
        print('调用子类构造方法')

    def childMethod(self):
        print('调用子类方法 child method')

    def parentMethod(self):
        print('重写了父类的方法')


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(20)
c.getAttr()


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d) ' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)

print(v1 + v2)




