# -*- coding: utf-8 -*-


import time, asyncio, aiohttp


urls = [
    'http://www.baidu.com?q={}',
    'http://www.baidu.com?q={}',
    # 'http://www.csdn.net?q={}',
    # 'http://www.google.com?q={}',
    # 'http://www.ti.com?q={}',
    # 'http://www.github.com?q={}'
]
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


async def do_work(url, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=headers, timeout=10) as response:
                    res = await response.read()
                    print(time.time(), response.status, response.url)
                    return res
            except Exception as ex:
                print(time.time(), 'error', url, ex)


async def run():
    # 限制并发量为500
    semaphore = asyncio.Semaphore(5)
    # 总共1000任务
    tasks = [do_work(urls[i].format(i), semaphore) for i in range(len(urls))]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()

