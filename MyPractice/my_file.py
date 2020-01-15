# -*- coding: utf-8 -*-


# f = open('test.txt')
# print(f.read())
# f.close()

with open('test.txt', 'r+', encoding='utf-8') as f:
    f.write('aaaaa')
    # f.writelines(['123', 'safsdf', '234324'])
    # content = f.read()
    # print(content)
    while True:
        content = f.readline()
        if content:
            print(content)
