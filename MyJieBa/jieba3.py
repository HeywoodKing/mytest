import os
import sys
import jieba

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(BASE_DIR)


def main():
    filename = r'D:\\Flack\\Project\\Github\\mytest\\三国演义.txt'
    txt = open(filename, "r", encoding='utf-8').read()
    words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
    counts = {}     # 通过键值对的形式存储词语及其出现的次数

    for word in words:
        if  len(word) == 1:    # 单个词语不计算在内
            continue
        else:
            counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1
            
    items = list(counts.items())                    # 将键值对转换成列表
    items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

    # 利用jieba库统计三国演义中人物的出场次数取前15名
    for i in range(15):
        word, count = items[i]
        print("{0:<5}{1:>5}".format(word, count))


if __name__ == "__main__":
    main()
