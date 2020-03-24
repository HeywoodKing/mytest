# -*- encoding: utf-8 -*-
"""
@File           : db_api.py
@Time           : 2019/12/28 13:40
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
from datetime import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler


def my_job(text):
    print('my_job', datetime.now(), text)


def main():
    scheduler = BlockingScheduler()

    # 只执行一次 2019-12-28 时刻运行一次
    scheduler.add_job(my_job, 'date', run_date=date(2017, 12, 28), args=['text'], id='job2')

    # # 只执行一次 2019-12-28 13:52:10
    # scheduler.add_job(my_job, 'date', run_date=datetime(2019, 12, 28, 13, 52, 10), args=['text'], id='job2')
    #
    # # 只执行一次 2019-12-28 13:52:10
    # scheduler.add_job(my_job, 'date', run_date='2019-12-28 13:52:10', args=['text'], id='job2')

    scheduler.start()


if __name__ == '__main__':
    main()

