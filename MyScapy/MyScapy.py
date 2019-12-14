# -*- encoding: utf-8 -*-
"""
@File           : MyScapy.py
@Time           : 2019/11/19 20:47
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""

import threading
from time import ctime
from scapy.all import *
# from scapy.contrib.etherip import IP
from scapy.contrib.icmp_extensions import IP, ICMP


def scan(ip, cc, handle):
    global dict
    dst = ip + str(cc)
    packet = IP(dst=dst, ttl=20) / ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if reply:
        print(reply.src, ' is online')
        tmp = [1, reply.src]
        handle.write(reply.src + '\n')
        # handle.write(reply.src+" is online"+"\n")


def main():
    threads = []
    ip = '192.168.1.1'
    s = 2
    e = 254
    f = open('ip.log', 'w')
    for i in range(s, e):
        t = threading.Thread(target=scan, args=(ip, i, f))
        threads.append(t)
    print("main Thread begins at ", ctime())

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("main Thread ends at ", ctime())


if __name__ == '__main__':
    main()
