# Filename: myqueue.py

import os
import multiprocessing
import time

def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.time())
    queue.put(info)

def outputQ(queue,lock):
    info = queue.get()
    lock.acquire()
    print(str(os.getpid()) + '(get):' + info)
    lock.release()

record1 = []
record2 = []
lock = multiprocessing.Lock()
queue = multiprocessing.Queue(3)

for i in range(10):
    process = multiprocessing.Process(target=inputQ,args=(queue,))
    process.start()
    record1.append(process)

for i in range(10):
    process = multiprocessing.Process(target=outputQ,args=(queue,lock))
    process.start()
    record2.append(process)

for p in record1:
    p.join()

for p in record2:
    p.join()
