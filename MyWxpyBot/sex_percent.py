# -*- coding:utf-8 -*-

from wxpy import *
from pyecharts import Pie
import webbrowser

# 定义一个机器人
bot = Bot(cache_path=True)
# 获取更新好友列表
friends = bot.friends(update=False)
male = female = other = 0

# 在好友列表中排出自己
for i in friends[1::]:
    sex = i.sex
    if sex == 1:  # 等于1代表男性
        male += 1
    elif sex == 2:  #等于2代表女性
        female += 1
    else:
        other += 1

# 计算总数
total = len(friends[1::])

# 分析
attr = ['男性', '女性', '其他']
v1 = [float(male), float(female), float(other)]

pie = Pie("饼图-圆环图示例", title_pos='center')
pie.add("", attr, v1, radius=[40,75], label_text_color=None, is_label_show=True,legend_orient='vertical', legend_pos='left')
pie.render("sex_percent.html")

webbrowser.open("sex_percent.html")
