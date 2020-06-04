# -*- coding: UTF-8 -*-
# @File        :  change_decimal
# @CreateTime  :  2019/9/17 18:05
# @Author      :  liuzhiqiang

"""
题目描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）

输入描述:
输入一个十六进制的数值字符串。

输出描述:
输出该数值的十进制字符串。

示例1
输入
0xA
输出
10
"""

while True:
    try:
        hex_str = input()
        print(int(hex_str, 16))
    except:
        break
