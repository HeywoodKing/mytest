# -*- encoding: utf-8 -*-
"""
@File           : run
@Time           : 2019/12/21
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
# import winreg
import platform
import pprint
import netifaces


def linux_info():
    pp = pprint.PrettyPrinter(indent=4)

    # pp.pprint(netifaces.address_families)
    # 获取网关
    # pp.pprint(netifaces.gateways())
    # 获取接口ID
    # pp.pprint(netifaces.interfaces())
    # 获取IP信息
    # pp.pprint(netifaces.ifaddresses('lo'))
    # pp.pprint(netifaces.ifaddresses('enp5s0'))
    # pp.pprint(netifaces.ifaddresses('wlp3s0'))

    # 获取到IPv4地址
    pp.pprint(netifaces.ifaddresses('wlp3s0')[netifaces.AF_INET][0]['addr'])
    # 获取到IPv4的MAC地址
    pp.pprint(netifaces.ifaddresses('wlp3s0')[netifaces.AF_PACKET][0]['addr'])
    # 获取到IPv6地址
    pp.pprint(netifaces.ifaddresses('wlp3s0')[netifaces.AF_INET6][0]['addr'])


def window_info():
    pass


def main():



if __name__ == '__main__':
    main()
