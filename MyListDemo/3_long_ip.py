# -*- coding: utf-8 -*-


import socket
import struct


# 将字符串IP转换为长整型
def ip2long(ip):
    """
    将点分十进制IP地址转换成无符号的长整形
    :param ip:
    :return:
    """
    # !I 将network byte > host byte
    # print(socket.inet_aton(ip), socket.inet_aton(ip).decode('gb2312'))
    # print(struct.unpack("!I", socket.inet_aton(ip)))
    return struct.unpack("!I", socket.inet_aton(ip))[0]


# 将长整型IP转为字符串IP
def long2ip(lint):
    """
    将无符号长整型转换为点分十进制IP地址
    :param lint:
    :return:
    """
    # !I 将network byte > host byte
    # print(struct.pack("!I", lint))
    return socket.inet_ntoa(struct.pack("!I", lint))


# 返回下一个IP
def get_next_ip(ip):
    new_ip = ip2long(ip)
    new_ip += 1
    return long2ip(new_ip)


# ip = get_next_ip('192.168.1.12')
# print(ip)


