import cv2


def main():
    image = cv2.imread('test.jpg')
    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x, y, w = 20, 20, 10
    # 画图
    cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)

    #
    face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

    # 探测图片中的人脸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(5, 5),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    print("发现{0}个人脸!".format(len(faces)))

    # 将人脸框出来
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)

    # 显示图像
    cv2.imshow("测试图片", image)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
