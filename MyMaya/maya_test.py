# -*- encoding: utf-8 -*-
"""
@File           : test.py
@Time           : 2019/11/22 16:21
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import time
import maya


def main():
    a = maya.now()
    print(a)
    print(a.iso8601())
    print(a.slang_date())
    print(a.slang_time())
    print(a.day)
    print(a.month)
    print(a.year)
    print(a.epoch)
    print(a.rfc2822())
    print(a.rfc3339())
    print(a.datetime())
    print(a.hour, a.minute, a.second, a.microsecond)

    tm = '2019-11-22 16:37:45.423992+00:00'
    print(maya.parse(tm).datetime())
    print(maya.parse(tm).datetime(to_timezone='US/Eastern', naive=True))
    print(maya.parse(tm).datetime(to_timezone='ASIA/Shanghai', naive=True))

    b = maya.get_localzone()
    print(b)

    # rand_day = maya.when('2011-02-07', timezone='US/Eastern')
    # print(rand_day)

    rand_day = maya.when('2019-11-22', timezone='ASIA/Shanghai')
    print(rand_day)
    print(rand_day.day, rand_day.month, rand_day.year)

    from datetime import datetime
    d = maya.MayaDT.from_datetime(datetime.utcnow())
    print(d)

    import time
    e = maya.MayaDT.from_struct(time.gmtime())
    print(e)
    f = maya.MayaDT(time.time())
    print(f)

    # tomorrow = maya.when('tomorrow')
    # print(tomorrow)
    # print(tomorrow.slang_date())
    # print(tomorrow.slang_time())
    # print(tomorrow.iso8601())


if __name__ == '__main__':
    main()
