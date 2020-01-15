# -*- coding: utf-8 -*-


import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont


# 中文乱码处理
def cv2_img_add_text(img, text, left, top, text_color=(0, 255, 0), text_size=20):
    """
    img = cv2_img_add_text(img, "大家好...", 140, 60, (255, 255, 0), 20)
    :param img: OpenCV类型图片
    :param text: 添加到图片的文本
    :param left: 左侧位置
    :param top: 顶部位置
    :param text_color: rgb()颜色值
    :param text_size: 字体大小
    :return:
    """
    # 判断是否OpenCV图片类型
    if isinstance(img, numpy.ndarray):
        # OpenCV图片转换为PIL图片格式
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    else:
        # 将图片转为OpenCV图片类型

    # 使用PIL绘制文字
    draw = ImageDraw.Draw(img)
    font_text = ImageFont.truetype("font/simsun.ttc", text_size, encoding="utf-8")
    draw.text((left, top), text, text_color, font=font_text)

    # 使用PIL绘制文字
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)

