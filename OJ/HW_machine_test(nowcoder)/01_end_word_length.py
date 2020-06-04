# -*- coding: UTF-8 -*-
# @File  :  str_count
# @Time  :  2019/9/12 11:56
# @Author:  liuzhiqiang

"""
题目描述
计算字符串最后一个单词的长度，单词以空格隔开。
输入描述:
一行字符串，非空，长度小于5000。

输出描述:
整数N，最后一个单词的长度。

示例1
输入
复制
hello world
输出
复制
5
"""
# strs = input()
# character = input()
# count = 0
#
# for item in strs:
#     if character == item:
#         count += 1
#
# print(count)

a = input()
if ' ' not in a:
    print(len(a))
else:
    sp = a.split(' ')
    print(len(sp[-1]))