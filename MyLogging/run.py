# -*- encoding: utf-8 -*-
"""
@File           : run.py
@Time           : 2019/11/22 13:59
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import time
import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from MyLogging.setting import *


# 日志实例
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s: %(message)s')

# log_file_name = 'test_log_{}.log'.format(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
log_file_name = 'test_'
# timeRotateHandler = TimedRotatingFileHandler(filename=LOG_PATH.rstrip('/').rstrip('\\') + "/{}_".format(log_file_name),
#                                              when="D", interval=1, backupCount=30, encoding='utf-8')
timeRotateHandler = TimedRotatingFileHandler(filename=log_file_name, when="midnight", interval=1, backupCount=3, encoding='utf-8')
# timeRotateHandler.suffix = "%Y-%m-%d %H-%M-%S.log"
timeRotateHandler.suffix = "%Y-%m-%d.log"
timeRotateHandler.setLevel(logging.INFO)
timeRotateHandler.setFormatter(formatter)

logger.addHandler(timeRotateHandler)


def main():
    while True:
        print('开始 {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        logger.info('=====================================开始=====================================')
        logger.info('123456789')
        logger.debug('123456789')
        logger.error('123456789')
        logger.critical('123456789')
        logger.warning('123456789')
        logger.info('=====================================结束=====================================\r\n')
        print('结束 {}\r\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        time.sleep(60*60)


if __name__ == '__main__':
    main()

