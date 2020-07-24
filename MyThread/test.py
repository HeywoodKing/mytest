# -*- encoding: utf-8 -*-
"""
@File           : db_api.py
@Time           : 2019/12/21 12:57
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed, wait, FIRST_COMPLETED, \
    ALL_COMPLETED


def worker(args):
    time.sleep(1)
    res = args * 10
    print(f"handler task{args} finished")
    return args, res


def worker_multi(args: list = None, num=0):
    time.sleep(1)
    res = "ok {}".format(args)
    total = num * 10
    print(f"handler task{num} finished")
    return res, total


def master_wait(hash_list):
    with ThreadPoolExecutor(max_workers=len(hash_list)) as pool:
        all_task = [pool.submit(worker, item) for item in hash_list]
        wait(all_task, return_when=FIRST_COMPLETED)
        print('finished')
        print(wait(all_task, timeout=2.5))


def master_as_completed(hash_list):
    with ThreadPoolExecutor(max_workers=len(hash_list)) as pool:
        obj_list = []
        for item in hash_list:
            obj = pool.submit(worker, item)
            obj_list.append(obj)

        for future in as_completed(obj_list):
            data = future.result()
            print("data={}".format(data))


def master_map(hash_list):
    i = 1

    param_list = [
        ("a", "b", "c"), ("d", "e", "f"), ("g", "h", "i"), ("j", "k", "l"), ("m", "n", "o"),
    ]

    with ThreadPoolExecutor(max_workers=len(hash_list)) as pool:
        obj_list = pool.map(worker_multi, param_list, hash_list)
        for item in obj_list:
            print("result:{}".format(item))

        # for result in pool.map(worker, hash_list):
        #     print("task{}:{}".format(i, result))
        #     i += 1


def main():
    # hash_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # master_wait(hash_list)
    # master_as_completed(hash_list)

    hash_list = [0, 1, 2, 3, 4]
    master_map(hash_list)


if __name__ == '__main__':
    main()
