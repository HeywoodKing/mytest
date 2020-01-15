# -*- coding: utf-8 -*-


import cv2


# 获取摄像头
def get_video():
    # 获取摄像头0表示第一个摄像头
    cap = cv2.VideoCapture(0)
    while 1:  # 逐帧显示
        ret, img = cap.read()

        discern(img)
        # cv2.imshow('Image', img)

        # 使用了“ & ”位元算法，含义是获取用户输入的最后一个字符的ASCII码，如果输入的是“q”，则跳出循环。
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break

    # 释放摄像头
    cap.release()
    # 释放窗口资源
    cv2.destroyAllWindows()


# 视频的人脸识别
def discern(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
    if len(faceRects):
        for facRect in faceRects:
            x, y, w, h = facRect
            # 框出人脸
            cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)

    cv2.imshow('Image', img)


get_video()

