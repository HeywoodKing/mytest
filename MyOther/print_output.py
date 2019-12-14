

import time


def main():
    print('倒计时程序')
    for x in range(5, -1, -1):
        my_str = '倒计时' + str(x) + '秒'
        print(my_str, end='')
        print('\b' * (len(my_str)*2), end='', flush=True)
        time.sleep(1)


def main1():
    a = []
    for i in a:
        print(i)


if __name__ == '__main__':
    main1()
