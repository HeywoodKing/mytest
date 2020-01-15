# Filename:mythreadingoop.py
# coding:gbk
# A program to simulate selling tickets in multi-thread way
# Written by Ching


import threading
import time
import os
import random

# ������������������ļ����
def doChore():
    time.sleep(0.5)

def printTicket(num):
    print("remain ticket:",num)

# ��һ���̴߳�����
# �Լ�������һ����BoothThread, �����̳���thread.Threading��
class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid = tid
        self.monitor = monitor
        threading.Thread.__init__(self)

    def run(self):
        while True:
            monitor['lock'].acquire()  # �������ߵȴ������߳��ͷ�����������ȴ������߳����ڳ�����
            if monitor['tick'] != 0:
                monitor['tick'] = monitor['tick'] - 1  # �۳�һ��Ʊ
                print(self.tid, ':now left:', "Z" + str(int(random.random() * 1000)))  # ��ӡ���۳��ĳ�Ʊ monitor['tick']
                doChore()  # �����ؼ�ҵ��
                printTicket(monitor['tick'])
            else:
                print("Thread_id", self.tid, "No more tickets")  # ��ӡû��Ʊ��
                os._exit(0)  # ȫ���߳������˳�
            monitor['lock'].release()  # �ͷ���
            doChore()  # �ǹؼ�ҵ��
            

# Start of the main function ������
monitor = {'tick':100, 'lock':threading.Lock()}  # ���߳�����

# ����10���߳�
for k in range(10):
    new_thread = BoothThread(k, monitor)  # ���߳�����Ŀ�꺯��
    new_thread.start()  # ��ʼ�����߳�
