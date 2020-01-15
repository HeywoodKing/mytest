# -*- coding: utf-8 -*-


import time
import asyncio
from threading import Thread


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def do_work(x):
    print('start work {}'.format(x))
    time.sleep(x)
    print('end work {}'.format(x))


async def do_work2(x):
    print('waiting work {}'.format(x))
    await asyncio.sleep(x)
    print('done work {}'.format(x))


if __name__ == '__main__':
    main_loop = asyncio.get_event_loop()
    t = Thread(target=start_loop, args=(main_loop,))
    t.start()
    print('线程已启动')

    # main_loop.call_soon_threadsafe(do_work, 6)
    # main_loop.call_soon_threadsafe(do_work, 3)

    asyncio.run_coroutine_threadsafe(do_work2(6), main_loop)
    asyncio.run_coroutine_threadsafe(do_work2(3), main_loop)

    # 主线程中创建一个new_loop，然后在另外的子线程中开启一个无限事件循环。
    # 主线程通过run_coroutine_threadsafe新注册协程对象。这样就能在子线程中进行事件循环的并发操作，
    # 同时主线程又不会被block。一共执行的时间大概在6s左右

    # main_loop.close()

