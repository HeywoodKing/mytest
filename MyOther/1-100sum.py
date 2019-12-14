# -*- encoding: utf-8 -*-
"""
@File           : 1-100sum.py
@Time           : 2019/12/5 11:04
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""


index = 1
ret = 1
while index < 101:
    if index % 2 == 0:
        print(index)

        ret *= index

    index += 1

print(ret)
