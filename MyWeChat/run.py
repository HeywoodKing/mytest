# -*- coding: utf-8 -*-


import itchat
from datetime import datetime
import time
import threading


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    # itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])
    itchat.send('%s' % msg['Text'], msg['FromUserName'])


def get_weather():
    pass


def get_days():
    now = datetime.now()
    start_day = datetime(2013, 12, 8)
    days_num = (now - start_day).days
    return days_num


def say_love(nick_names):
    print(nick_names)
    # nick_name = 'Yuki3.14'
    while True:
        now_time = datetime.now()
        print(str(now_time.hour) + ":" + str(now_time.minute))
        if now_time.hour == 23 and now_time.minute == 23:
            message = '亲爱的，已经很晚了，该睡觉了，这样我就会梦见你'
        elif now_time.hour == 8 and now_time.minute == 8:
            message = '亲爱的，今天是我们在一起的' + str(get_days()) + '天了，我每天都记着呢，而且每天我都告诉你，我爱你！！！'
        else:
            message = None

        if message:
            for item in nick_names:
                try:
                    # name, nickName这两个都可以 remarkName不可以
                    userinfo = itchat.search_friends(name=item)
                    username = userinfo[0]['UserName']
                    itchat.send(message, toUserName=username)
                    # itchat.send_msg(message, toUserName=username)
                except:
                    print('error', item)
                    continue

        time.sleep(60)


t = threading.Thread(target=say_love, args=(['Yuki3.14', '杨颖', ],))
# t.setDaemon(True)
t.start()
# t.join()

itchat.auto_login()
itchat.run()



