import cv2


def main():
    kobe_image = face_recognition.load_image_file("kobe.jpg")  # 已知科比照片
    jordan_image = face_recognition.load_image_file("jordan.jpeg")  # 已知乔丹照片
    unknown_image = face_recognition.load_image_file("unkown.jpeg")  # 未知照片

    kobe_face_encoding = face_recognition.face_encodings(kobe_image)[0]
    jordan_face_encoding = face_recognition.face_encodings(jordan_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

    known_faces = [
        kobe_face_encoding,
        jordan_face_encoding
    ]
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)  # 识别结果列表
    print("这张未知照片是科比吗? {}".format(results[0]))
    print("这张未知照片是乔丹吗? {}".format(results[1]))

    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)


if __name__ == '__main__':
    main()
