# -*- encoding: utf-8 -*-
"""
@File           : test5.py
@Time           : 2019/12/28 14:48
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
from pytz import utc
from pymongo import MongoClient
# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from MyAPScheduler.helper import *

exec_time = {
    'hour': 14,
    'minute': 33,
    'second': 50
}

host = '127.0.0.1'
port = 27017
client = MongoClient(host, port)


# 配置作业存储器
jobstores = {
    'mongo': MongoDBJobStore(collection='job', database='test', client=client),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite'),
    # 'default': MemoryJobStore()
}

# 配置执行器，并设置线程数
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
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


def main():
    scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
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
        scheduler.add_job(my_job, 'cron', hour='16-17', minute='*/3', args=['000'])

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
