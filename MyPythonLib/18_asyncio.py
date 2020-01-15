# -*- coding: utf-8 -*-


import time
import asyncio


# 定义一个异步函数
async def do_work(index, delay):
    # asyncio.sleep(1)
    await asyncio.sleep(delay)
    print('%s Hello World:%s' % (index, time.time()))


# 创建事件循环
if __name__ == "__main__":
    # 声明一个异步的事件循环
    loop = asyncio.get_event_loop()
    # for i in range(5):
    #     loop.run_until_complete(do_work(i))

    loop.run_until_complete(do_work(1, 2))
    # loop.run_until_complete(do_work(2, 1))
    # loop.run_until_complete(do_work(3, 4))
    # loop.run_until_complete(do_work(4, 2))

    loop.close()
