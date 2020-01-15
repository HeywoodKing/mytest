# -*- coding: utf-8 -*-

class Person(object):

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        # if gender.strip() != '':
        #     self.__gender = gender
        # else:
        #     raise ValueError('bad gender')

        if gender.strip():
            self.__gender = gender
        else:
            raise ValueError('bad gender')

    def print_per(self):
        print('%s, %s' % (self.__name, self.__gender))


lisa = Person('Linda', '女')
lisa.print_per()
lisa.set_gender('男')
lisa.print_per()

