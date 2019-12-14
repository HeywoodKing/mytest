


import time


def main():
    print('显示百分比')
    for x in range(101):
        my_str = '百分比' + str(x) + '%'
        print(my_str, end='')
        print('\b' * (len(my_str) * 2), end='', flush=True)
        time.sleep(0.1)


if __name__ == '__main__':
    main()
