#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-29 17:41:12
# @Author  : Flack (flackmaster@163.com)
# @Link    : http://www.cnblogs.com/ching126/
# @Version : $Id$


import match
import os
import datetime
import json

def writeToTxt(list_name, file_path):
    try:
        # 这里直接write item 即可，不要自己给序列化在写入，会导致json格式不正确的问题
        fp = open(file_path, "w+", encoding='utf-8')
        l = len(list_name)
        i = 0
        fp.write('[')
        for item in list_name:
            print(item)
            fp.write(str(item))
            if i < l - 1:
                fp.write(',\n')
            i += 1
        fp.write(']')
        fp.close()
    except IOError:
        print("fail to open file")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def saveBlogs(index):
    if is_number(index):
        if index >= 1:
            index += 1
        else:
            index = 2
    else:
        index = 2
    for i in range(1, index):
        print('request for ' + str(i) + '...')
        blogs = match.blogParser(i)
        #保存到文件
        path = createFile()
        print(path)
        writeToTxt(blogs, path + '/blog_' + str(i) + '.json')
        print('第' + str(i) + '页已经完成')

    return 'success'


def createFile():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    path = '/' + date
    if os.path.exists(path):
        return path
    else:
        os.mkdir(path)
        return path


result = saveBlogs(1)
print(result)

