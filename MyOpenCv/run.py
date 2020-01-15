# -*- coding: utf-8 -*-


# import numpy as np
import cv2

# opencv 学习开始
# print(cv2.__version__)


def hello_world():
    filepath = 'test.jpg'
    img = cv2.imread(filepath)
    cv2.namedWindow('Image')
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


hello_world()
