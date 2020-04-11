# -*- encoding: utf-8 -*-
"""
@File           : db_api.py
@Time           : 2019/12/30 19:00
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import time
import requests
from fake_useragent import UserAgent


def main(key):
    session = requests.session()
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    salt = int(time.time() * 10000)
    ts = int(salt / 10)

    form_data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": "abf857d70c24cb55263b1f624193b38b",
        "ts": ts,
        # "bv": "bbb3ed55971873051bc2ff740579bb49",
        "bv": "316dd52438d41a1d675c1d848edf4877",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
    }

    try:
        with session.post(url=url, params=form_data, headers=headers) as resp:
            resp.raise_for_status()
            if resp.status_code == 200:
                json_data = resp.json()
                if json_data['errorCode'] == 0:
                    res = json_data['translateResult'][0][0]['tgt']
                    print('翻译结果：{}'.format(res))
            else:
                print(resp.status_code)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    while True:
        keyword = input("请输入要翻译的内容：")
        main(keyword)
