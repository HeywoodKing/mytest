# -*- coding: utf-8 -*-


import time
import asyncio


def write_log(content, future):
    with open('log.txt', 'a+', encoding='utf8') as f:
        f.write(content)


def callback(future):
    print('callback:', future.result())


# 定义一个异步函数
async def do_work1(i, loop):
    print('开始执行协程')
    print('%s Hello World:%s' % (i, time.time()))

    # print('call_soon start', time.time())

    # loop.call_soon(write_log, '回调函数内容')
    # loop.call_at(loop.time() + 1, write_log, 'call_at')
    # loop.call_later(1, write_log, 'call_later')

    # 模拟耗时操作
    await asyncio.sleep(2)

    # print('call_soon end', time.time())

    print('协程执行结束')
    return 'do_work' + str(i)


# 创建事件循环
if __name__ == "__main__":
    # 声明一个异步的事件循环
    loop = asyncio.get_event_loop()

    try:
        # 第一种写法
        # result = loop.run_until_complete(do_work1(loop))
        # print(result)

        # 第二种写法
        # tasks = [do_work1(i, loop) for i in range(2)]
        # loop.run_until_complete(asyncio.wait(tasks))

        # 第三种写法
        # 创建5个任务, 如果我们的协程函数有返回值而且我们要使用这个返回值，
        # 则一定要创建一个任务loop.create_task
        # tasks = [loop.create_task(do_work1(i, loop)) for i in range(5)]

        # tasks = [asyncio.ensure_future(do_work1(i, loop)) for i in range(5)]

        # 给每一个任务添加回调函数
        tasks = []
        for i in range(5):
            tk = asyncio.ensure_future(do_work1(i, loop))
            # 这里的tk和callback函数里面的future参数实际上是同一个对象
            tk.add_done_callback(callback)
            tasks.append(tk)

        # asyncio.wait无法收集每个协程函数执行之后的返回值,返回值在传入的tasks上
        # results, pendings = await asyncio.wait(tasks)
        # results = loop.run_until_complete(asyncio.wait(tasks))
        # for res in tasks:
        #     print(res.result())

        # asyncio.gather收集每个协程函数执行之后的返回值,同时返回值在传入的tasks上
        results = loop.run_until_complete(asyncio.gather(*tasks))
        for res in results:
            print(res)
        # for res in tasks:
        #     print(res.result())

        # for task in results:
        #     print(task)
        #     print(task.result())
    except KeyboardInterrupt as ex:
        print(asyncio.Task.all_tasks())
        for task in asyncio.Task.all_tasks():
            print(task.cancel())

        loop.stop()
        loop.run_forever()
    finally:
        print('事件循环完毕')
        loop.close()

