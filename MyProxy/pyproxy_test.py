

import requests


def get_proxy2():
    res = requests.get('http://192.168.1.79:5555/get')
    return res.text


if __name__ == '__main__':
    proxy = get_proxy2()
    print(proxy)
