import wxpy
import re

# 实例化微信对象
bot = wxpy.Bot(cache_path=True)

# 启用puid 并指定puid所需映射数据保存的路径
bot.enable_puid(path='wxpy_puid.pkl')

# 用于存放每个用户最近发送的消息
msgs = dict()

# 信息的类型
msg_types = {
    'Text': '文本',
    'Map': '位置',
    'Picture': '图片',
    'Video': '视频',
    'Attachment': '文件',
    'Sharing': '分享',
    'Card': '名片',
    'Recording': '语音',
}


@bot.register()
def handle_receive_msg(msg):
    """
    监听消息
    :param msg: 接收到的消息
    :return:
    """
    # 原信息数据
    raw = msg.raw
    print(msg)
    print(raw)

    # 如果消息的状态码是4  即撤回消息
    if raw.get('Status') == 4:
        print('撤回消息')
        # 如果是群消息
        if isinstance(msg.chat, wxpy.api.chats.group.Group):
            print(1)
            # 获取群成员的puid
            puid = msg.member.puid
            # 获取发送者的昵称
            name = msg.member.nick_name
        # 如果是好友消息
        elif isinstance(msg.chat, wxpy.api.chats.friend.Friend):
            print(2)
            # 获取好友的puid
            puid = msg.chat.puid
            # 获取好友的昵称
            name = msg.chat.nick_name
        else:
            print(3)
            puid = None
            name = None
        if puid:
            print(4)
            print('puid %s' % puid)
            # 被撤回消息的msgid的匹配规则
            msg_id_regex = re.compile('<msgid>(\d+)</msgid>')
            print(14)
            print(16,raw.get('Content'))
            # 获取被撤回消息的msgid
            old_msg_id = msg_id_regex.findall(raw.get('Content'))[0]
            print(15)
            # 获取该发送者的最后5次的消息记录
            chat_msgs = msgs.get(puid)
            print(16)
            print(chat_msgs)
            # 遍历消息记录
            for chat_msg in chat_msgs[::-1]:
                # 跳过不是被撤回的信息
                if str(chat_msg.id) != old_msg_id:
                    continue
                chat = chat_msg.chat
                # 如果被撤回的信息是文本信息
                if chat_msg.type == "Text":
                    print(5)
                    # 如果消息长度过长 则不予处理
                    if len(chat_msg.text) >= 150:
                        print(6)
                        warning = "【您撤回的消息过长，有炸群嫌疑，不予处理！！！】"
                        bot.file_helper.send('%s撤回了一条文本消息--【%s】'.decode('utf-8') % (name, warning))
                        break
                    # 将此消息转发出来
                    chat_msg.forward(chat, prefix='%s撤回了一条文本消息，消息内容为：'.decode('utf-8') % name)
                # 如果被撤回的是位置信息
                elif chat_msg.type == "Map":
                    print(7)
                    # 位置信息的匹配规则
                    map_regex = re.compile(r'label="(.+?)"')
                    # 获取位置信息中的位置
                    map = map_regex.findall(chat_msg.raw.get("OriContent"))[0]
                    # 将位置信息发出来
                    msg.reply('%s撤回了一条位置消息，位置信息为：【%s】'.decode('utf-8') % (name, map))
                else:
                    print(8)
                    # 获取信息的类型
                    msg_type = msg_types.get(chat_msg.type).decode('utf-8')
                    # 将信息转发出来
                    chat_msg.forward(chat, prefix='%s撤回了一条%s消息， 消息内容为：'.decode('utf-8') % (name, msg_type))
                break
    else:
        print(9)
        # 如果是群消息
        if isinstance(msg.chat, wxpy.api.chats.group.Group):
            print(10)
            # 获取群成员的puid
            puid = msg.member.puid
        # 如果是好友消息
        elif isinstance(msg.chat, wxpy.api.chats.friend.Friend):
            print(11)
            # 获取好友的puid
            puid = msg.chat.puid
        else:
            print(12)
            puid = None
        if puid:
            print(13)
            # 记录消息
            msgs.setdefault(puid, []).append(msg)
            # 截取消息  保留最大5条记录
            msgs[puid] = msg[puid][-5:]


# 使机器人后台运行，并进入交互模式
wxpy.embed()
