# -*- coding: utf-8 -*-


import asyncio
import aiohttp
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq


def parser_html(html):
    # content = ''
    # soup = BeautifulSoup(html, 'html.parser')  # lxml lxml-xml xml html5lib
    # # print(soup.prettify())
    # # //*[@id="phrsListTab"]/div[2]/ul
    # div = soup.find('div', id='results-contents')
    # print(div)

    doc = pq(html)
    content = ''
    for li in doc.items("#phrsListTab .trans-container ul li"):
        content += li.text()

    # print(content)
    return content


async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            assert response.status == 200
            return await response.text()


async def main(words, loop):
    # urls = ['http://dict.youdao.com/w/eng/{}'.format(word) for word in words]
    try:
        tasks = [get_html('http://dict.youdao.com/w/eng/{}'.format(word)) for word in words]
        results = await asyncio.gather(*tasks)
        # for content in results:
        #     print(parser_html(content))

        for index, content in enumerate(results):
            print(index, parser_html(content))
    except Exception as ex:
        print('Error for:' % ex)


if __name__ == "__main__":
    text = 'home'
    words = text
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(words, loop))
    finally:
        loop.close()

