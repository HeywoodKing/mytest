# -*- encoding: utf-8 -*-
"""
@File           : deploy.py
@Time           : 2019/12/27 18:57
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import shutil
from fabric2 import Connection
from MyFabric.setting import *


def start_deploy():
    """
    打包部署到远程机器
    :return:
    """
    try:
        conn = Connection(host=HOST, port=PORT, user=USER, connect_kwargs={'password': PASSWORD},
                          connect_timeout=CONNECT_TIMEOUT)
        # shutil.make_archive(base_name, format, base_dir)
        """
        base_name       ---> 创建的目标文件名，包括路径，减去任何特定格式的扩展
        format          ---> 压缩包格式后缀：zip、tar、bztar、gztar、xztar
        base_dir        ---> 开始打包的路径
        """
        folder = '{}/{}'.format(SERVER_PATH.rstrip('/'), PACK_FILENAME)

        if COMPRESS_TYPE.lower() == 'gztar':
            shutil.make_archive(PACK_FILENAME, 'gztar', LOCAL_PATH)
        elif COMPRESS_TYPE.lower() == 'bztar':
            shutil.make_archive(PACK_FILENAME, 'bztar', LOCAL_PATH)
        elif COMPRESS_TYPE.lower() == 'xztar':
            shutil.make_archive(PACK_FILENAME, 'xztar', LOCAL_PATH)
        elif COMPRESS_TYPE.lower() == 'tar':
            shutil.make_archive(PACK_FILENAME, 'tar', LOCAL_PATH)
        else:
            # COMPRESS_TYPE.lower() == 'zip':
            shutil.make_archive(PACK_FILENAME, 'zip', LOCAL_PATH)

        # 首先进入根目录
        conn.run('cd {}'.format(SERVER_PATH.rstrip('/')))

        # 先删除旧文件加以及文件，包等
        conn.run('rm -rf {} {}'.format(PACK_FILENAME, PACK_FULL_FILENAME))

        # 创建文件夹
        conn.run('mkdir {}'.format(folder))

        # 上传包
        conn.put(PACK_FULL_FILENAME, SERVER_PATH)

        # 解压到指定目录下
        conn.run('tar -C {} -zxvf {}/{}'.format(folder, SERVER_PATH.rstrip('/'), PACK_FULL_FILENAME))

        # 赋值权限
        # conn.sudo('chmod -R 666 {}'.format(folder))

        # 重启web服务器
        conn.run('systemctl nginx restart')

        # 重启网关接口
        conn.run('supervisorctl start uwsgi ')

    except Exception as ex:
        print('{}'.format(ex))


if __name__ == '__main__':
    start_deploy()
