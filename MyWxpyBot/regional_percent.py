# -*- coding: utf-8 -*-

# 全球国家地图: echarts - countries - pypkg(1.9
# MB): 世界地图和
# 213
# 个国家，包括中国地图
# 中国省级地图: echarts - china - provinces - pypkg(730
# KB)：23
# 个省，5
# 个自治区
# 中国市级地图: echarts - china - cities - pypkg(3.8
# MB)：370
# 个中国城市
# 中国县区级地图: echarts - china - counties - pypkg(4.1
# MB)：2882
# 个中国县·区
# 中国区域地图: echarts - china - misc - pypkg(148
# KB)：11
# 个中国区域地图，比如华南、华北。
#
# 特别注明，中国地图在
# echarts - countries - pypkg
# 里。需要这些地图的朋友，可以装
# pip
# 命令行
# 需要安装一下第三方库
# pip3 install echarts-countries-pypkg
# pip3 install echarts-china-provinces-pypkg
# pip3 install echarts-china-cities-pypkg
# pip3 install echarts-china-counties-pypkg
# pip3 install echarts-china-misc-pypkg


from wxpy import *
from pyecharts import Map
import webbrowser

province_name = '甘肃'

b = '市'
def get_city_name(x):
    return x + b


bot = Bot(cache_path=True)
friends = bot.friends(update=False).search(province=province_name)
citys = []
for f in friends:
    city = f.city
    citys.append(city)

r = map(get_city_name, citys)

cityss = list(r)
# print(cityss)

# 计算城市数量
a = {}
for i in cityss:
    if i != '市':
        num = cityss.count(i)
        if isinstance(num, int):
            a[i] = num
        else:
            a[i] = 0


# a.pop('市')
# print(a)

#把字典进行有序拆分为2个列表
attrs = []
values = []
for attr,value in a.items():
    attrs.append(attr)
    values.append(value)

# 开会绘图
map = Map(province_name + '地图示例', width=1200, height=600)
if province_name != '中国':
    map.add("好友所在城市分布图", attrs, values, maptype=province_name, is_label_show=True, is_visualmap=True, visual_text_color='#000',is_more_utils=True)
else:
    map.add("好友分布图", attrs, values, maptype='china', visual_range=[0, 200], is_visualmap=True, visual_text_color="#fff", is_more_utils=True,symbol_size=10)

map.render('regional_percent.html')


friends_stat = bot.friends().stats()
# friends_loc = []
attrs = []
values = []
for province,count in friends_stat["province"].items():
    if province != "":
        attrs.append(province)
        values.append(count)

# print(attrs)
# print(values)

map = Map(province_name + '地图示例', width=1200, height=600)
map.add("好友分布图", attrs, values, maptype='china', visual_range=[0, 200], is_visualmap=True, visual_text_color="#fff", is_more_utils=True,symbol_size=10)

map.render('regional_percent2.html')

webbrowser.open('regional_percent2.html')

# # 对人数进行倒数排序
# friends_loc.sort(key=lambda x: x[1], reverse=True)
#
# for item in friends_loc:
#     print(item[0], item[1])


