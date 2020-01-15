# -*- coding: utf-8 -*-


from celery import Celery

broker = 'redis://192.168.99.100:6379/0'
backend = 'redis://192.168.99.100:6379/1'

app = Celery('8_celery_task', broker=broker, backend=backend)


@app.task()
# 任务函数
def add(x, y):
    return x + y



