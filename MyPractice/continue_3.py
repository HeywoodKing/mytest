# -*- coding: utf-8 -*-
from collections import defaultdict


# 查找第一次连续出现3个的字母
def find_3_continue_letter(str):
    for i in range(len(str) - 3):
        if str[i] == str[i+1] and str[i] == str[i+2]:
            return str[i]

    return None


# 查找第一次出现3次的字母
def find_letter_first_3(str):
    dict_res = defaultdict(lambda: 0)
    for char in str:
        dict_res[char] += 1
        if dict_res[char] == 3:
            return char
            # print(char)
            # break

    return None


str = 'aafssfakkfaaffslfaffdddd'
letter1 = find_3_continue_letter(str)
letter2 = find_letter_first_3(str)
print(letter1, letter2)
