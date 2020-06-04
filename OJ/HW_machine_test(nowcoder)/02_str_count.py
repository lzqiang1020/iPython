# -*- coding: UTF-8 -*-
# @File  :  str_count
# @Time  :  2019/9/17 17:35
# @Author:  liuzhiqiang

"""
题目描述写出一个程序，接受一个有字母和数字以及空格组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

输入描述输入一个有字母和数字以及空格组成的字符串，和一个字符。

输出描述输出输入字符串中含有该字符的个数。

示例1输入：
ABCDEF
A
输出：1
"""

strs = input().lower()
character = input().lower()

print(strs.count(character))
