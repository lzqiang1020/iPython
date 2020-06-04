# -*- coding: UTF-8 -*-
# @File        :  reverse_str
# @CreateTime  :  2019/9/19 10:59
# @Author      :  liuzhiqiang

"""
题目描述
写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。例如：
输入描述:输入N个字符

输出描述:
输出该字符串反转后的字符串

示例1
输入
abcd
输出
dcba
"""

get_input = input()
print(get_input[-1:-len(get_input)-1:-1])