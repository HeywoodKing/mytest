# -*- encoding: utf-8 -*-
"""
@File           : test
@Time           : 2019/12/22
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import os
import tinify

# tinify.url = 'https://tinypng.com/dashboard/api'
tinify.key = 'V6yQTZTK4L35y0T74G5QM0BhfhhglkqR'
path = '/home/flack/图片'


def main():
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            try:
                img_path = os.path.join(dirpath, file)
                print('compressing...' + img_path)
                tinify.from_file(img_path).to_file(img_path)
            except Exception as ex:
                print('{} 压缩失败：{}'.format(file, ex))


if __name__ == '__main__':
    main()
