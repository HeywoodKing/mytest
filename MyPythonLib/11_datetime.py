# -*- coding: utf-8 -*-


from datetime import date, datetime

now = date.today()
now1 = datetime.now()
print(now, now1)
print(now1.strftime('%Y-%m-%d %H:%M:%S'))
