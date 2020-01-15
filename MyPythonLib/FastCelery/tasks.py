# -*- coding: utf-8 -*-


from __future__ import absolute_import
from FastCelery.celery import app
import time
from datetime import datetime


# 启动分布式服务
# celery -A <mymodule> worker -l info

# 为了解决win10 报错，
# Task handler raised error: ValueError('not enough values to unpack (expected 3, got 0)')
# 安装eventlet 并且启动的时候增加-P eventlet
# celery -A <mymodule> worker -l info -P eventlet


@app.task()
def add(x, y):
    return x + y


@app.task()
def minus(x, y):
    return x - y


@app.task()
def multi(x, y):
    return x * y


@app.task()
def divide(x, y):
    return x / y


@app.task()
def notice(msg):
    # return datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '>>' + msg
    return msg
