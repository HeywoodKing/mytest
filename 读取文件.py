# coding = utf -8
import os
import xlwt
import sys


print(sys.path[0])

file_path = r'\\192.168.1.169\data2\PDF\jiagen\单个下载.xls'
f = xlwt.Workbook(encoding='utf-8', )
sheet = f.add_sheet('sheet1')
pathdir = os.listdir(sys.path[0])

i = 0
for s in pathdir:
    sheet.write(i, 0, s)
    i = i + 1

print(file_path)
print(i)
f.save(file_path)
