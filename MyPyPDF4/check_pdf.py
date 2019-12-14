# -*- encoding: utf-8 -*-
"""
@File           : check_pdf.py
@Time           : 2019/11/4 12:36
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import optparse
import PyPDF4
from PyPDF4 import PdfFileReader


def is_valid_pdf(file_path):
    try:
        pdf_file = PdfFileReader(open(file_path, 'rb'))
        doc_info = pdf_file.getDocumentInfo()
        print('[*] PDF MetaData For: {}'.format(file_path))
        for metaItem in doc_info:
            print('[+] {0} : {1}'.format(metaItem, doc_info[metaItem]))

        return True
    except Exception as ex:
        print(ex)
        return False


if __name__ == "__main__":
    # pdf_path = r'E:\valid_file\152S43W103ZV6E.pdf'
    # pdf_path = r'E:\valid_file\4990250210.pdf'
    # pdf_path = r'E:\valid_file\lt8301.pdf'
    pdf_path = r'E:\valid_file\ssm2019.pdf'
    res = is_valid_pdf(pdf_path)
    print(res)
