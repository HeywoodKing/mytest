import sys
import cv2

image_path = "face.jpg"


# https://github.com/opencv/opencv/tree/master/data/haarcascades?spm=a2c4e.10696291.0.0.300719a4x9vez5


def detect_face():
    # 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
    face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
    # 读取图片
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 探测图片中的人脸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(5, 5),
        # flags=cv2.CV_HAAR_SCALE_IMAGE
    )

    print("发现{0}个人脸!".format(len(faces)))

    for (x, y, w, h) in faces:
        print(x, y, w, h)
        cv2.circle(image, (int((x + x + w) / 2), int((y + y + h) / 2)), int(w / 2), (0, 255, 0), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, "OpenCV", (80, 90), font, 2, (255, 255, 255), 3)

    cv2.imshow("Find faces", image)
    cv2.waitKey(0)


def main():
    detect_face()


if __name__ == '__main__':
    main()
