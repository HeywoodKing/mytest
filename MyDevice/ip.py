# -*- encoding: utf-8 -*-
"""
@File           : ip
@Time           : 2019/12/22
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import ipaddress


def test():
    # ip = ipaddress.ip_address('192.168.0.6')
    ip = ipaddress.ip_network('192.168.0.6/24', strict=False).num_addresses
    # ip = ipaddress.ip_interface('192.168.0.6/24').network
    # ip = ipaddress.ip_address('fe80::1').version
    print(ip)
    # 计算有多少个可用IP
    # net = ipaddress.ip_network('192.168.0.1/24', strict=False)
    # for x in net.hosts():
    #     print(x)

    netmask = ipaddress.ip_network('192.168.0.1/24', strict=False).netmask
    hostmask = ipaddress.ip_network('192.168.0.1/24', strict=False).hostmask
    print(netmask, hostmask)

    ip = ipaddress.ip_network('192.168.0.1/24', strict=False).network_address
    broadcast = ipaddress.ip_network('192.168.0.1/24', strict=False).broadcast_address
    print(ip, broadcast)


def get_ip_info(ip_net):
    try:
        net = ipaddress.ip_network(ip_net, strict=False)
        print('IP版本号： ' + str(net.version))
        print('是否是私有地址： ' + str(net.is_private))
        print('IP地址总数: ' + str(net.num_addresses))
        print('可用IP地址总数： ' + str(len([x for x in net.hosts()])))
        print('网络号： ' + str(net.network_address))
        print('起始可用IP地址： ' + str([x for x in net.hosts()][0]))
        print('最后可用IP地址： ' + str([x for x in net.hosts()][-1]))
        print('可用IP地址范围： ' + str([x for x in net.hosts()][0]) + ' ~ ' + str([x for x in net.hosts()][-1]))
        print('掩码地址： ' + str(net.netmask))
        print('反掩码地址： ' + str(net.hostmask))
        print('广播地址： ' + str(net.broadcast_address))
    except ValueError:
        print('您输入格式有误，请检查！')


if __name__ == '__main__':
    ip = '192.168.1.1/24'
    get_ip_info(ip)
