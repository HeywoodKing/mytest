# -*- encoding: utf-8 -*-
"""
@File           : helper.py
@Time           : 2019/12/28 14:49
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import datetime


def write_log(txt):
    with open('job_list.txt', 'a', encoding='utf8') as f:
        f.write("\r\n")
        f.write("+" * 100)
        f.write("\n{}：{}\n".format(datetime.datetime.now(), txt))
        f.write("+" * 100)
