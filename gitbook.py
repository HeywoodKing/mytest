# -*- coding:UTF-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
# from w3lib.html import remove_tags

"""
类说明:下载小说
Parameters: 
Returns: 
Modify: 2020-01-07
Auth: eddie.wang
"""


class downloader(object):
    def __init__(self):
        self.server = 'https://www.biqukan.com'
        self.target = 'https://www.biqukan.com/74_74536/'
        self.names_urls = []
        self.nums = 0  # 章节数

    """    
    函数说明:获取下载链接

    """

    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding = 'gbk'
        html = req.text
        div_bf = BeautifulSoup(html, features="lxml")
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]), features="lxml")
        a = a_bf.find_all('a')
        self.nums = len(a[12:])
        for each in a[12:]:
            self.names = each.string
            self.urls = self.server + each.get('href')
            self.names_urls.append([self.names, self.urls])
        # print("{} '\n'".format(self.names_urls))

    """
    函数说明:获取章节内容
 
    """

    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = req.apparent_encoding
        html = req.text
        bf = BeautifulSoup((html.replace('<br>', '\n')).replace('<br/>', ''), "lxml")
        texts = bf.find_all('div', class_='showtxt')
        # texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        texts = texts[0].text
        # print(texts.encode('utf8'))
        return texts

    """
    函数说明:将爬取的文章内容写入文件

    """

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print('开始下载:')
    for i in range(dl.nums):
        print(dl.names_urls[i])
        dl.writer(dl.names_urls[i][0], '我的虚拟王国.txt', dl.get_contents(dl.names_urls[i][1]))
        sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('《我的虚拟王国》下载完成')
