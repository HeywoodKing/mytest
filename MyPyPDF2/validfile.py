import os
import time
import traceback
from PyPDF2 import PdfFileReader


class ValidFile(object):
    def __init__(self):
        pass

    def is_valid_pdf(self, file_path):
        """
        直接用文件内容判断头尾
        :param file_path: 参数为pdf文件全路径名
        :return:
        """
        is_valid = True
        try:
            reader = PdfFileReader(file_path)
            if reader.getNumPages() < 1:
                is_valid = False
            print('OK：{}'.format(file_path))
        except Exception as ex:
            print('Error: {}, {}'.format(file_path, ex))
            is_valid = False

        return is_valid

    def read_file(self, file_path):
        pass
        # content_result = b''
        # file_size = 0
        # with open(file_path, 'rb') as f:
        #     while True:
        #         content = f.read(1024)
        #         if not content:
        #             break
        #         file_size += len(content)
        #         content_result += content
        # file_size = file_size / 1024 / 1024
        # print(file_size, content_result)


if __name__ == '__main__':
    v = ValidFile()
    v.is_valid_pdf(r'E:\valid_file\152S43W103ZV6E.pdf')
    v.is_valid_pdf(r'E:\valid_file\RC0603FR-104K12L.pdf')
    v.is_valid_pdf(r'E:\valid_file\4990250210.pdf')
