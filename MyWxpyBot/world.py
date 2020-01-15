# -*- coding: utf-8 -*-

from wxpy import *
from pyecharts import Map

values = [95.1, 23.2, 43.3, 66.4, 88.5]
attrs= ["China", "Canada", "Brazil", "Russia", "United States"]
map = Map("世界地图示例", width=1200, height=600)
map.add("", attrs, values, maptype="world", is_visualmap=True, visual_text_color='#000')
map.render('world.html')