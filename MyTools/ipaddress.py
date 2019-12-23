# -*- encoding: utf-8 -*-
"""
@File           : ipaddress
@Time           : 2019/12/22
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import socket
import uuid


def get_hostname():
    return socket.getfqdn(socket.gethostname())


def get_ip_address_lan():
    return socket.gethostbyname(get_hostname())


def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def get_mac_address():
    try:
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
    except Exception as ex:
        print(ex)
    return None
