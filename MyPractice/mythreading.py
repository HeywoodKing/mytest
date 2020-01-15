# Filename:mythreading.py
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

# 这每一个线程要处理的函数
def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()  # 上锁或者等待其他线程释放所，锁，或等待其他线程正在持有锁
        if i != 0:
            i = i - 1  # 售出一张票
            print(tid,':now left:', "Z" + str(int(random.random() * 1000)))  # 打印已售出的车票
            # doChore()  # 其他关键业务
            printTicket(i)
        else:
            print("Thread_id",tid,"No more ticket")  # 打印没有票了
            os._exit(0)  # 全部线程立刻退出
        lock.release()  # 释放锁
        doChore()  # 非关键业务

# Start of the main function 主函数
i = 100  # 票的数量
lock = threading.Lock()  # 给线程上锁

# 开启10个线程
for k in range(10):
    new_thread = threading.Thread(target=booth,args=(k,))  # 给线程设置目标函数
    new_thread.start()  # 开始运行线程
