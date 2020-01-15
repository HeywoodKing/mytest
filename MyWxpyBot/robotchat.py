# -*- coding:utf-8 -*-

from wxpy import *


bot = Bot(cache_path=True)

tuling = Tuling(api_key='3e1521bf6d464037a7912b1705c09faf')

nickname = '浅轩'
friends = bot.friends()
friend = friends.search(nickname)[0]
groups = bot.groups()
group = groups.search('美团红包')[0]
# boss = group.search('老板娘')[0]

# 让机器人与所有好友和群聊天
# @bot.register()
# def auto_reply(msg):
#     tuling.do_reply(msg)

# 使用图灵机器人自动与所有群聊天，仅仅回复@我的消息
@bot.register(chats=groups, msg_types=TEXT)
def reply_groups(msg):
    if msg.is_at:
        # msg.reply(msg.text)
        tuling.do_reply(msg)
    elif '小白' in msg.text:
        tuling.do_reply(msg)
    else:
        pass
    # if msg.member == boss:  # 如果是群里的指定的人消息转发到我的文件助手里面
    #     msg.forword(bot.file_helper, prefix='老板发言')

    print(msg, msg.member, msg.text)

# 使用图灵机器人自动与指定群聊天
@bot.register(chats=group, msg_types=TEXT)
def reply_group(msg):
    # if msg.is_at:
    #     msg.reply(msg.text)
    # if msg.member == boss:  # 如果是群里的指定的人消息转发到我的文件助手里面
    #     msg.forword(bot.file_helper, prefix='老板发言')
    tuling.do_reply(msg)
    print(msg.text)

# 和自己聊天
@bot.register(chats=bot.self,except_self=False)
def reply_self(msg):
    tuling.do_reply(msg)
    print(msg)

# 使用图灵机器人自动与所有好友聊天
# @bot.register(chats=[FRIENDS])
# def reply_friend(msg):
#     tuling.do_reply(msg)

# 使用图灵机器人自动与指定好友聊天
@bot.register(chats=friend, msg_types=TEXT)
def reply_friend(msg):
    tuling.do_reply(msg)


if __name__ == "__main__":
    print('小白正在运行...')
    bot.start()
    embed()

