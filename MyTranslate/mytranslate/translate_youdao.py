# -*- encoding: utf-8 -*-
"""
@File           : translate_youdao
@Time           : 2019/12/29
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import time  # 时间戳
import json  # 返回json 处理
import requests  # 请求 url
import hashlib  # md5 加密


def translate(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule
    # 有道翻译的　API
    salt = str(int(time.time() * 10000))  # 当前时间戳
    t = str(int(time.time() * 1000))  # 当前时间戳

    s = "sr_3(QOHT)L2dx#uuGR@r"  # 一段用来加密的字符串
    sign_ = "fanyideskweb" + word + salt + s

    m = hashlib.md5()  # 根据数据串的内容进行 md5 加密
    m.update(sign_.encode('utf-8'))
    # print(m.hexdigest())
    word_key = {  # key 这个字典为 POST 给有道词典服务器的内容
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': m.hexdigest(),
        'ts': t,
        'bv': '7434a9f77e8705ee10f15cb51e8d4684',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false'
    }
    response = requests.post(url, data=word_key)  # 发送请求
    # print('+' * 100)
    # print(response.text)
    # print('+' * 100)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        return response.text
    else:
        print("有道 API 调用失败")
        return None


def get_word_result(word):
    # print(word)
    word_result = json.loads(word)
    # 通过　json.loads 把返回的结果加载成 json 格式
    # print(word_result)
    print("输入的词为：" + word_result["translateResult"][0][0]['src'])
    print("翻译结果为：" + word_result["translateResult"][0][0]['tgt'])


def main():
    print("欢迎使用，本程序调用有道词典 API 进行翻译\n自动检测输入语言-->中文\n中文-->英文")
    while True:
        word = str(input("请输入你想翻译的词或者句子(输入 q 退出)："))
        if word == 'q':
            print("感谢使用")
            break
        word_ = translate(word)
        get_word_result(word_)


if __name__ == '__main__':
    main()
