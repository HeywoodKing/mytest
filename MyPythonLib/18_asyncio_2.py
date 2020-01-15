# -*- coding: utf-8 -*-


import time
import asyncio
from aiohttp import ClientSession


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)


if __name__ == "__main__":
    url = 'https://www.baidu.com'
    tasks = []
    print(time.time())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello(url))
    print(time.time())
