# -*- encoding: utf-8 -*-
"""
@File       : setting.py
@Time       : 2019/10/14 11:10
@Author     : Flack
@Email      : opencoding@hotmail.com
@ide        : PyCharm
@project    : MyTest
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

ES_ADDRESS = ['http://192.168.1.106:9200']
ES_USER = None
ES_PWD = None
ES_TIMEOUT = 3600
