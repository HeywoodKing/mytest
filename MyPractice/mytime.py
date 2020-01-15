# Filename: mytime.py

import time
print("Wall clock time:" + str(time.time()))
print("CPU time:" + str(time.clock()))

print('start')
time.sleep(1)
print('wake up')

st1 = time.gmtime()
print(st1)
st2 = time.localtime()
print(st2)
s = time.mktime(st1)
print(s)
