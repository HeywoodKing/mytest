# -*- encoding: utf-8 -*-
"""
@File           : run.py
@Time           : 2019/11/9 13:47
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import pysnooper


@pysnooper.snoop('E:/log/pysnooper/file.log', depth=2, prefix='pysnooper:', )
def main():
    a = 1
    b = 2
    c = a * b
    print(c)
    print(c * b)
    return c


if __name__ == '__main__':
    main()

