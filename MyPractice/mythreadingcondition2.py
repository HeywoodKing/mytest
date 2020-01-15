# Filename:mythreadingcondition2.py

import threading

import time

import os

def doCore():

        time.sleep(0.5)

def booth(tid):

        global i

        global cond

        cont.acquire()

        i+=1

        if(i<=10):

                cont.wait()

                print('drink beer')

                doCore()

        elif(i==11):

                cont.notify_all()

        cont.release()

 

i=0

cont=threading.Condition()

for k in range(100):

        new_thread=threading.Thread(target=booth,args=(k,))

        new_thread.start()
