# -*- encoding: utf-8 -*-
"""
@File           : add_white.py
@Time           : 2019/11/5 11:49
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""

import requests
import time

white_list = [
    '113.81.234.227',
    '113.81.234.75',
    '113.81.235.52',
    '116.30.217.150',
    '113.81.233.33',
    '113.81.234.81',
    '113.81.234.179',
    '113.81.232.79',
    '116.30.218.172',
    '113.81.233.42',
    '113.81.233.4',
    '116.30.218.197',
    '113.81.233.228',
    '113.81.234.33',
    '113.81.233.56',
    '113.81.232.213',
    '110.43.42.121',
    '113.116.24.57',
    '113.105.121.58',
    '218.18.76.145',
    '218.18.79.22',
    '113.110.149.49',
    '113.116.8.137',
    '113.116.9.157',
    '113.116.10.143',
    '113.110.149.51',
    '113.116.9.157',
    '113.81.235.122',
    '113.81.232.4',
    '113.110.148.140',
    '113.110.148.65',
    '113.116.11.113',
    '113.110.148.139',
    '113.116.9.109',
    '113.116.11.127',
    '113.110.149.45',
    '113.81.234.119',
    '113.81.233.164',
    '116.30.218.212',
    '116.30.217.78',
    '116.30.219.123',
    '113.81.233.78',
    '116.30.219.225',
    '113.81.232.186',
    '113.81.235.95',
    '116.30.217.16',
    '113.81.235.162',
    '113.81.233.106',
    '113.81.235.201',
    '113.81.235.150',
    '113.81.235.19',
    '116.30.219.63',
    '116.30.218.55',
    '116.30.218.195',
    '113.81.233.170',
]
proxy_zhima_white_url = 'http://wapi.http.cnapi.cc/index/index/save_white?neek=58229&appkey=c96baaee3543657104015f30788fc9f0&white={}'


def add_white():
    if white_list:
        session = requests.session()
        for ip in white_list:
            time.sleep(5)
            resp = session.get(proxy_zhima_white_url.format(ip))
            if resp.status_code == 200:
                result = resp.json()
                if result['code'] == 0:
                    print('ip:{} 白名单, code:{}, msg:{}'.format(ip, result['code'], result['msg']))
                    print('添加白名单成功：{}'.format(ip))
                else:
                    print('ip:{}, code:{}, msg:{}'.format(ip, result['code'], result['msg']))

            else:
                print('添加白名单失败：{}'.format(ip))

        session.close()

    print('白名单添加完成')


if __name__ == "__main__":
    add_white()

