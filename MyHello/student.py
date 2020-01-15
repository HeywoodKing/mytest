# -*- coding: utf-8 -*-

class Student(object):
    # __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
    # 就可以把各种属性绑定到self，因为self就指向创建的实例本身
    # 第一个参数永远是实例变量self，并且，调用时，不用传递该参数,仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
    # 比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
    # 当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
    def __init__(self, name, score):
         self.__name = name
         self.__score = score

    # 这个函数称为类的方法
    def print_score(self):
        print('%s: %s => %s' % (self.__name, self.__score, self.get_grade()))

    # 获取级别
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        elif self.__score >= 70:
            return 'C'
        elif self.__score >= 60:
            return 'D'
        else:
            return 'E'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 实例化一个类
bart = Student('Flack', 99)
# 给实例绑定属性name
# bart.name = "Flack123"
# bart.score = 50

# 不能改变私有变量的属性值，因为这样的话类内部的属性值没有任何改变，改变的仅仅是新增属性而已
# bart.__name = "Flack123"
# bart.__score = 50
# print(bart.__name, bart.__score)

# 谁的成绩谁打印
bart.print_score()
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量
# 改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名
# print(bart._Student__name, 0)

smoke = Student('Lisa', 85)
smoke.print_score()

link = Student('flix', 58)
link.print_score()




