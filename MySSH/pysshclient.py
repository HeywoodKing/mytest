# -*- encoding: utf-8 -*-
"""
@File           : sshclient
@Time           : 2019/12/22
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from datetime import datetime
import time
import logging


class SSHClient(object):
    def __init__(self):
        self.ssh = None

    def login_host(self, device):
        """
        定义login_host函数，用于登陆设备
        :param device:
        :return:
        """
        try:
            self.ssh = ConnectHandler(**device)
            self.ssh.enable()
            reply = self.ssh.find_prompt()
            print('>' * 10 + '成功登陆结果如下:' + '>' * 10 + '\n' + reply)
            return True
        except ValueError:
            logging.warning(device['host'] + ' Secret 密码错误')
        except NetMikoTimeoutException:
            logging.warning(device['host'] + ' 连接不上设备,请检查网络是否正常通信')
        except NetMikoAuthenticationException:
            logging.warning(device['host'] + ' 登录失败,用户名或密码错误')

    def do_cmd(self, cmds):
        """
        定义do_cmd函数,用于执行命令
        :param cmds:
        :return:
        """
        with open(cmds) as cmd_obj:
            for cmd in cmd_obj:
                reply = self.ssh.send_command(cmd)
                time.sleep(1)
                logging.warning('>' * 10 + cmd.rstrip() + ' 命令执行结果如下:' + '>' * 10 + '\n' + reply)

    def logout_host(self):
        """
        定义logout_host函数，关闭程序
        :return:
        """
        self.ssh.disconnect()


if __name__ == '__main__':
    cmds = 'cmd.txt'
    ssh_client = SSHClient()
    start_time = datetime.now()
    devices = [
        {
            'device_type': 'linux',
            # 'name': '11',
            'host': '192.168.0.6',
            'port': 22,
            'username': 'flack',
            'password': 'root'
        },
    ]
    for device in devices:
        # 如果登录结果为True，则执行命令，然后退出
        if ssh_client.login_host(device):
            ssh_client.do_cmd(cmds)
            ssh_client.logout_host()
            time.sleep(2)
    stop_time = datetime.now()
    print('总花费时长：{0}\n'.format(stop_time - start_time))

