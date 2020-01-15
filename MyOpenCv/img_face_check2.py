# -*- coding: utf-8 -*-


import cv2
import dlib
import img_add_text


class ImageFace(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.img = None

    def _get_image(self):
        self.img = cv2.imread(self.file_path)

    def _image_handler(self):
        self._get_image()
        # 转为灰度图
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # 使用特征提取器get_frontal_face_detector
        detector = dlib.get_frontal_face_detector()

        # dlib的68点模型，使用作者训练好的特征预测器
        predictor = dlib.shape_predictor(
            r"E:\Python\opencv\shape_predictor_68_face_landmarks.dat"
        )

        color = (0, 255, 0)

        # 调用识别人脸
        dets = detector(gray, 1)
        for face in dets:
            # 寻找人脸的68个标定点
            shape = predictor(self.img, face)
            # 遍历所有点，打印出其坐标，并圈出来
            for pt in shape.parts():
                pt_pos = (pt.x, pt.y)
                cv2.circle(self.img, pt_pos, 2, color, 1)

    def show(self):
        self._image_handler()
        self.img = img_add_text.cv2_img_add_text(self.img, "大家好...", 140, 60)
        cv2.imshow('Image', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


filepath = 'test7.jpg'
face = ImageFace(filepath)
face.show()


