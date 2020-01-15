# Filename: mydatetime.py

import datetime

t = datetime.datetime(2015,12,27,9,16,30)
print(t)

t_next = datetime.datetime(2015,12,27,15,23,30)
print(t_next)

delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
delta3 = datetime.timedelta(days = 1)
delta4 = datetime.timedelta(hours = 2)
delta5 = datetime.timedelta(milliseconds = 1000)
delta6 = datetime.timedelta(microseconds = 1000)
print(t + delta1)
print(t + delta2)
print(t + delta3)
print(t + delta4)
print(t + delta5)
print(t + delta6)
print(t_next - t)
print(t > t_next)

format = "output_%Y-%m-%d-%H%M%S.txt"
str = "output_2015-12-27-090000.txt"
t = datetime.datetime.strptime(str,format)
t1 = t.strftime(format)
print(t)
print(t1)













