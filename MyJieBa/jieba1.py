import jieba


def main():
    # # 精确模式，返回一个可迭代数据类型
    # results = jieba.cut('中华人民共和国是一个伟大的国家')
    # for item in results:
    #     print(item)

    # 全模式，输出文本中所有可能的单词
    # results = jieba.cut('中华人民共和国是一个伟大的国家', cut_all=True)
    # for item in results:
    #     print(item)

    # 搜索引擎模式，适合搜索引擎建立索引的分词结果
    # results = jieba.cut_for_search('中华人民共和国是一个伟大的国家')
    # for item in results:
    #     print(item)
    
    # # 精确模式返回列表
    # res_list = jieba.lcut('中华人民共和国是一个伟大的国家')
    # print(res_list)

    # 全模式，返回列表
    # res_list = jieba.lcut('中华人民共和国是一个伟大的国家', cut_all=True)
    # print(res_list)

    # 搜索引擎模式，返回列表
    res_list = jieba.lcut_for_search('中华人民共和国是一个伟大的国家')
    print(res_list)

    # 向分词词典中增加新词
    # jieba.add_word('你我他')


if __name__ == "__main__":
    main()

