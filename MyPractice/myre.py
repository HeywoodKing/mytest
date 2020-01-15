# Filename:myre.py
# coding:utf8

import re
m = re.search('[0-9]','abc5d4e19f')
print(m.group(0))

#m = re.match('[0-9]','abdc4ef')
#print(m.group())

m = re.search("output_(\d{4})","output_1986.txt")
print(m.group())

m = re.search("output_(?P<year>\d{4})","output_1986.txt")
print(m.group("year"))

# 有一个文件，文件名为output_1981.10.21.txt 。
# 下面使用Python： 读取文件名中的日期时间信息，并找出这一天是周几。
# 将文件改名为output_YYYY-MM-DD-W.txt (YYYY:四位的年，MM：两位的月份，
# DD：两位的日，W：一位的周几，并假设周一为一周第一天)

# f = open("output_1981.10.21.txt","r");

fn = "output_1981.10.21.txt";

res = re.search('output_(?P<dt>[1-9]\d{3}\.\d{2}\.\d{2}\.txt)',fn);
print(res.group())


res2 = re.match('output_(?P<dt>[1-9]\d{3}\.\d{2}\.\d{2}\.txt)',fn);
print("原始：" + res2.group())

import time,datetime
res3 = re.sub('output_(?P<dt>[1-9]\d{3}\.\d{2}\.\d{2}\.txt)', "output_" + time.strftime("%Y-%m-%d %H-%M-%a") + ".txt",fn);
print("替换后：" + res3)

print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y-%m-%d %H:%M"))
print(datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:%S"))
print(str(datetime.datetime.now()))
print(str(datetime.datetime.now())[:])
print(str(datetime.datetime.now())[:22])
