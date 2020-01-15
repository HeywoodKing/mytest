# -*- coding: utf-8 -*-


import cv2


# 视频的人脸识别
class VideoFace(object):
    def __init__(self, device_index=0, is_eye=False, is_nose=False, is_mouth=False):
        """
        初始化
        :param device_index: 设备索引，默认0，即第一个设备
        :param is_eye: 是否圈出眼睛
        :param is_nose: 是否圈出鼻子
        :param is_mouth:  是否圈出嘴巴
        """
        self.device_index = device_index
        self.is_eye = is_eye
        self.is_nose = is_nose
        self.is_mouth = is_mouth
        self.img = None

    # 获取摄像头
    def get_video_face_check(self):
        # 获取摄像头0表示第一个摄像头
        cap = cv2.VideoCapture(self.device_index)
        while 1:  # 逐帧显示
            ret, self.img = cap.read()

            self._image_handler()

            # 使用了“ & ”位元算法，含义是获取用户输入的最后一个字符的ASCII码，如果输入的是“q”，则跳出循环。
            if cv2.waitKey(1) & 0XFF == ord('q'):
                break

        # 释放摄像头
        cap.release()
        # 释放窗口资源
        cv2.destroyAllWindows()

    def _image_handler(self):
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
        faceRects = classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))

        # 大于0则检测到人脸
        if len(faceRects):
            for faceRect in faceRects:
                # 单独框出每一张人脸
                x, y, w, h = faceRect
                # 框出人脸
                cv2.rectangle(self.img, (x, y), (x + h, y + w), color, 2)

                if self.is_eye:
                    # 左眼
                    cv2.circle(self.img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8), color)
                    # 右眼
                    cv2.circle(self.img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8), color)

                if self.is_nose:
                    pass

                if self.is_mouth:
                    # 嘴巴
                    cv2.rectangle(self.img, (x + 3 * w // 8, y + 3 * h // 4), (x + 5 * w // 8, y + 7 * h // 8), color)

            self._show()

    def _show(self):
        cv2.imshow('Image', self.img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


face = VideoFace()
face.get_video_face_check()


