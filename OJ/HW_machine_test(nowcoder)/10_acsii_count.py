# -*- coding: UTF-8 -*-
# @File        :  acsii_count
# @CreateTime  :  2019/9/19 10:04
# @Author      :  liuzhiqiang

"""
题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。

输入描述:
输入N个字符，字符在ACSII码范围内。

输出描述:
输出范围在(0~127)字符的个数。

示例1
输入
abc
输出
3
"""

def acsii_count(s):
    ss = str()
    for i in s:
        if ord(i) < 127 and i not in ss:
            ss += i
    print(len(ss))

s = input()
acsii_count(s)