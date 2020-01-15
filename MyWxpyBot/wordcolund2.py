# -*- coding: utf-8 -*-

from wxpy import *
from pyecharts import WordCloud

name2 = ['天水', '秦皇岛', 'Amy Schumer', '丽江','贵阳',
        'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express','海南','江油',
        '成都', '天津', '平凉', '黑河','天水', '陇南', '厦门', '兰州','西安',
       '武汉','上海','广州','深圳','北京']
value2 = [10000, 6181, 562, 4055, 2467,
         789, 1898, 100, 1112,965,
         847, 582, 555, 550, 462,
         366, 360, 282, 273, 265,
        120,150,180,185,195]
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name2, value2, word_size_range=[20, 100])
wordcloud.render('wordcloud2.html')

print('生成成功')
