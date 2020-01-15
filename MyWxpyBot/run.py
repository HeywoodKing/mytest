# -*- coding: utf-8 -*-

from wxpy import *
import re



# friends = []
# groups =[]
# mps = []
# chats = []

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


# 登录成功之后获取所有好友和聊天群
def qr_func(uuid,status,qrcode):
    print('获取到二维码')

def login_func():
    print('登录成功')

def logout_func():
    print('退出登录')

"""
:param cache_path:
    * 设置当前会话的缓存路径，并开启缓存功能；为 `None` (默认) 则不开启缓存功能。
    * 开启缓存后可在短时间内避免重复扫码，缓存失效时会重新要求登陆。
    * 设为 `True` 时，使用默认的缓存路径 'wxpy.pkl'。
:param console_qr:
    * 在终端中显示登陆二维码，需要安装 pillow 模块 (`pip3 install pillow`)。
    * 可为整数(int)，表示二维码单元格的宽度，通常为 2 (当被设为 `True` 时，也将在内部当作 2)。
    * 也可为负数，表示以反色显示二维码，适用于浅底深字的命令行界面。
    * 例如: 在大部分 Linux 系统中可设为 `True` 或 2，而在 macOS Terminal 的默认白底配色中，应设为 -2。
:param qr_path: 保存二维码的路径
:param qr_callback: 获得二维码后的回调，可以用来定义二维码的处理方式，接收参数: uuid, status, qrcode
:param login_callback: 登陆成功后的回调，若不指定，将进行清屏操作，并删除二维码文件
:param logout_callback: 登出时的回调
"""
# 初始化机器人，扫码登录
# bot = Bot(cache_path=True, qr_path='/wxpy_bot/', qr_callback=qr_func, login_callback=login_func, logout_callback=logout_func)

bot = Bot(cache_path=True)

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
# bot.enable_puid(path='wxpy_puid.pkl')


# 为 True 时，将自动消除手机端的新消息小红点提醒 (默认为 False)
# bot.auto_mark_as_read(True)

# # 在 Web 微信中把自己加为好友
# bot.self.add()
# bot.self.accept()

# 机器人账号自身
myself = bot.self



# 获取所有好友
def get_friends():
    global friends
    friends = bot.friends()

# # 遍历输出好友名称
# for friend in friends:
#     print(friend)

# 查找好友
# <Friend: 乙醚>
def search_friend(name):
    return bot.friends.search(name)[0]

# 获取所有聊天群
def get_groups():
    global groups
    groups = bot.groups()

# for group in groups:
#     print(group)

# 获取所有公众号
def get_mps():
    global mps
    mps = bot.mps()

# 获取所有聊天对象
def get_chats():
    global chats
    chats = bot.chats()

# 登出当前账号
def logout():
    bot.logout()


# 发送文本
def send_text(obj, msg):
    obj.send(msg)

# 发送图片 | 以动态的方式发送图片
def send_image(obj, msg, is_dynamic=False):
    if is_dynamic:
        obj.send('@img@' + msg)
    else:
        obj.send_image(msg)

# 发送视频
def send_video(obj, msg):
    obj.send_video(msg)

# 发送文件
def send_file(obj, msg):
    obj.send_file(msg)


# 获取所有类型的消息（好友消息、群聊、公众号，不包括任何自己发送的消息）
# 并将获得的消息打印到控制台
# @bot.register()
# def print_all_msg(msg):
#     print(msg)



# 发送消息
def send_msg(name, msg, t='T'):
    friend = bot.friends.search(name)[0]
    t = t.upper()
    if t == "T":
        send_text(friend, msg)
    elif t == "I":
        send_image(friend, msg)
    elif t == "V":
        send_video(friend, msg)
    else:  # t == "F":
        send_file(friend, msg)

# 给机器人自己发送消息
def send_self_msg(msg):
    bot.self.send(msg)

# 给机器人自己文件传输助手发送消息
def send_file_helper(msg):
    bot.file_helper.send(msg)



# 统一回复消息
# @bot.register()
# def reply_auto_msg(msg):
#     msg.reply('我正在忙呢，一会儿给你回复哦！');

@bot.register()
def handle_receive_msg(msg):
    '''
    监听消息
    :param msg:接收到的消息
    :return:
    '''
    # 原数据信息
    print(msg)  # ☀️太奥北区9 10楼☀️业主交流群 : 你撤回了一条消息 (Note)
    raw = msg.raw
    print(raw)
    '''
    {
        'MsgId': '5098181968702529210',
        'FromUserName': '@@6e7d5de77e858d7a8fa029e39294c851bf8fdc6c5243abd34b40f6749d239726',
        'ToUserName': '@f52bbbc8e53379b45fa07c753e1b44fc67032d77263e8cf62bd7da3392e775e4',
        'MsgType': 10002,
        'Content': '&lt;sysmsg type="revokemsg"&gt;&lt;revokemsg&gt;&lt;session&gt;5538097630@chatroom&lt;/session&gt;&lt;oldmsgid&gt;1096526481&lt;/oldmsgid&gt;&lt;msgid&gt;4241293912041778012&lt;/msgid&gt;&lt;replacemsg&gt;&lt;![CDATA[你撤回了一条消息]]&gt;&lt;/replacemsg&gt;&lt;/revokemsg&gt;&lt;/sysmsg&gt;',
        'Status': 4,
        'ImgStatus': 1,
        'CreateTime': 1544105858,
        'VoiceLength': 0,
        'PlayLength': 0,
        'FileName': '',
        'FileSize': '',
        'MediaId': '',
        'Url': '',
        'AppMsgType': 0,
        'StatusNotifyCode': 0,
        'StatusNotifyUserName': '',
        'RecommendInfo': {
            'UserName': '',
            'NickName': '',
            'QQNum': 0,
            'Province': '',
            'City': '',
            'Content': '',
            'Signature': '',
            'Alias': '',
            'Scene': 0,
            'VerifyFlag': 0,
            'AttrStatus': 0,
            'Sex': 0,
            'Ticket': '',
            'OpCode': 0
        },
        'ForwardFlag': 0,
        'AppInfo': {
            'AppID': '',
            'Type': 0
        },
        'HasProductId': 0,
        'Ticket': '',
        'ImgHeight': 0,
        'ImgWidth': 0,
        'SubMsgType': 0,
        'NewMsgId': 5098181968702529210,
        'OriContent': '',
        'EncryFileName': '',
        'ActualUserName': '@f52bbbc8e53379b45fa07c753e1b44fc67032d77263e8cf62bd7da3392e775e4',
        'ActualNickName': 'Yuki3.14',
        'isAt': False,
        'Type': 'Note',
        'Text': '你撤回了一条消息'
    }
    '''

    print(raw.get('Status'))   #4

    # 如果消息的状态码是4  即撤回消息
    if raw.get('Status') == 4:
        # 如果是群消息
        if isinstance(msg.chat, bot.chats.group.Group):
            # 获取群成员的puid
            puid = msg.member.puid
            # 获取发送者的昵称
            name = msg.member.nick_name
        # 如果是好友消息
        elif isinstance(msg.chat, bot.chats.friend.Friend):
            # 获取好友的puid
            puid = msg.chat.puid
            # 获取好友的昵称
            name = msg.chat.nick_name
        else:
            puid = None
            name = None

        if puid:
            # 被撤回消息的msgid的匹配规则
            msg_id_regex = re.compile('<msgid>(\d+)</msgid>')

            # 获取被撤回消息的msgid
            old_msg_id = msg_id_regex.findall(raw.get('Content'))[0]
            # 获取该发送者的最后5次的消息记录
            chat_msgs = msgs.get(puid)
            # 遍历消息记录
            for chat_msg in chat_msgs[::-1]:
                # 跳过不是被撤回的信息
                if str(chat_msg.id) != old_msg_id:
                    continue
                chat = chat_msg.chat
                # 如果被撤回的信息是文本信息
                if chat_msg.type == "Text":
                    # 如果消息长度过长 则不予处理
                    if len(chat_msg.text) >= 150:
                        warning = "【您撤回的消息过长，有炸群嫌疑，不予处理！！！】"
                        bot.file_helper.send('%s撤回了一条文本消息--【%s】'.decode('utf-8') % (name, warning))
                        break
                    # 将此消息转发出来
                    chat_msg.forward(chat, prefix='%s撤回了一条文本消息，消息内容为：'.decode('utf-8') % name)
                # 如果被撤回的是位置信息
                elif chat_msg.type == "Map":
                    # 位置信息的匹配规则
                    map_regex = re.compile(r'label="(.+?)"')
                    # 获取位置信息中的位置
                    map = map_regex.findall(chat_msg.raw.get("OriContent"))[0]
                    # 将位置信息发出来
                    msg.reply('%s撤回了一条位置消息，位置信息为：【%s】'.decode('utf-8') % (name, map))
                else:
                    # 获取信息的类型
                    msg_type = msg_types.get(chat_msg.type).decode('utf-8')
                    # 将信息转发出来
                    chat_msg.forward(chat, prefix='%s撤回了一条%s消息， 消息内容为：'.decode('utf-8') % (name, msg_type))
                break
    # 如果消息的状态码是别的
    else:
        # 如果是群消息
        if isinstance(msg.chat, bot.chats.group.Group):
            # 获取群成员的puid
            puid = msg.member.puid
        # 如果是好友消息
        elif isinstance(msg.chat, bot.chats.friend.Friend):
            # 获取好友的puid
            puid = msg.member.puid
        else:
            puid = None

        if puid:
            # 记录消息
            msgs.setdefault(puid, []).append(msg)
            # 截取消息 保留最大5条记录
            msgs[puid] = msg[puid][-5:]






# # 监控回复 某个对象my_friend 发送的消息
# @bot.register(my_friend)
# def reply_my_friend_msg(msg):
#     return 'received: {} ({})'.format(msg.text, msg.type)


# 监控回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
@bot.register(bot.self, except_self=False)
def reply_self_msg(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 给指定对象回复消息



# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我已通过，你自己看着办吧！')


#自动添加好友的条件
add_friend_request = "加好友"

# 注册好友请求类消息
@bot.register(msg_types=FRIENDS, enabled=True)
# 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    if add_friend_request in msg.text.lower():
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        # 向新的好友发送消息
        new_friend.send('哈哈，我已通过，你自己看着办吧！')


admin_puids = frozenset(['XX', 'YY'])   #不可变集合
admins = list(map(lambda x: bot.friends().search(puid=x), admin_puids))

def invite(user):
    # sorted用于排序，lambda x:x.name用于群名排序
    groups = sorted(bot.groups(update=True).search(group_name), key=lambda x: x.name)

    if len(groups) > 0:
        for group in groups:
            if group.members == 500:
                continue
            if user in group:
                content = "您已经加入了{} [微笑]".format(group.nick_name)  # 经过format格式化的内容传递到{}
                user.send(content)
            else:
                group.add_members(user, use_invitation=True)
            return
        else:
            next_topic = group_tmpl.format(re.search(r'\d+', s).group() + 1)  # 当前群的名字后面+1
            new_group = bot.create_group(admins, topic=next_topic)
            # 以上3句代码的解释为：利用for if else语句进行判断，如果从查找的群名
            # 里面找不到对应的群就自动创建一个新群并添加进去
    else:
        print('Invite Failed')



# 打印出所有群聊中@自己的文本消息，并自动回复相同内容
# 这条注册消息是我们构建群聊机器人的基础
@bot.register(Group, TEXT)
def print_group_msg(msg):
    if msg.is_at:
        print(msg)
        msg.reply("@" + msg.text)




if __name__ == '__main__':
    # friends = get_friends()
    # groups = get_groups()
    # mps = get_mps()
    # chats = get_chats()
    # send_self_msg('快睡觉吧！')
    # send_msg('徐琦', '上班了，迟到了！')
    pass


# 在程序末尾（或其他你想要暂停调试的地方）加上embed()方法就可以让程序保持运行

# 使机器人后台运行，并进入交互模式
embed()



# # 初始化图灵机器人
# tuling = Tuling(api_key='')
#
# @bot.register(msg_types=TEXT)
# def reply_auto_all(msg):
#     tuling.do_reply(msg)
#
# # 开始运行
# bot.join()


