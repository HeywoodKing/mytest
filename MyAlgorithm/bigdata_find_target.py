# -*- coding: utf-8 -*-
import os
import heapq
import operator
import pprint
from collections import Counter

source_file = 'E:/Python/PythonProject/Algorithm/bigdata.txt'
temp_files = 'E:/Python/PythonProject/Algorithm/temp/'
top_1000ip = []


def hash_file():
    temp_path_list= []
    if not os.path.exists(temp_files):
        os.mkdir(temp_files)

    for i in range(0, 1000):
        temp_path_list.append(open(temp_files + str(i) + '.txt', mode='w', encoding='utf-8'))

    with open(source_file, encoding='utf-8') as f:
        for line in f:
            temp_path_list[hash(str(line)) % 1000].write(line)
            # print(temp_path_list, hash(str(line)) % 1000, hash(str(line)), line)

    # print('temp_path_list:', temp_path_list)
    for i in range(0, 1000):
        temp_path_list[i].close()


def calc_query_frequency():
    for root, dirs, files in os.walk(temp_files):
        for file in files:
            real_path = os.path.join(root, file)
            ip_list = []

            with open(real_path, encoding='utf-8') as f:
                for line in f:
                    ip_list.append(line.replace('\n', ''))

            try:
                top_1000ip.append(Counter(ip_list).most_common()[0])
            except:
                pass


def get_ip():
    pprint.pprint(top_1000ip)
    return (sorted(top_1000ip, key=lambda a: a[1], reverse=True)[0])[0]


if __name__ == "__main__":
    hash_file()
    calc_query_frequency()
    print(get_ip())
