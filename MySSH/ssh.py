# -*- encoding: utf-8 -*-
"""
@File           : sshcopyid.py
@Time           : 2020/4/11 12:28
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import os
import argparse
from subprocess import call


class SSHHelper(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='SSH 文件传输以及登录')
        parser.add_argument(
            "-i", "--identity_file",
            help="identity file, default to ~\\.ssh\\idrsa.pub",
            default=os.environ.get('HOME', '') + "\\.ssh\\id_rsa.pub"
        )
        parser.add_argument(
            "-d", "--dry",
            help="run in the dry run mode and display the running commands.",
            action="store_true"
        )
        parser.add_argument("remote", metavar="user@machine")

        self.args = parser.parse_args()
        self.remote_key = "~/temp_id_rsa.pub"
        # print(self.args.identity_file, self.args.dry)

    def _win2posix(self, win):
        posix = win.replace('\\', '/')
        return '/' + posix.replace(':', '', 1)

    def scp_execute(self):
        local_key = self._win2posix(self.args.identity_file)
        print('local_key:{}'.format(local_key))

        # Copy the public key over to the remote temporarily
        scp_command = "scp {} {}:{}".format(local_key, self.args.remote, self.remote_key)
        print('scp_command:{}'.format(scp_command))
        if not self.args.dry:
            call(scp_command)

    def ssh_execute(self):
        # Append the temporary copied public key to authorized_key file and then remove the temporary public key
        ssh_command = ("ssh {} "
                       "mkdir ~/.ssh;"
                       "touch ~/.ssh/authorized_keys;"
                       "cat {} >> ~/.ssh/authorized_keys;"
                       "rm {};").format(self.args.remote, self.remote_key, self.remote_key)
        print(ssh_command)
        if not self.args.dry:
            call(ssh_command)

    def run(self):
        self.scp_execute()
        # self.ssh_execute()


if __name__ == '__main__':
    # cmd执行python ssh-copy-id root@xx.xx.xx.xx，其中root为登陆用户名，xx.xx.xx.xx为IP
    ssh = SSHHelper()
    ssh.run()
