# Filename: myos.py
# coding: gb2312

import os.path
import datetime
import time
path = "D:/Work/Python/test.txt"

print(os.path.basename(path))
print(os.path.dirname(path))

info = os.path.split(path)
print(info)

path2 = os.path.join("D:/Work/","Python/","test.txt")
print(path2)

p_list = [path,path2]
print("commonprefix:" + os.path.commonprefix(p_list))

path3 = os.path.normpath(path)
print("normpath:" + path3)


print("exists:" + str(os.path.exists(path)))

print("getsize:" + str(os.path.getsize(path)))
print("getatime:" + str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.path.getatime(path)))))
print("getmtime:" + str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.path.getmtime(path)))))

print("当前时间戳：" + str(time.time()))
print("当前日期：" + str(time.ctime()))

print("isfile:" + str(os.path.isfile(path)))
print("isdir:" + str(os.path.isdir(path)))










