# -*- coding: utf-8 -*-


# import logging
# import sys, os, time, io, traceback, warnings, weakref, collections
# import linecache
# import tokenize
# import re
# from enum import Enum,unique
from wxpy import *


# bot = Bot('bot.pkl',console_qr=True)

# bot = Bot()

# bot = Bot(cache_path=True)#扫码登陆

#
# # 初始化图灵机器人
# tuling = Tuling(api_key='3e1521bf6d464037a7912b1705c09faf')
#
# 调用图灵机器人API，实现自动回复
# 自动回复功能，回复所有消息
# @bot.register(msg_types=TEXT)
# def auto_reply_all(msg):
#     tuling.do_reply(msg)
#
#
# bot.join() #开始运行


# 给指定的人发送消息
def wx_send(name,msg):
    friend = bot.friends().search(name)[0]
    friend.send(msg)

# 定时发送消息
def wx_send_timer(name, msg):
    wx_send(name, msg)

# 统一回复消息
def reply_msg(obj, msg):
    if len(msg) <= 0:
        msg = '我正在忙呢，，，'
    obj.reply(msg)




wx_send('杨颖', '吃饭了没？')

'''
验证信息
'''
def valid_msg(msg):
    return '密码' in msg.text.lower()


'''
邀请用户
使用 bot 的 groups 方法来获取到所有的用户，并使用搜索，取到我们想要的数据
使用 ensure_one 方法来保证只返回一个结果，而不是一个数组
使用 group 的 add_members 方法来邀请用户加入到群聊
'''
def invite(user):
    group = bot.groups().search('“运维密码”体验群')
    group[0].add_members(user, use_invitation=True)

'''
处理加好友信息
'''
# 注册一个监听器
@bot.register(msg_types=FRIENDS)
def new_friends(msg):
    user = msg.card.accept()
    if valid_msg(msg):
        invite(user)
    else:
        user.send('Hello {},你忘了填写加群口令，快回去找找口令吧'.format(user.name))

