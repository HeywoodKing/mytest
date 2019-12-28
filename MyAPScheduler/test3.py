# -*- encoding: utf-8 -*-
"""
@File           : test3.py
@Time           : 2019/12/28 14:06
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from MyAPScheduler.helper import *

scheduler = BlockingScheduler()

"""
参数如下：
year (int|str) – 年，4位数字 
month (int|str) – 月 (范围1-12) 
day (int|str) – 日 (范围1-31) 
week (int|str) – 周 (范围1-53) 
day_of_week (int|str) – 周内第几天或者星期几 (范围0-6 或者 mon,tue,wed,thu,fri,sat,sun) 
hour (int|str) – 时 (范围0-23) 
minute (int|str) – 分 (范围0-59) 
second (int|str) – 秒 (范围0-59) 
start_date (datetime|str) – 最早开始日期(包含) 
end_date (datetime|str) – 最晚结束时间(包含) 
timezone (datetime.tzinfo|str) – 指定时区
"""

exec_time = {
    'hour': 14,
    'minute': 33,
    'second': 50
}


# my_job每天14点33分50秒执行一次
@scheduler.scheduled_job(
    'cron', day_of_week='*',
    hour=exec_time['hour'], minute=exec_time['minute'], second=exec_time['second'], args=['123456']
)
def my_job1(text):
    print('my_job1', datetime.datetime.now(), text)
    write_log('定时任务1执行成功！')


# my_job将会在6,7,8,11,12月的第3个周五的1,2,3点运行
@scheduler.scheduled_job('cron', month='6-8,11-12', day='3rd fri', hour='0-3', args=['123456'])
def my_job2(text):
    print('my_job2', datetime.datetime.now(), text)
    write_log('定时任务2执行成功！')


# 截止到2016-12-30 00:00:00，每周一到周五早上五点半运行my_job
@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2016-12-31', args=['123456'])
def my_job3(text):
    print('my_job3', datetime.datetime.now(), text)
    write_log('定时任务3执行成功！')


# 在每年 1-3、7-9 月份中的每个星期一、二中的 00:00, 01:00, 02:00 和 03:00 执行 my_job4 任务
# scheduler.add_job(job_func, 'cron', month='1-3,7-9',day='0, tue', hour='0-3')
@scheduler.scheduled_job('cron', month='1-3,7-9', day='0, tue', hour='0-3', args=['123456'])
def my_job4(text):
    print('my_job4', datetime.datetime.now(), text)
    write_log('定时任务3执行成功！')


def main():
    try:
        print('定时任务已启动，执行时间：{}:{}:{}'.format(exec_time['hour'], exec_time['minute'], exec_time['second']))
        scheduler.start()
    except Exception as ex:
        scheduler.shutdown()
        write_log('定时任务执行失败！')
        print(ex)


if __name__ == '__main__':
    main()
