# -*- encoding: utf-8 -*-
"""
@File           : run
@Time           : 2019/12/23
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import fire
from mytranslate.pytranslate import exec


def main():
    try:
        exec()
    except Exception as ex:
        print(ex)
        main()


if __name__ == '__main__':
    fire.Fire(main)
