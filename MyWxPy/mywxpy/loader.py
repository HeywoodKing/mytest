# -*- encoding: utf-8 -*-
"""
@File           : loader.py
@Time           : 2019/11/20 17:14
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import time
import re
import wxpy
from MyWxPy.mywxpy.setting import *


class Loader(object):
    def __init__(self):
        # 初始化机器人，扫码登录
        # cache_path保持登录，Bot初始化中可以加入参数：console_qr是否在控制台显示二维码
        self.bot = None
        self.friends = []
        self.groups = []
        self.msgs = dict()
        # 信息的类型
        self.msg_types = {
            'Text': '文本',
            'Map': '位置',
            'Picture': '图片',
            'Video': '视频',
            'Attachment': '文件',
            'Sharing': '分享',
            'Card': '名片',
            'Recording': '语音',
            'Note': '提示'
        }

    def run(self):
        self.bot = wxpy.Bot(cache_path=True, console_qr=False)
        self.bot.messages.max_history = MAX_HISTORY
        self.bot.enable_puid('wxpy_puid.pkl')
        self.friends = self.bot.friends()
        self.groups = self.bot.groups()

        print('登录成功！')

        target_friend = self.friends.search(MONITOR_FRIEND_LIST)[0]
        # current_friend = self.friends.search(u'好友昵称', sex=FEMALE, city="好友信息中的城市")[0]
        print('监控对象：', target_friend)

        # todo
        # ====================================================================================
        # 找到好友列表中昵称为“我说”的好友，监控聊天，打印该好友发来的文本消息
        # @self.bot.register(chats=target_friend, except_self=False, msg_types=wxpy.TEXT)
        # def reply_friend(msg):
        #     print('header reply_friend:', msg)
        #     #  ['_get_chat_by_user_name', '_receive_time',
        #     #  'articles', 'bot', 'card', 'chat', 'create_time', 'file_name', 'file_size', 'forward', 'get_file', 'id',
        #     #  'img_height', 'img_width', 'is_at', 'latency', 'location', 'media_id', 'member', 'play_length', 'raw',
        #     #  'receive_time', 'receiver', 'reply', 'reply_file', 'reply_image', 'reply_msg', 'reply_raw_msg',
        #     #  'reply_video', 'sender', 'text', 'type', 'url', 'voice_length']
        #
        #     # print(msg.member, type(msg.sender))
        #     # target_friend.send('我已经截图了，哈哈，你撤回也么有用咯！' + msg.text)
        #     # target_friend.send_image('my_picture.png')
        #     # target_friend.send_video('my_video.mov')
        #     # target_friend.send_file('my_file.zip')
        #     # target_friend.send('@img@my_picture.png')
        #
        #     print('footer reply_friend:', msg)

        target_group = self.groups.search(MONITOR_GROUP_LIST)[0]
        print('监控群组：', target_group)

        # 监控群聊消息，打印群聊中的文本消息
        @self.bot.register(
            chats=target_group,
            msg_types=wxpy.TEXT or wxpy.PICTURE or wxpy.VIDEO or wxpy.MAP or wxpy.CARD or wxpy.SHARING or
                      wxpy.RECORDING or wxpy.ATTACHMENT or wxpy.NOTE
        )
        def reply_group(msg):
            print('header reply_group:', msg)
            # target_group.send('我已经截图了，哈哈，你撤回也么有用咯！' + msg.text)
            print('footer reply_group', msg)

        # 处理撤回消息
        @self.bot.register(except_self=False)
        def handle_receive_msg(msg):
            """
            监听消息
            :param msg: 接收到的消息
            :return:
            """
            try:
                # 原信息数据
                raw = msg.raw

                # raw.get('Status') == 3 个人消息
                # 如果消息的状态码是4  即撤回消息
                if raw.get('Status') == 4:
                    # 如果是群消息
                    if isinstance(msg.chat, wxpy.api.chats.group.Group):
                        # 获取群成员的puid
                        puid = msg.member.puid
                        # 获取发送者的昵称
                        name = msg.member.nick_name
                    # 如果是好友消息
                    elif isinstance(msg.chat, wxpy.api.chats.friend.Friend):
                        # 获取好友的puid
                        puid = msg.chat.puid
                        # 获取好友的昵称
                        name = msg.chat.nick_name

                        # # 获取发送者的puid
                        # puid = msg.sender.puid
                        # # 获取发送者的名称
                        # name = msg.sender.raw['UserName']
                    else:
                        puid = None
                        name = None

                    if puid:
                        # 被撤回消息的msgid的匹配规则
                        msg_id_regex = re.compile('<msgid>(\d+)</msgid>')

                        # 获取被撤回消息的msgid
                        msg_content = msg_id_regex.findall(raw.get('Content'))
                        if msg_content:
                            old_msg_id = msg_content[0]
                        else:
                            old_msg_id = None

                        # 获取该发送者的最后5次的消息记录
                        chat_msgs = self.msgs.get(puid)
                        print(chat_msgs)

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
                                    warning = "有人炸群咯！！！"
                                    self.bot.file_helper.send('%s %s' % (name, warning))
                                    break
                                # 将此消息转发出来
                                chat_msg.forward(chat, prefix='%s 已截图，哈哈哈，消息内容为：' % name)
    
                            # 如果被撤回的是位置信息
                            elif chat_msg.type == "Map":
                                # 位置信息的匹配规则
                                map_regex = re.compile(r'label="(.+?)"')
                                # 获取位置信息中的位置
                                map = map_regex.findall(chat_msg.raw.get("OriContent"))[0]
                                # 将位置信息发出来
                                msg.reply('%s 已经看到你的位置啦，啦啦啦，位置信息为：【%s】' % (name, map))
                            else:
                                # 获取信息的类型
                                # msg_type = self.msg_types.get(chat_msg.type).encode('utf-8')
                                msg_type = self.msg_types.get(chat_msg.type)
                                # 将信息转发出来
                                chat_msg.forward(chat, prefix='%s 怀孕了也不用怕，我们一起想办法！撤回了一条%s消息，消息内容为：' % (name, msg_type))
                            break
                else:
                    # 如果是群消息
                    if isinstance(msg.chat, wxpy.api.chats.group.Group):
                        # 获取群成员的puid
                        puid = msg.member.puid
                    # 如果是好友消息
                    elif isinstance(msg.chat, wxpy.api.chats.friend.Friend):
                        # 获取好友的puid
                        puid = msg.chat.puid
                    else:
                        puid = None

                    if puid:
                        # 记录消息
                        self.msgs.setdefault(puid, []).append(msg)
                        # 截取消息  保留最大5条记录
                        self.msgs[puid] = self.msgs[puid][-5:]

            except Exception as ex:
                print('error:{}'.format(ex))

        # # 机器人回复
        # @self.bot.register(msg_types=TEXT)
        # def tuling_reply_msg(msg):
        #     print(msg)
        #     sender_username = msg.sender.raw['UserName']
        #     # 输出发送信息的好友或者群聊中的人员信息
        #     print(sender_username)
        #     # 判断是否和我设置的想要自动恢复到人一致如果一致调用tuling进行消息回复
        #     if sender_username == target_friend.raw['UserName']:
        #         # 输出或得到的消息
        #         print(msg)
        #
        #         # # 调用tuling机器人回复消息，并将消息赋值给message
        #         # message = tuling.do_reply(msg)
        #         # # 输出回复消息的内容
        #         # print(message)

        # @self.bot.register()
        # def tuling_reply_msg(msg):
        #     """
        #     自动回复消息
        #     :param msg: 接收到的信息数据
        #     :return: 回复文本
        #     """
        #     # do_reply会自动回复消息并返回消息文本
        #     tu_ling.do_reply(msg)
        #     pass
        # ====================================================================================

        print('正在运行...')

        # 阻塞进程
        # self.bot.join()

        # 使机器人后台运行，并进入交互模式
        wxpy.embed()

    def logout(self):
        if self.bot:
            self.bot.logout()
        print('退出登录！')

    # 验证删除我的好友
    def vaild_del_my_friend(self):
        for friend in self.friends:
            print(friend)
            time.sleep(0.4)
            if friend != self.bot.self:
                friend.send('జ్ఞ ‌ా')


if __name__ == '__main__':
    loader = Loader()
    loader.run()
