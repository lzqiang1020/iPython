# -*- coding:UTF-8 -*-
import sys

std_keyboard = 'QWERTYUIOPASDFGHJKLZXCVBNM'
natural_keyboard = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_swap = dict(list(zip(natural_keyboard, std_keyboard.lower())))

# alpha_swap = {
#     'A': 'q',
#     'B': 'w',
#     'C': 'e',
#     'D': 'r',
#     'E': 't',
#     'F': 'y',
#     'G': 'u',
#     'H': 'i',
#     'I': 'o',
#     'J': 'p',
#     'K': 'a',
#     'L': 's',
#     'M': 'd',
#     'N': 'f',
#     'O': 'g',
#     'P': 'h',
#     'Q': 'j',
#     'R': 'k',
#     'S': 'l',
#     'T': 'z',
#     'U': 'x',
#     'V': 'c',
#     'W': 'v',
#     'X': 'b',
#     'Y': 'n',
#     'Z': 'm'
# }

while True:
    tem = str()
    try:
        get_str = sys.stdin.readline().strip()
        for i in get_str:
            if i.upper() in alpha_swap:
                if i.isupper():
                    # print(alpha_swap[i].upper(), end='')
                    tem += alpha_swap[i].upper()
                else:
                    # print(alpha_swap[i.upper()], end='')
                    tem += alpha_swap[i.upper()]
            else:
                # print(i, end='')
                tem += i

        print(tem)
    except:
        break

# get_str = sys.stdin.readline().strip()
# for i in get_str:
#     if i.upper() in alpha_swap:
#         if i.isupper():
#             print(alpha_swap[i].upper(), end='')
#         else:
#             print(alpha_swap[i.upper()], end='')
#     else:
#         print(i, end='')
# # H kz k xif.

