# -*- coding: UTF-8 -*-
# @File        :  sort_str
# @CreateTime  :  2019/9/19 11:15
# @Author      :  liuzhiqiang

"""
题目描述
给定n个字符串，请对n个字符串按照字典序排列。
输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。
示例1
输入
9
cap
to
cat
card
two
too
up
boat
boot
输出
boat
boot
cap
card
cat
to
too
two
up
"""

while True:
    try:
        number = int(input())
        get_strs = []
        for i in range(number):
            get_strs.append(input())
        get_strs.sort()
        for i in get_strs:
            print(i)
    except:
        break
