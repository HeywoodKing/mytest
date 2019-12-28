# -*- encoding: utf-8 -*-
"""
@File           : operate.py
@Time           : 2019/12/27 21:39
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
from fabric2 import Connection, Config
from invoke import Responder, task, exceptions
import socket
# import k8s
import asyncio


def create_th_num(c):
    zh = c.run("locale | grep LANG= | grep zh_CN | wc -l")
    patten = 'UNIX 密码' if zh == 1 else 'new UNIX password:'
    passwd_res = Responder(
        pattern=patten,
        response="th_num.20..\n"
    )
    try:
        c.sudo("useradd -d /home/th_num -s /bin/bash -U -m  th_num")
    except exceptions.UnexpectedExit as e:
        print(e)
        c.sudo("rm  /etc/sudoers.d/th_num")
        c.sudo("userdel -r th_num")
        c.sudo("useradd -d /home/th_num -s /bin/bash -U -m  th_num")
    c.sudo("passwd th_num", pty=True, watchers=[passwd_res, ])
    c.sudo("echo \"th_num ALL=(ALL:ALL) NOPASSWD:ALL\" | sudo tee /etc/sudoers.d/th_num", pty=True)


def insert_ssh_keys(c, ssh_key, ssh_share_key=None, ssh_share_key_sec=None):
    try:
        c.run("cd ~ && mkdir .ssh")
    except exceptions.UnexpectedExit:
        pass
    c.run("chmod 0700 ~/.ssh")
    c.run('echo "' + ssh_key + '" >> ~/.ssh/authorized_keys')
    if ssh_share_key:
        c.run('echo "' + ssh_share_key + '" > ~/.ssh/id_rsa.pub')
        c.run("chmod 0600 ~/.ssh/id_rsa.pub")
    if ssh_share_key_sec:
        c.run('echo "' + ssh_share_key_sec + '" > ~/.ssh/id_rsa')
        c.run("chmod 0600 ~/.ssh/id_rsa")
    c.run("chmod 0600 ~/.ssh/authorized_keys")


def installnccl(c):
    c.run(
        "wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb")
    c.sudo("dpkg -i nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb")
    c.sudo("apt update")
    c.sudo("apt install  libnccl2=2.2.13-1+cuda9.0 libnccl-dev=2.2.13-1+cuda9.0")


def installcudnnNew(c):
    c.sudo("dpkg -i libcudnn7_7.1.4.18-1+cuda9.0_amd64.deb")


def create_user(c, username, ssh_key):
    zh = c.run("locale | grep LANG= | grep zh_CN | wc -l")
    patten = 'UNIX' if zh == 1 else 'new UNIX password:'
    newpasswd = username + ".2018!"
    passwd_res = Responder(
        pattern=patten,
        response=newpasswd + "\n"
    )
    try:
        c.sudo("useradd -d /home/%s -s /bin/bash -U -m  %s" % (username, username))
    except exceptions.UnexpectedExit as e:
        print(e)
        c.sudo("userdel -r %s" % username)
        c.sudo("useradd -d /home/%s -s /bin/bash -U -m  %s" % (username, username))
    c.sudo("passwd %s" % username, pty=True, watchers=[passwd_res, ])
    c.sudo('su - %s -c "mkdir /home/%s/.ssh && echo %s > /home/%s/.ssh/authorized_keys && \
    chmod 0700 /home/%s/.ssh && chmod 0600  /home/%s/.ssh/authorized_keys" ' % (
        username, username, ssh_key, username, username, username))
    return newpasswd


def new_user(username, ssh_key, host):
    with Connection(host=host, user='th_num', port=22, connect_kwargs={"key_filename": "/Users/panyan/.ssh/id_rsa"},
                    connect_timeout=5) as c:
        create_user(c, username, ssh_key)


def setsudoNopass(c, user):
    c.sudo("echo \"%s ALL=(ALL:ALL) NOPASSWD:ALL\" | sudo tee /etc/sudoers.d/%s" % (user, user), pty=True)


def installAnaconda(c):
    try:
        c.run("rm Anaconda2-5.2.0-Linux-x86_64.sh*")
    except exceptions.UnexpectedExit as e:
        pass
    c.run("wget https://repo.anaconda.com/archive/Anaconda2-5.2.0-Linux-x86_64.sh")
    c.run("chmod +x Anaconda2-5.2.0-Linux-x86_64.sh")
    try:
        c.run("./Anaconda2-5.2.0-Linux-x86_64.sh -b -p $HOME/anaconda2")
        c.run("echo 'export PATH=\"/home/th_num/anaconda2/bin:$PATH\"' >> ~/.bashrc")
    except exceptions.UnexpectedExit as e:
        print(e)
    try:
        c.run("rm Anaconda2-5.2.0-Linux-x86_64.sh*")
    except exceptions.UnexpectedExit as e:
        pass


def installCuda(c):
    c.run(
        "wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.0.176-1_amd64.deb")
    c.sudo("dpkg -i cuda-repo-ubuntu1604_9.0.176-1_amd64.deb")
    c.sudo(
        "apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub")
    c.sudo("apt-get update")
    c.sudo("apt-get install cuda-9-0 -y")
    c.sudo("nvidia-xconfig")


def setHostnameandHosts(host, n):
    hostfile = """127.0.0.1 localhost
    ::1     localhost ip6-localhost ip6-loopback
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters
    172.164.18.1  th01
    172.164.18.2  th02
    172.164.18.9  th03
    172.164.18.10  th04"""
    config = Config(overrides={'sudo': {'password': 'ehxP5vdsVfsdc'}})
    with Connection(host=host, user='th_num', port=22, config=config,
                    connect_kwargs={"key_filename": "/Users/WANG/.ssh/id_rsa", "password": "password"},
                    connect_timeout=120) as c:
        c.sudo("echo \"%s\" | sudo tee /etc/hosts" % hostfile)
        c.sudo("hostnamectl set-hostname th0%d --transient --static " % n)


def setNopasswodssh(c):
    c.sudo("echo \"PasswordAuthentication no\" | sudo tee /etc/ssh/sshd_config", pty=True)
    c.sudo("systemctl restart ssh")


def createConnect(user, host, password, port=22, timeout=120, keyfile='~/.ssh/id_rsa'):
    config = Config(overrides={'sudo': {'password': password}})
    return Connection(host=host, user=user, port=22, config=config,
                      connect_kwargs={"key_filename": keyfile, "password": password}, connect_timeout=timeout)
    # return Connection(host=host,user=user,port=22,config=config,connect_kwargs={"password":password},connect_timeout=timeout)


def removeolduser(c, olduser):
    c.run("sudo pkill -u %s" % olduser, pty=True)
    c.sudo("userdel -r %s" % olduser)


def runCmd(c, cmd):
    c.sudo(cmd)


# async def installOpenMpi(c):
#     try:
#         c.run("wget https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.1.tar.bz2")
#         c.run("tar -xvf openmpi-3.1.1.tar.bz2")
#         c.run("cd openmpi-3.1.1 && ./configure --prefix=/usr/local --with-cuda && sudo make all install")
#     except BaseException as e:
#         print(e)
#         c.run("rm openmpi-3.1.1.tar.bz2")
#         c.sudo("rm openmpi-3.1.1 -rf")

def installPytorch(c):
    c.sudo("pip3.6 install torch torchvision")
    return 0


def installPython36(c):
    resp = Responder(
        pattern=r'Press \[ENTER\] to continue or ctrl-c to cancel adding it',
        response='\r', )
    c.sudo("add-apt-repository ppa:deadsnakes/ppa", pty=True, watchers=[resp])
    c.sudo("apt update")
    c.sudo("apt install python3.6 python3.6-dev -y")
    c.run("wget https://bootstrap.pypa.io/get-pip.py")
    c.sudo("python3.6 get-pip.py")


if __name__ == "__main__":
    iplist = ['192.168.16.156',
              '192.168.16.157', ]
    user = 'th_num'
    password = 'th_num'
    keyfile = "/home/th_num/.ssh/id_rsa"

    runlist = []
    arg_command = input("输入执行的命令:")

    for ip in iplist:
        c = createConnect(user, ip, password, keyfile=keyfile)
        # c.put('/home/th_num/pytorch_mnist.py','/home/th_num/pytorch_mnist.py')
        # runCmd(c,"rm /home/th_num/pytorch_resnet.py /home/th_num/pytorch_mnist.py")
        # runCmd(c,"pip3.6 uninstall -y horovod;HOROVOD_GPU_ALLREDUCE=NCCL pip3.6 install --user --no-cache-dir git+https://github.com/wu-yy/horovod.git")
        runCmd(c, arg_command)
        # runCmd(c,"cp/home/th_num/pytorch_mnist.py /home/th_num/pytorch_mnist.py")
        # runCmd(c,"ldconfig")
    # runlist.append(installOpenMpi(c))
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(runlist))
    # loop.close()
