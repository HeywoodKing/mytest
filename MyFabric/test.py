# -*- encoding: utf-8 -*-
"""
@File           : db_api.py
@Time           : 2019/12/27 18:11
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
from fabric2 import Connection


def main():
    fab = Connection(
        host='www.xachf.com', user='root', port=22, connect_timeout=20,
        connect_kwargs={"password": "@chinslicking2019"}
    )
    # print(fab)
    res = fab.run('uname -s', hide=True)
    # 'command', 'connection', 'encoding', 'env', 'exited', 'failed', 'hide', 'ok', 'pty', 'return_code', 'shell', 'stderr', 'stdout', 'tail'
    # print(dir(res))
    # print(res.stdout.strip())
    # print(res.command, res.connection.host,res.connection.user)
    if res.ok:
        print('{}>>用户{} 执行[{}]命令成功'.format(res.connection.host, res.connection.user, res.command))
    else:
        print('{}>>用户{} 执行[{}]命令失败'.format(res.connection.host, res.connection.user, res.command))


if __name__ == '__main__':
    main()
