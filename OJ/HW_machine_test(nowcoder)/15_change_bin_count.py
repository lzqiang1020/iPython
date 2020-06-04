# -*- coding: UTF-8 -*-
# @File        :  change_bin_count
# @CreateTime  :  2019/9/19 17:15
# @Author      :  liuzhiqiang

"""
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
输入描述:
输入一个整数（int类型）
输出描述:
这个数转换成2进制后，输出1的个数
示例1
输入
5
输出
2
"""

while True:
    try:
        num = int(input())
        count = 0
        for i in bin(num):
            if i == '1':
                count += 1
        print(count)
    except:
        break
