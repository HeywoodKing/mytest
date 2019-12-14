# -*- encoding: utf-8 -*-
"""
@File           : run.py
@Time           : 2019/11/20 17:13
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
from MyWxPy.mywxpy.scheduler import Scheduler


def main():
    try:
        s = Scheduler()
        s.run()
    except Exception as ex:
        print(ex)
        main()


if __name__ == '__main__':
    main()
