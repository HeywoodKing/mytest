# -*- encoding: utf-8 -*-
"""
@File           : dbapi.py
@Time           : 2019/12/27 18:37
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
from fabric2 import SerialGroup as Group


def main():
    fab = Group(
        "root@www.xachf.com:22", "admin@www.xachf.com:22", "test@www.xachf.com:22",
        connect_kwargs={"password": "@chinslicking2019"}
    )

    for f in fab:
        # print(f)
        try:
            res = f.run('uname -s', hide=True)

            if res.ok:
                print('{}>>用户{} 执行[{}]命令成功'.format(res.connection.host, res.connection.user, res.command))
            else:
                print('{}>>用户{} 执行[{}]命令失败'.format(res.connection.host, res.connection.user, res.command))
        except Exception as ex:
            print("{}>>{}:{}".format(f.host, f.user, ex))


if __name__ == '__main__':
    main()
