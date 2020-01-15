# Filename:mythreadingcondition2_oop.py

import threading,os,time

def doChore():

        time.sleep(0.5)

class WorkThread(threading.Thread):

        def __init__(self,id,monitor):

                self.id=id

                self.monitor=monitor

                threading.Thread.__init__(self)

        def run(self):

                monitor['cont'].acquire()

                monitor['num']=monitor['num']+1

                if(monitor['num']<=10):

                        monitor['cont'].wait()

                        print('drink beer')

                        doChore()

                elif(monitor['num']==11):

                        monitor['cont'].notify_all()

                monitor['cont'].release()

                doChore()

 

 

 

monitor={'num':0,'cont':threading.Condition()}

for i in range(100):

        workThread=WorkThread(i,monitor)

        workThread.start()
