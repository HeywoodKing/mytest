# Filename:mythreadingoop.py
# coding:gbk
# A program to simulate selling tickets in multi-thread way
# Written by Ching


import threading
import time
import os
import random

# 这个函数可以做其他的家务活
def doChore():
    time.sleep(0.5)

def printTicket(num):
    print("remain ticket:",num)

# 这一个线程处理类
# 自己定义了一个类BoothThread, 这个类继承自thread.Threading类
class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid = tid
        self.monitor = monitor
        threading.Thread.__init__(self)

    def run(self):
        while True:
            monitor['lock'].acquire()  # 上锁或者等待其他线程释放所，锁，或等待其他线程正在持有锁
            if monitor['tick'] != 0:
                monitor['tick'] = monitor['tick'] - 1  # 售出一张票
                print(self.tid, ':now left:', "Z" + str(int(random.random() * 1000)))  # 打印已售出的车票 monitor['tick']
                doChore()  # 其他关键业务
                printTicket(monitor['tick'])
            else:
                print("Thread_id", self.tid, "No more tickets")  # 打印没有票了
                os._exit(0)  # 全部线程立刻退出
            monitor['lock'].release()  # 释放锁
            doChore()  # 非关键业务
            

# Start of the main function 主函数
monitor = {'tick':100, 'lock':threading.Lock()}  # 给线程上锁

# 开启10个线程
for k in range(10):
    new_thread = BoothThread(k, monitor)  # 给线程设置目标函数
    new_thread.start()  # 开始运行线程
