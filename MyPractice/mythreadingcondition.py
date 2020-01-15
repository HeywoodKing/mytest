# Filename:mythreadingcondition.py
#-*- coding:utf-8 -*- 

import time, os
import threading  

class BoothThread(threading.Thread):

    def __init__(self, tid, cond):
        self.tid = tid 
        self.cond = cond 
        threading.Thread.__init__(self)
        # super(BoothThread,self).__init__()

    def run(self):
        self.cond.acquire()
        global num
        num += 1
        if num <= 10:
            self.cond.wait()
            print self.tid, 'drink beer'
        elif num == 11:
            self.cond.notify_all() 

        self.cond.release()
 
# 主函数
if __name__ == '__main__':
    num = 0
    cond = threading.Condition()
    for tid in xrange(100):
        bt = BoothThread(tid, cond)
        bt.start()
