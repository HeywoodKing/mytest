# -*- coding: utf-8 -*-

from __future__ import absolute_import
from datetime import timedelta
from celery.schedules import crontab
from kombu import Queue, Exchange
# from FastCelery import tasks


# CELERY_IMPORTS = ['FastCelery.tasks',]
# CELERY_IGNORE_RESULT = False
# BROKER_HOST = '192.168.99.100'
# BROKER_PORT = 5672
# redis
BROKER_URL = 'redis://192.168.99.100:6379/0'
# rabbitmq
# BROKER_URL = 'amqp://guest:guest@192.168.99.100:15672'

# 存储结果
CELERY_RESULT_BACKEND = 'redis://192.168.99.100:6379/1'
# CELERY_RESULT_BACKEND = 'db+mysql://root:123456@192.168.99.100:3306/celery'

# CELERY_RESULT_BACKEND = 'mongodb'
# CELERY_RESULT_BACKEND_SETTINGS = {
#     'host': '192.168.99.100',
#     'port': 27017,
#     'database': 'jobs',
#     'taskmeta_collection': 'stock_taskmeta_collection',
# }


# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60*60*24
# CELERY_ACCEPT_CONTENT = ['json']
CELERY_MAX_TASKS_PER_CHILD = 40
# celery worker amount
# CELERYD_CONCURRENCY = 8
# the amount that a celery worker get task from broker each time
CELERY_PREFETCH_MULTIPLIER = 4
# CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('for_task_add', Exchange('for_task_add'), routing_key='task_add'),
    Queue('for_task_minus', Exchange('for_task_minus'), routing_key='task_minus'),
    Queue('for_task_multi', Exchange('for_task_multi'), routing_key='task_multi'),
    Queue('for_task_divide', Exchange('for_task_divide'), routing_key='task_divide'),
)

CELERY_ROUTES = {
    'FastCelery.tasks.add': {'queue': 'for_task_add', 'routing_key': 'task_add'},
    'FastCelery.tasks.minus': {'queue': 'for_task_minus', 'routing_key': 'task_minus'},
    'FastCelery.tasks.multi': {'queue': 'for_task_multi', 'routing_key': 'task_multi'},
    'FastCelery.tasks.divide': {'queue': 'for_task_divide', 'routing_key': 'task_divide'},
}

CELERYBEAT_SCHEDULE = {
    # 表示每隔30秒执行 add 函数。一旦使用了 scheduler, 启动 celery需要加上-B 参数
    'add_scheduler': {
        'task': 'FastCelery.tasks.add',
        'schedule': timedelta(seconds=30),  # 每隔30秒执行
        'args': (16, 20),
    },
    'add_scheduler_monday_morning': {
        'task': 'FastCelery.tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),  # 每周一早晨7:30分执行
        'args': (16, 16),
    },
    'minus_scheduler': {
        'task': 'FastCelery.tasks.minus',
        'schedule': timedelta(seconds=60*60*3),  # 每隔3小时执行
        'args': (10, 5),
    },
    'notice_scheduler': {
        'task': 'FastCelery.tasks.notice',
        'schedule': timedelta(seconds=10),  # 每天执行一次
        # 'schedule': timedelta(days=1),  # 每天执行一次
        'args': ('定时通知：广大旅客注意啦，Celery上线了，需要抢购了昂！！！', ),
    },
}


