# Filename:mythreading.py
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

# ��ÿһ���߳�Ҫ����ĺ���
def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()  # �������ߵȴ������߳��ͷ�����������ȴ������߳����ڳ�����
        if i != 0:
            i = i - 1  # �۳�һ��Ʊ
            print(tid,':now left:', "Z" + str(int(random.random() * 1000)))  # ��ӡ���۳��ĳ�Ʊ
            # doChore()  # �����ؼ�ҵ��
            printTicket(i)
        else:
            print("Thread_id",tid,"No more ticket")  # ��ӡû��Ʊ��
            os._exit(0)  # ȫ���߳������˳�
        lock.release()  # �ͷ���
        doChore()  # �ǹؼ�ҵ��

# Start of the main function ������
i = 100  # Ʊ������
lock = threading.Lock()  # ���߳�����

# ����10���߳�
for k in range(10):
    new_thread = threading.Thread(target=booth,args=(k,))  # ���߳�����Ŀ�꺯��
    new_thread.start()  # ��ʼ�����߳�
