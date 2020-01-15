# -*- coding utf-8 -*-

# def trim(s):
#     print("s:", s, len(s), s[-1:])
#     if len(s) > 0:
#         f = s[0:1]
#         print("f:", f)
#         e = s[-1:]
#         print("e:", e)
#
#         if f.isspace():
#             s = s[1:]
#
#         if e.isspace():
#             return s[0:len(s) - 1]
#         else:
#             return s



def trimLeft(s):
    r = s
    index = 0
    for i in s:
        if i.isspace():
            pass
        else:
            r = s[index:]
            break

        index += 1

    return r


def trim(s):
    r = trimLeft(s)
    r = trimLeft(r[::-1])
    return  r[::-1]

# print(trim(' asf ab BCD'))
print(trim('  abcd   dfsadfd              '))


