# -*- coding: utf-8 -*-


import cv2


class ImageFace(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.img = None

    def get_image(self):
        self.img = cv2.imread(self.file_path)

    def image_handler(self):
        self.get_image()
        # 转为灰度图
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # OpenCV人脸识别分类器  使用训练分类器查找人脸
        classifier = cv2.CascadeClassifier(
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_eye.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_frontalcatface.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_frontalcatface_extended.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_frontalface_alt.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_frontalface_alt_tree.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_frontalface_alt2.xml"
            r"E:\GitHub\opencv\data\haarcascades\haarcascade_frontalface_default.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_fullbody.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_lefteye_2splits.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_licence_plate_rus_16stages.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_lowerbody.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_profileface.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_righteye_2splits.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_russian_plate_number.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_smile.xml"
            # r"E:\GitHub\opencv\data\haarcascades\haarcascade_upperbody.xml"
        )

        color = (0, 255, 0)

        # 调用识别人脸
        faceRects = classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

        # 大于0则检测到人脸
        if len(faceRects):
            for faceRect in faceRects:
                # 单独框出每一张人脸
                x, y, w, h = faceRect
                # 框出人脸
                cv2.rectangle(self.img, (x, y), (x + h, y + w), color, 2)
                # cv2.rectangle(self.img, (x, y), (x + w, y + w), color, 1)

                # 左眼
                cv2.circle(self.img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8), color)
                # 右眼
                cv2.circle(self.img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8), color)
                # 嘴巴
                cv2.rectangle(self.img, (x + 3 * w // 8, y + 3 * h // 4), (x + 5 * w // 8, y + 7 * h // 8), color)

    def show(self):
        self.image_handler()
        cv2.imshow('Image', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


filepath = 'test7.jpg'
face = ImageFace(filepath)
face.show()
