# -*- encoding: utf-8 -*-
"""
@File           : setting.py
@Time           : 2020/4/18 13:37
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import os
from fake_useragent import UserAgent


UA = UserAgent(
    verify_ssl=False,
    path=os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/fake_useragent_v0.1.11.json'
)

BAIDU_URL = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
