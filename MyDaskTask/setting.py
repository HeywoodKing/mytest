# -*- encoding: utf-8 -*-
"""
@File           : setting.py
@Time           : 2019/11/18 11:13
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import os
import sys

BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)
sys.path.append(BASE_DIR)


DASK_SCHEDULER_URL = '192.168.1.190:8786'

WORK_PATH = r'E:/valid_file'
SAVE_TXT_PATH = r'E:/valid_file_txt'
