# -*- coding: UTF-8 -*-
# @File  :  strs_split
# @Time  :  2019/9/17 16:53
# @Author:  liuzhiqiang

"""
    题目描述
    •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
    •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
    输入描述:
    连续输入字符串(输入2次,每个字符串长度小于100)

    输出描述:
    输出到长度为8的新字符串数组

    示例1
    输入：
    abc
    123456789
    输出：
    abc00000
    12345678
    90000000
"""

while True:
    try:
        str1 = input()
        if str1:
            length1 = len(str1)
            if length1 % 8 == 0:
                for i in range(0, length1, 8):
                    print(str1[i:i+8])
            else:
                length1_ = (length1 // 8) * 8 + 8
                str1 += '0' * (length1_ - length1)
                for i in range(0, length1_, 8):
                    print(str1[i:i+8])
        else:
            print(str1)

        str2 = input()
        if str2:
            length2 = len(str2)
            if length2 % 8 == 0:
                for i in range(0, length2, 8):
                    print(str2[i:i+8])
            else:
                length2_ = (length2 // 8) * 8 + 8
                str2 += '0' * (length2_ - length2)
                for i in range(0, length2_, 8):
                    print(str2[i:i+8])
        else:
            print(str2)
    except:
        break
