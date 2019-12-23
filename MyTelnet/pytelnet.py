# -*- encoding: utf-8 -*-
"""
@File           : pytelnet
@Time           : 2019/12/22
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import time
import logging
from telnetlib import Telnet


class TelnetClient(object):
    """
    初始化属性
    """

    def __init__(self):
        self.tn = Telnet()

    def login_host(self, ip, username, password, enable=None, verbose=True):
        """
        定义login_host函数，用于登陆设备
        :param ip:
        :param username:
        :param password:
        :param enable:
        :param verbose:
        :return:
        """
        '连接设备，try-except结构'
        try:
            self.tn.open(ip, port=23)
        except:
            logging.warning('%s网络连接失败' % ip)
            return False
        '输入用户名'
        self.tn.read_until(b'Username:', timeout=1)
        self.tn.write(b'\n')
        self.tn.write(username.encode() + b'\n')
        rely = self.tn.expect([], timeout=1)[2].decode().strip()  # 读显
        if verbose:
            print(rely)
        '输入用户密码'
        self.tn.read_until(b'Password:', timeout=1)
        self.tn.write(password.encode() + b'\n')
        rely = self.tn.expect([], timeout=1)[2].decode().strip()
        if verbose:
            print(rely)
        '进去特权模式'
        if enable is not None:
            self.tn.write(b'enable\n')
            self.tn.write(enable.encode() + b'\n')
            if verbose:
                rely = self.tn.expect([], timeout=1)[2].decode().strip()
                print(rely)
                time.sleep(1)

        rely = self.tn.read_very_eager().decode()
        if 'Login invalid' not in rely:
            logging.warning('%s登陆成功' % ip)
            return True
        else:
            logging.warning('%s登陆失败，用户名或密码错误' % ip)
            return False

    '定义do_cmd函数,用于执行命令'

    def do_cmd(self, cmds):
        '读取文件，for语句循环执行命令'
        with open(cmds) as cmd_obj:
            for cmd in cmd_obj:
                self.tn.write(cmd.encode().strip() + b'\n')
                time.sleep(2)
                rely = self.tn.read_very_eager().decode()
                logging.warning('命令执行结果:\n %s' % rely)

    '定义logout_host函数，关闭程序'

    def logout_host(self):
        self.tn.close()


def main():
    username = 'flack'  # 用户名
    password = 'root'  # 密码
    enable = 'root'  # 特权密码
    lists = 'list.txt'  # 存放IP地址文件，相对路径
    cmds = 'cmd.txt'  # 存放执行命令文件，相对路径
    telnet_client = TelnetClient()
    '读取文件，for语句循环登陆IP'
    with open(lists, 'rt') as list_obj:
        for ip in list_obj:
            '如果登录结果为True，则执行命令，然后退出'
            if telnet_client.login_host(ip.strip(), username, password, enable):
                telnet_client.do_cmd(cmds)
                telnet_client.logout_host()
                time.sleep(2)


if __name__ == '__main__':
    main()
