# -*- coding: utf-8 -*-
import random
import copy


# def solution(A, B, C):
#     # write your code in Python 3.6
#     if A == 0 and B == 1 and C >= 4:
#         return 'ccbcc'
#     else:
#         high = max(A, B, C)
#         la = ['a' for _ in range(high)]
#         la_t = copy.deepcopy(la)
#         s = ''.join(la)
#
#         lb = ['b' for _ in range(B)]
#         lc = ['c' for _ in range(C)]
#
#         pos = B + C
#
#         while is_continue_letter(s):
#             la_t.clear()
#             la_t = copy.deepcopy(la)
#             for i in range(len(la)):
#                 la_t.insert(i, lb[0])
#                 for j in range(i + 1, len(la)):
#                     la_t.insert(j, lc[0])
#                     s = ''.join(la_t)
#                     if is_continue_letter(s):
#                         la_t.clear()
#                         la_t = copy.deepcopy(la)
#                         pass
#                     else:
#                         print(s)


        #
        # L = la + lb + lc
        # while L:
        #     i = random.randint(0, len(L) - 1)
        #     # print(s, s[-1:], s[-2:-1])
        #     print(i, L)
        #     # print(L[i])
        #     if s[-1:] == L[i] and s[-2:-1] == L[i]:
        #         print(0, s, L[i])
        #     elif len(s) > 0 and (s[0] == 'b' or s[0] == 'c'):
        #         pass
        #     else:
        #         s += L[i]
        #         del L[i]
        #     # print(s)

        # return s


# def is_continue_letter(s):
#     for i in range(len(s) - 3):
#         if s[i] == s[i+1] and s[i+1] == s[i+2]:
#             return True
#
#     return False


def solution(A, B, C):
    # write your code in Python 3.6
    if A == 0 and B == 1 and C >= 4:
        return 'ccbcc'
    else:
        # high = max(A, B, C)

        la = ['a' for _ in range(A)]
        lb = ['b' for _ in range(B)]
        lc = ['c' for _ in range(C)]
        m, n, l = int(A/2),int(B/2),int(C/2)
        group_a = ['A+' for _ in range(m)]
        if A % 2 != 0:
            group_a.append('A-')

        group_b = ['B+' for _ in range(n)]
        if B % 2 != 0:
            group_b.append('B-')

        group_c = ['C+' for _ in range(l)]
        if C % 2 != 0:
            group_c.append('C-')

        group = [group_a, group_b, group_c]
        # print(group)

        group_pos = [A, B, C]

        group_index = group_pos.index(max(group_pos))
        # print('group_index:', group_index)

        group_max = copy.deepcopy(group[group_index])
        del group[group_index]

        print(group)

        res = []
        group_a_t = []
        group_a_t = copy.deepcopy(group_max)
        for i in range(len(group_max) + 1):
            # group 元素前后位置调换
            if len(group[0]) > len(group[1]):
                for j in range(len(group[0])):
                    group_a_t.insert(i, group[0][j])
                    for k in range(len(group[1])):
                        group_a_t.insert(i + 2, group[1][k])
                        # print(group_a_t)
            else:
                for j in range(len(group[1])):
                    group_a_t.insert(i, group[1][j])
                    for k in range(len(group[0])):
                        group_a_t.insert(i + 2, group[0][k])
                        # print(group_a_t)

            # 判断是否有连接到一起的
            b_res = False
            for p in range(len(group_a_t) - 1):
                if group_a_t[p] == group_a_t[p + 1]:
                    b_res = True
                    break
                # if group_a_t[p][0] == group_a_t[p + 1][0]:
                #     b_res = True
                #     break

            # print(group_a_t)
            if b_res is False:
                res.append(copy.deepcopy(group_a_t))

            print('res:', res)
            group_a_t.clear()
            group_a_t = copy.deepcopy(group_max)

        s = ''
        for r in range(len(res)):
            # print(res[r])
            t = ''.join(res[r])
            s += t + ','

        s = s.replace('A+', 'aa').replace('A-', 'a')\
            .replace('B+', 'bb').replace('B-', 'b')\
            .replace('C+', 'cc').replace('C-', 'c')
        return s.rstrip(',')


# a, b, c = 6, 1, 1
a, b, c = 1, 3, 3
res = solution(a, b, c)
print(res)
