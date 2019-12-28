# -*- encoding: utf-8 -*-
"""
@File           : test2.py
@Time           : 2019/12/28 14:03
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def my_job(text):
    print('job1', datetime.datetime.now(), text)


def my_job2(text):
    print('job2', datetime.datetime.now(), text)


def my_job3(text):
    print('job3', datetime.datetime.now(), text)


def my_job4(text):
    print('job4', datetime.datetime.now(), text)


def main():
    scheduler = BlockingScheduler()
    """
    间隔调度，参数如下：
    weeks (int) – 间隔几周 
    days (int) – 间隔几天 
    hours (int) – 间隔几小时 
    minutes (int) – 间隔几分钟 
    seconds (int) – 间隔多少秒 
    start_date (datetime|str) – 开始日期 
    end_date (datetime|str) – 结束日期 
    timezone (datetime.tzinfo|str) – 时区
    """
    # 每隔5秒执行一次
    scheduler.add_job(my_job, 'interval', seconds=5, args=['5 second'], id='job1')
    # 每隔5分钟执行一次
    scheduler.add_job(my_job2, 'interval', minutes=5, args=['5 minute'], id='job2')
    # 每隔5小时执行一次
    scheduler.add_job(my_job3, 'interval', hours=5, args=['5 hour'], id='job3')
    # 每隔5天执行一次
    scheduler.add_job(my_job4, 'interval', days=5, args=['5 day'], id='job4')

    scheduler.start()


if __name__ == '__main__':
    main()
