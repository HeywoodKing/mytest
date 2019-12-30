# -*- encoding: utf-8 -*-
"""
@File           : translate
@Time           : 2019/12/23
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import urllib
import codecs
import re
import time
import requests
from sys import argv
from bs4 import BeautifulSoup


class Translate(object):
    def __init__(self):
        self.outtext = None

    def start(self):
        self._get_html_source()
        self._get_content("enc")
        self._remove_tag()
        self._print_result()

    def _get_html_source(self):
        word = argv[1] if len(argv) > 1 else ''
        url = "http://dict.baidu.com/s?wd=%s&tn=dict" % word
        # self.html_source = unicode(urllib.urlopen(url).read(), "gb2312", "ignore").encode("utf-8", "ignore")
        with requests.get(url) as resp:
            if resp.status_code == 200:
                resp.encoding = resp.apparent_encoding
                self.html_source = resp.text

    def _get_content(self, div_id):
        soup = BeautifulSoup("".join(self.html_source))
        self.data = str(soup.find("div", {"id": div_id}))

    def _remove_tag(self):
        if self.data:
            soup = BeautifulSoup(self.data)
            self.outtext = ''.join([element for element in soup.recursiveChildGenerator() if isinstance(element, str)])

    def _print_result(self):
        for item in range(1, 10):
            self.outtext = self.outtext.replace(str(item), "\n%s" % str(item))
        self.outtext = self.outtext.replace("  ", "\n")
        print(self.outtext)


if __name__ == '__main__':
    Translate().start()
