# -*- encoding: utf-8 -*-
"""
@File           : baidudict.py
@Time           : 2020/4/18 13:38
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import json
import random
import hashlib
from urllib.parse import quote
import requests
from setting import *


class BaiduDict(object):
    def __init__(self):
        self.src = None
        self.url = BAIDU_URL
        self.header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
            # "Cache-Control": "max-age=0",
            # "Connection": "keep-alive",
            # "Host": "fanyi.baidu.com",
            # "Upgrade-Insecure-Requests": "1",
            "User-Agent": UA.random,
        }

    def _request(self, url, q):
        """
        请求远程api服务
        """
        try:
            if url is None:
                url = self.url

            if q is not None:
                url = url + quote(q.encode('utf-8'))
                appid = "20200417000422561"
                secret = "E6abxhIDE2DrRXCzEIk1"
                salt = random.randint(100000, 999999999)
                "appid+q+salt+密钥 的MD5值"
                md5 = hashlib.md5()
                md5.update((appid + q + salt + secret).encode('utf8'))
                sign = md5.hexdigest()
                payload = {
                    "q": q,
                    "from": "auto",
                    "to": "zh",
                    "appid": appid,
                    "salt": salt,
                    "sign": sign
                }

                resp = requests.get(url, params=payload)
                content = resp.json(encoding='utf8')
                code = 0
            else:
                code = 1
                content = 'Usage: dict fire'
        except Exception as ex:
            code = -1
            content = 'ERROR: Network or remote service error! {}'.format(ex)

        return {
            "code": code,
            "content": content
        }

    def _parse(self, content):
        """
        解析内容
        """
        code = content['errorCode']
        try:
            src = content['translateResult'][0][0]['src']  # source
            if code == 0:  # Success
                tgt = content['translateResult'][0][0]['tgt']  # result
                msg = '获取成功'
            elif code == 20:
                # print('WORD TO LONG')
                tgt = None
                msg = 'WORD TO LONG'
            elif code == 30:
                # print('TRANSLATE ERROR')
                tgt = None
                msg = 'TRANSLATE ERROR'
            elif code == 40:
                # print('DON\'T SUPPORT THIS LANGUAGE')
                tgt = None
                msg = 'DON\'T SUPPORT THIS LANGUAGE'
            elif code == 50:
                # print('KEY FAILED')
                tgt = None
                msg = 'KEY FAILED'
            elif code == 60:
                # print('DON\'T HAVE THIS WORD')
                tgt = None
                msg = 'DON\'T HAVE THIS WORD'
            else:
                # print('UNKOWN')
                tgt = None
                msg = 'UNKOWN'
        except Exception as ex:
            code = -1
            src = self.src
            tgt = None
            msg = ex

        return {
            "code": code,
            "type": content['type'],
            "src": src,
            "tgt": tgt,
            "msg": msg
        }

    def translate(self, q):
        """
        根据输入内容翻译并返回翻译结果
        :param text:
        :return:
        """
        try:
            self.src = q
            resp = self._request(url=BAIDU_URL, q=q)
            print(resp)
            return

            # if resp['code'] == 0:
            #     result = self._parse(resp['content'])
            # else:
            #     result = {
            #         "code": resp['code'],
            #         "type": None,
            #         "src": q,
            #         "tgt": q,
            #         "msg": resp['content']
            #     }
            #
            # return result
        except Exception as ex:
            raise Exception('ERROR: remote service error! {}'.format(ex))


if __name__ == '__main__':
    baidu = BaiduDict()
    baidu.translate('hello world')
