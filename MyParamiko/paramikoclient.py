# -*- encoding: utf-8 -*-
"""
@File           : paramikoclient
@Time           : 2020/2/8
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import paramiko
from configparser import ConfigParser


class ParamikoClient(object):
    def __init__(self, config_str):
        self.conf = ConfigParser()
        self.conf.read(config_str, encoding='utf8')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client_state = 0
        self.sftp_client = None

    def connect(self):
        try:
            self.client.connect(
                hostname=self.conf.get('ssh', 'host'),
                port=self.conf.getint('ssh', 'port'),
                username=self.conf.get('ssh', 'username'),
                password=self.conf.get('ssh', 'password'),
                timeout=self.conf.getfloat('ssh', 'timeout'),
            )
            self.client_state = 1
        except Exception as ex:
            print(ex)
            self.client_state = 0
            self.client.close()
        finally:
            pass

    def run_cmd(self, cmd):
        if self.client_state == 0:
            self.connect()

        stdin, stdout, stderr = self.client.exec_command(cmd)
        for line in stdout:
            print(line)

    def get_sftp_client(self):
        if self.client_state == 0:
            self.connect()

        if not self.sftp_client:
            self.sftp_client = paramiko.SFTPClient.from_transport(self.client.get_transport())
        return self.sftp_client
