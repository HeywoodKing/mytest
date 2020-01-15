# -*- coding: utf-8 -*-


import cv2
import dlib
import img_add_text


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

        # 使用特征提取器get_frontal_face_detector
        detector = dlib.get_frontal_face_detector()
        # dlib的68点模型，使用作者训练好的特征预测器
        predictor = dlib.shape_predictor(
            r"E:\Python\opencv\shape_predictor_68_face_landmarks.dat"
        )

        color = (0, 255, 0)

        # 调用识别人脸
        dets = detector(gray, 1)

        if dets:
            for face in dets:
                left = face.left()
                top = face.top()
                right = face.right()
                bottom = face.bottom()

                # 寻找人脸的68个标定点
                shape = predictor(self.img, face)
                # 遍历所有点，打印出其坐标，并圈出来
                # for i in range(68):
                #     cv2.circle(self.img, (shape.part(i).x, shape.part(i).y), 5, color, -1, 8)
                #     cv2.putText(self.img, str(i), (shape.part(i).x, shape.part(i).y), cv2.FONT_HERSHEY_SIMPLEX,
                #                 0.5, (255, 255, 255))

                for pt in shape.parts():
                    pt_pos = (pt.x, pt.y)
                    # cv2.circle(self.img, pt_pos, 2, color, 1)
                    cv2.circle(self.img, pt_pos, 5, color, -1, 8)
                    cv2.putText(self.img, str(i), (shape.part(i).x, shape.part(i).y), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (255, 255, 255))

                x, y, w, h = left, top, right - left, bottom - top

                # 框出人脸
                cv2.rectangle(self.img, (left, top), (right, bottom), color, 2)

                text = '渣渣辉'
                img_add_text.cv2_img_add_text(self.img, text, (left / 2 - len(text) / 2), top - 20)

                # if self.is_eye:
                #     # 左眼
                #     cv2.circle(self.img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8), color)
                #     # 右眼
                #     cv2.circle(self.img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8), color)
                #
                # if self.is_nose:
                #     pass
                #
                # if self.is_mouth:
                #     # 嘴巴
                #     cv2.rectangle(self.img, (x + 3 * w // 8, y + 3 * h // 4), (x + 5 * w // 8, y + 7 * h // 8), color)

            self._show()

    def _show(self):
        cv2.imshow('Image', self.img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


face = VideoFace()
face.get_video_face_check()


