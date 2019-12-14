
import asyncio
import aiohttp


class Run(object):
    async def get_proxy(self):
        try:
            url = 'http://192.168.1.79:5555/get'
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url) as response:
                    response.raise_for_status()
                    status = response.status
                    proxy = await response.text(encoding='utf8')
                    print(proxy, status)
        except Exception as ex:
            print('get_proxy 请求报错', ex)

    async def main(self):
        tasks = [asyncio.create_task(self.get_proxy())]
        complete = await asyncio.gather(*tasks)

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())


if __name__ == '__main__':
    r = Run()
    r.run()
