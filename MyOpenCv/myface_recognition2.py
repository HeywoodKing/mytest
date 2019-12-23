import face_recognition
from PIL import Image, ImageDraw
import numpy as np


# 人脸标注
def draws():
    kobe_image = face_recognition.load_image_file("kobe.jpg")
    kobe_face_encoding = face_recognition.face_encodings(kobe_image)[0]

    jordan_image = face_recognition.load_image_file("jordan.jpeg")
    jordan_face_encoding = face_recognition.face_encodings(jordan_image)[0]

    known_face_encodings = [
        kobe_face_encoding,
        jordan_face_encoding
    ]
    known_face_names = [
        "Kobe",
        "Jordan"
    ]

    unknown_image = face_recognition.load_image_file("two_people.jpeg")

    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    pil_image = Image.fromarray(unknown_image)
    draw = ImageDraw.Draw(pil_image)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    del draw


    pil_image.show()
    pil_image.save("image_with_boxes.jpg")


# 给人脸美妆
def draw_face():
    # 将人脸中的面部所有特征识别到一个列表中
    image = face_recognition.load_image_file("bogute.jpeg")
    face_landmarks_list = face_recognition.face_landmarks(image)
    # 遍历列表中的元素，修改眉毛
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    给人脸涂口红
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # 增加眼线
    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), wid=6)


if __name__ == '__main__':
    draws()
