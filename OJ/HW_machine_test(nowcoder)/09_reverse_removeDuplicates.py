# -*- coding: UTF-8 -*-
# @File        :  reverse_removeDuplicates
# @CreateTime  :  2019/9/18 10:54
# @Author      :  liuzhiqiang

"""
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

示例1
输入
9876673
输出
37689
"""

# num = input()
# reversed_input = str(reversed(num))
# reversed_output = str()
# for el in reversed_input:
#     if el in reversed_output:
#         continue
#     else:
#         reversed_output += el
#         print(el, end='')
#

while True:
    try:
        num = input()
        # output = num[-1]
        output = str()
        for i in range(len(num)-1, -1, -1):
            if num[i] not in num[i+1:]:
            # if num[i] not in output:    # if num[i] not in num[i:]
                output += num[i]
        print(output)
    except:
        break