# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import time

bot = Bot(cache_path=True)

myself = bot.self

# msgs = dict('name':'','msg':'')
name, msg = '徐琦', '该下班了'
times = 0

def get_news():
    '''
    获取金山词霸的每日一句
    :return:
    '''
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_news():
    try:
        global times
        times += 1
        print('已发送', times)
        content,note = get_news()

        # friend = bot.friends().search(name)[0]
        # friend.send(u'每日一英文')
        # friend.send(content)
        # friend.send(note)

        myself.send(u'每日一英文')
        myself.send(content)
        myself.send(note)

        # 每86400秒（1天），发送1次
        # 1*24*60*60=86400
        t = Timer(86400, send_news)
        t.start()

        # 15秒钟后停止
        # time.sleep(15)
        # t.cancel()
    except:
        # new_friend = bot.friends().search(u'Yuki3.14')[0]
        # new_friend.send(u"今天消息发送失败了")
        myself.send(u'今天消息发送失败了')



if __name__ == "__main__":
    send_news()
    embed()






