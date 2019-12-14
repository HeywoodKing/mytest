# -*- encoding: utf-8 -*-
"""
@File           : setting.py
@Time           : 2019/11/20 17:13
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

ROBOT_ENABLE = True

MONITOR_FRIEND_LIST = [u"Yuki3.14", u'']
MONITOR_GROUP_LIST = [u"泽融", ]
MAX_HISTORY = 10000

START_DAEMON_TYPE = 'thread'  # thread  process


TULING_KEY = ''



#
# # [Group]
# # 定时发送时间
# timing = '00:00:00'
# # 定时发送内容
# timing_send = ""
# # 定时发送群聊
# timing_group = None
#
# # 监控group里面boss发送的包含key的消息到forward_group里面（带前缀）
# forward_prefix = None
# boss_name = None
# boss_key = None
# boss_group = None
# forward_group = None
#
# # 自动回复被group里面@的消息，回复内容为msg
# auto_reply_msg = None
# auto_reply_group = None
# # 每周六定时发送好友统计信息
# week = None
#
# # [Friend]
# # 添加好友信息中包含key的时候回复content
# friend_key = None
# friend_content = None
#
# # [Default]
# # 基础信息，tuling的key和图片地址
# tuling_key = "你的图灵key"
# img_path = None
#
# # [Add_group]
# user_add_group = None
#
# # [Function]
# # 博客地址
# person_url = None
# # 功能列表
# function_list = """回复关键字: 进群
# 博客
# 其他
# 打赏
# 继续我们的互撩吧(* ^ __ ^ * )
# """
#
# # 回复其他的时候获得的列表
# other_function = "回复讲笑话、讲故事、XX座运势、脑筋急转弯、歇后语、绕口令、顺口溜体验更多功能"

