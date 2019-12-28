# -*- encoding: utf-8 -*-
"""
@File           : test4.py
@Time           : 2019/12/28 14:48
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import time
from apscheduler.schedulers.background import BackgroundScheduler
from MyAPScheduler.helper import *

exec_time = {
    'hour': 14,
    'minute': 33,
    'second': 50
}


def my_job(text):
    print('+' * 100)
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
    print('my_job', datetime.datetime.now(), text)
    write_log('定时任务执行成功！')
    print('+' * 100)


def main():
    scheduler = BackgroundScheduler()
    try:
        # print('定时任务已启动，执行时间：{}:{}:{}'.format(exec_time['hour'], exec_time['minute'], exec_time['second']))
        # # 每隔5天执行一次
        # job = scheduler.add_job(my_job, 'interval', days=5, args=['5 day'], id='job')

        # 每隔5秒执行一次
        job = scheduler.add_job(my_job, 'interval', seconds=5, args=['5 second'], id='job')
        # job.remove()

        # 启动调度任务
        scheduler.start()
        # scheduler.remove_job([job_id])

        while True:
            print(time.time())
            time.sleep(5)
    except Exception as ex:
        scheduler.shutdown()
        write_log('定时任务执行失败！')
        print(ex)


if __name__ == '__main__':
    main()
