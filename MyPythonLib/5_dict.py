# -*- coding: utf-8 -*-


def dict_test():
    for x, y in zip(range(1, 25), range(20, 40)):
        print(x, y)


def dict_test2():
    dict1 = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 1, 'b': 2, 'c': 3}
    ]

    dict2 = [
        {'a': 1, 'b': 2, 'd': 4},
        {'a': 1, 'b': 2, 'd': 4},
        {'a': 1, 'b': 2, 'd': 4}
    ]

    new_dict = []
    for x, y in zip(dict1, dict2):
        temp_dict = {}
        for i, j in zip(x, y):
            # print(x[i], y[j])
            if i == j:
                temp_dict[i] = x[i] + y[j]
            else:
                temp_dict[i] = x[i]
                temp_dict[j] = y[j]

        new_dict.append(temp_dict)

    print(new_dict)
