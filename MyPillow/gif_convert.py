# -*- encoding: utf-8 -*-
"""
@File           : gif_convert.py
@Time           : 2019/12/31 8:51
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
import random
from PIL import Image, ImageSequence


def main():
    with Image.open('pic.gif') as im:
        frames = None
        if im.is_animated:
            frames = [f.copy() for f in ImageSequence.Iterator(im)]
            # 内置序列表倒序方法
            frames.reverse()

            # 鬼畜打乱gif动画效果
            # random.shuffle(frames)

            # 将倒序后的所有帧图像保存下来
            frames[0].save('pic_reverse.gif', save_all=True, append_images=frames[1:])


if __name__ == '__main__':
    main()
