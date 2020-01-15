# -*- coding: utf-8 -*-

from wxpy import *

bot = Bot(cache_path=True)
bot.enable_puid('wxpy_puid.pkl')
bot.auto_mark_as_read = True
friends = bot.friends(update=False)

groups = bot.groups(update=False)

chats = bot.chats(update=False)

# print(len(chats), chats)

print(len(friends), friends)
#
# print(friends.search('Yuki3.14'))
#
# print(friends.search('Yuki3.14')[0])
#
# print(len(groups), groups)

friend = friends.search('Yuki3.14')[0]

# friend = ensure_one(friend_obj)

print(friend.puid)
# friend.send('Hello chat')
# friend.send_image('a.jpg')

# 打印来自其他好友，群聊和公众号的消息
@bot.register()
def print_all_msg(msg):
    print(msg)


@bot.register(friend)
def reply_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')







bot.join()


