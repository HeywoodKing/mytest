# -*- coding: utf-8 -*-


import re


def check_ip(ip):
    # 255.255.255.255
    pattern = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if pattern.match(ip):
        return True

    return False


def check_phone(phone):
    # pattern = re.compile(r'^1(3|5|7|8)\d{9}$')
    # pattern = re.compile(r'^1([38]\d|5[0-35-9]|7[3678])\d{8}$')
    pattern = re.compile(r'^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}$')
    if pattern.match(phone):
        return True

    return False


def check_email(email):
    # pattern = re.compile(r'^.+?@.+?\.com$')
    pattern = re.compile(r'^[a-zA-Z0-9]+[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
    pattern = re.compile(r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
    if pattern.match(email):
        return True

    return False


def check_domain(domain):
    pattern = re.compile(r'^[a-zA-Z0-9]+(\.?[a-zA-Z0-9_-]+)+$')
    if pattern.match(domain):
        return True

    return False


# print(check_ip('222.250.234.99'))
# print(check_phone('18890909090'))
# print(check_email('aa2_2a__?_@aaa.com'))
print(check_domain('www.baidu-image.ok_http78.com'))
