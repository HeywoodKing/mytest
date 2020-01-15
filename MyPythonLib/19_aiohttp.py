# -*- coding: utf-8 -*-


import asyncio
from aiohttp import ClientSession


tasks = []
url = 'https://www.baidu.com'


async def do_work(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            try:
                res = await response.read()
                response.raise_for_status()
                print(response.get_encoding())
                # print(response.text)
                # print(response.content)
                print(res)
            except Exception as ex:
                print(ex.message)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_work(url))
