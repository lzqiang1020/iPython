# -*- coding: UTF-8 -*-
# @File        :  prime_factor
# @CreateTime  :  2019/9/17 21:18
# @Author      :  liuzhiqiang

"""
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）最后一个数后面也要有空格

输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入
180
输出
2 2 3 3 5
"""

while True:
    try:
        num = int(input())
        while num > 1:
            i = 2
            while True:
                if num % i == 0:
                    print(i, end=' ')
                    num /= i
                    break
                i += 1
    except:
        break
