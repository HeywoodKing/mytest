# -*- coding: utf-8 -*-


import time
import datetime
import pandas as pd


# datetime对象时间
q = pd.datetime(2018, 1, 1)
p = pd.datetime.today()
print('对象时间', q, p)


# strftime将对象时间转换成字符串时间
qstr = q.strftime("%Y-%m-%d %H:%M:%S")
pstr = p.strftime("%Y-%m-%d %H:%M:%S")
print('字符串时间', qstr, pstr)


# strptime将字符串时间转换成tuple时间
qtup = time.strptime(qstr, "%Y-%m-%d %H:%M:%S")
ptup = time.strptime(pstr, "%Y-%m-%d %H:%M:%S")
print('字符串时间转元组时间', qtup, ptup)


# 将对象时间转换成tuple时间
qtup2 = pd.datetime.timetuple(q)
ptup2 = pd.datetime.timetuple(p)
print('对象时间转元组时间', qtup2, ptup2)


# 将tuple时间转换成时间戳
qstamp = time.mktime(qtup)
pstamp = time.mktime(ptup)
print('元组时间转时间戳', qstamp, pstamp)


# 计算时间间隔
# 60 * 60 = 3600s 一个小时，* 24 = 一天
ndays = int((pstamp - qstamp) / (3600*24))
print(qstr, pstr, '相差：', str(ndays) + '天')



