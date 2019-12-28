# -*- encoding: utf-8 -*-
"""
@File           : test6.py
@Time           : 2019/12/28 14:48
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
from pytz import utc
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from MyAPScheduler.helper import *

exec_time = {
    'hour': 14,
    'minute': 33,
    'second': 50
}

host = '127.0.0.1'
port = 27017
client = MongoClient(host, port)

# # 配置作业存储器
# jobstores = {
#     'mongo': MongoDBJobStore(collection='job', database='test', client=client),
#     'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite'),
#     # 'default': MemoryJobStore()
# }
#
# # 配置执行器，并设置线程数
# executors = {
#     'default': ThreadPoolExecutor(20),
#     'processpool': ProcessPoolExecutor(5)
# }
#
# job_defaults = {
#     'coalesce': False,  # 默认情况下关闭新的作业
#     'max_instances': 3  # 设置调度程序将同时运行的特定作业的最大实例数3
# }


# 配置作业存储器
jobstores = {
    # 'mongo': {'type': 'mongodb'},
    # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    'default': MemoryJobStore()
}

# 配置执行器，并设置线程数
executors = {
    'default': {'type': 'threadpool', 'max_workers': 20},
    'processpool': ProcessPoolExecutor(max_workers=5)
}

job_defaults = {
    'coalesce': False,  # 默认情况下关闭新的作业
    'max_instances': 3  # 设置调度程序将同时运行的特定作业的最大实例数3
}


def my_job(text):
    print('+' * 100)
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
    print('my_job', datetime.datetime.now(), text)
    write_log('定时任务执行成功！')
    print('+' * 100)


def my_listener(event):
    if event.exception:
        print('任务出错了！！！！！！')
    else:
        print('任务照常运行...')


def main():
    # scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
    # scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
    scheduler = BackgroundScheduler({
        'apscheduler.jobstores.mongo': {
            'type': 'mongodb'
        },
        'apscheduler.jobstores.default': {
            'type': 'sqlalchemy',
            'url': 'sqlite:///jobs.sqlite'
        },
        'apscheduler.executors.default': {
            'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
            'max_workers': '20'
        },
        'apscheduler.executors.processpool': {
            'type': 'processpool',
            'max_workers': '5'
        },
        'apscheduler.job_defaults.coalesce': 'false',
        'apscheduler.job_defaults.max_instances': '3',
        'apscheduler.timezone': 'UTC',
    })

    try:
        print('定时任务已启动')
        # print('定时任务已启动，执行时间：{}:{}:{}'.format(exec_time['hour'], exec_time['minute'], exec_time['second']))
        # scheduler.add_job(my_job, 'interval', seconds=5, args=['123456'])

        """
        hour =19 , minute =23
        hour ='19', minute ='23'
        minute = '*/3' 表示每 5 分钟执行一次
        hour ='19-21', minute= '23' 表示 19:23、 20:23、 21:23 各执行一次任务
        """
        scheduler.add_job(my_job, 'cron', hour='16-17', minute='*/3', args=['000'], replace_existing=True,
                          misfire_grace_time=30, coalesce=True)

        # scheduler.add_job(my_job, args=['job_once_now', ], id='job_once_now'replace_existing=True)
        # scheduler.add_job(my_job, trigger='date', run_date='2018-04-05 07:48:05', args=['job_date_once', ],
        #                   id='job_date_once', replace_existing=True)
        # scheduler.add_job(my_job, trigger='interval', seconds=5, args=['job_interval', ], id='job_interval',
        #                   replace_existing=True)
        # scheduler.add_job(my_job, trigger='cron', month='4-8,11-12', hour='7-11', second='*/10', end_date='2018-05-30',
        #                   args=['job_cron', ], id='job_cron', replace_existing=True)

        scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

        # 获取所有作业
        # jobs = scheduler.get_jobs()
        # print(jobs)

        scheduler.start()
    except Exception as ex:
        scheduler.shutdown()
        client.close()
        write_log('定时任务执行失败！')
        print(ex)


if __name__ == '__main__':
    main()
