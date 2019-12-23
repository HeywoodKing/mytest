
from PIL import Image, ImageDraw


def get_gray():
    im = Image.open('vc.jpg')
    im.show()

    gray = im.convert('L')
    gray.show()
    gray.save('gray.jpg')


# 二值化处理
def get_table(threshold=115):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table


# 图片进行降噪处理
def get_pixel(image, x, y, G, N):
    # 获取像素值
    L = image.getpixel((x, y))

    # 与阈值比较
    if L > G:
        L = True
    else:
        L = False

    nearDots = 0

    if L == (image.getpixel((x - 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y + 1)) > G):
        nearDots += 1

    if nearDots < N:
        return image.getpixel((x, y - 1))
    else:
        return None


# 降噪
# Z: 降噪次数
def clear_noise(image, G, N, Z):
    draw = ImageDraw.Draw(image)

    for i in range(0, Z):
        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                color = get_pixel(image, x, y, G, N)
                if color is not None:
                    draw.point((x, y), color)


def main():
    get_gray()
    # 打开灰度化图片并进行二值处理
    binary = Image.open('gray.jpg').point(get_table(120), "1")
    # 展示二值化图片
    binary.show()
    # 保存二值化图片
    binary.save('binary.png')

    # 打开二值化图片
    b_im = Image.open('binary.png')
    # 将二值化图片降噪
    # 设置的二值化阈值为50，降噪率为4，降噪次数为4
    clear_noise(b_im, 50, 4, 4)
    # 展示降噪后的图片
    b_im.show()
    # 保存降噪后的图片
    b_im.save('result.png')

    # 我们还可以通过 PIL 库的 ImageEnhance 和 ImageFilter 对图片做其他处理，
    # 例如增加对比度、亮度、锐化等，最终的目的都是去除图片的噪点，是图片更容易辨别


if __name__ == '__main__':
    main()
