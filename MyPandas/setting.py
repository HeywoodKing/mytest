# -*- encoding: utf-8 -*-
"""
@File           : setting.py
@Time           : 2019/11/20 10:51
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


# 开发配置
MYSQL_HOST = '192.168.1.163'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'mofang123'
MYSQL_DATABASE = 'db_test'
MYSQL_CHARSET = 'utf8'
# MYSQL_CHARSET = 'utf8mb4'
DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT,
                                                            MYSQL_DATABASE, MYSQL_CHARSET)


FILE_PATH = r'E:/test/tb_electron_factory - 副本.xlsx'



