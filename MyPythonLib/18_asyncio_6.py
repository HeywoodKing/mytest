# -*- coding: utf-8 -*-


import time
import asyncio
import aiohttp
import aioredis
from motor.motor_asyncio import AsyncIOMotorClient
import collections
import logging
from pprint import pprint
from bs4 import BeautifulSoup


class AsyncFetch(object):
    def __init__(self, url_list, max_semaphores=5, max_queues=5, max_threads=5):
        self.urls = url_list
        self.results = []
        # self.max_semaphore = max_semaphores
        self.semaphore = asyncio.Semaphore(max_semaphores)
        self.max_queues = max_queues
        self.max_threads = max_threads
        self.worker = collections.defaultdict(int)

    def _parse_results(self, url, html):
        """
        解析任务内容
        :param url: 任务URL
        :param html: 任务HTML
        :return:
        """
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find('title').get_text()
        except Exception as ex:
            raise ex

        if title:
            # self.results[url] = title
            self.results.append((url, title,))

    async def get_body(self, url):
        """
        获取任务内容主体
        :param url: 任务URL
        :return: 返回任务URL和任务内容HTML
        """
        async with self.semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=15) as response:
                    assert response.status == 200
                    html = await response.read()
                    return response.url, html

    async def get_results(self, url):
        """
        获取任务结果
        :param url: 任务URL
        :return: 返回任务状态
        """
        url, html = await self.get_body(url)
        self._parse_results(url, html)
        return '%s Completed' % url

    async def handler_task(self, task_id, work_queue):
        """
        任务处理（循环取出队列的URL进行下面的工作直到队列为空）
        :param task_id: 工人id
        :param work_queue: 任务队列
        :return:
        """
        while not work_queue.empty():
            current_url = await work_queue.get()
            self.worker[task_id] += 1
            try:
                print(task_id, current_url, 'running...')
                task_status = await self.get_results(current_url)
                print(task_id, task_status)
            except Exception as ex:
                logging.exception('Error for {}'.format(current_url), exc_info=True)

        print('worker:%s task finish' % task_id)

    def eventloop(self):
        """
        入口方法，协程事件循环
        :return:
        """
        q = asyncio.Queue(maxsize=self.max_queues)
        [q.put_nowait(url) for url in self.urls]
        loop = asyncio.get_event_loop()
        try:
            # 如果设置的工人数量多余任务数量，则安装每个人一个任务的需求作业
            max_workers = len(self.urls) if self.max_threads > len(self.urls) else self.max_threads
            tasks = [self.handler_task(task_id, q, ) for task_id in range(max_workers)]
            loop.run_until_complete(asyncio.wait(tasks))
        finally:
            # print('作业完成！')
            loop.close()


class AsyncRedisDB(object):
    def __init__(self):
        pass

    async def do_find(self, loop):
        """
        查询
        :param loop:
        :return:
        """
        pass

    async def do_find_one(self, loop):
        pass

    async def do_insert(self, loop):
        """
        插入
        :param loop:
        :return:
        """
        conn = await aioredis.create_connection(
            'redis://localhost',
            loop=loop
        )
        await conn.execute('set', 'my-key', 'value')
        val = await conn.execute('get', 'my-key')
        print(val)
        conn.close()
        await conn.wait_closed()

    def eventloop(self):
        """
        入口方法，协程事件循环
        :return:
        """
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.go_db(loop))
        loop.close()


class AsyncMongoDB(object):
    def __init__(self, host='127.0.0.1', port=27017, db_name='admin', col_name='test'):
        self.host = host
        self.port = port
        self.client = AsyncIOMotorClient('mongodb://{}:{}'.format(host, port))
        self.db = self.client[db_name]
        self.collection = self.db[col_name]
        # db = self.client[self.db_name]
        # collection = db[self.col_name]

    async def do_find(self):
        pass

    async def do_find_one(self):
        document = await self.collection.find_one({'id': {'$lt': 1}})
        pprint(document)

    async def do_insert(self):
        document = {'key': 'value'}
        result = await self.collection.insert_one(document)
        print('result %s' % repr(result.inserted_id))


if __name__ == "__main__":
    urls = [
        'http://github.com',
        'http://www.zhihu.com',
        # 'http://www.udemy.com',
        'http://zhangslob.github.io',
        'http://edmundmartin.com'
    ]

    fetch = AsyncFetch(urls, 1, len(urls), 10)
    fetch.eventloop()
    # import pprint
    # pprint.pprint(fetch.results)
    print(fetch.results)
    # print(fetch.worker)

