# -*- coding: UTF-8 -*-
# @File        :  merge_table_dict
# @CreateTime  :  2019/9/17 22:50
# @Author      :  liuzhiqiang

"""
题目描述
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）

示例1
输入
================
4
0 1
0 2
1 2
3 4
================
输出
0 3
1 2
3 4
"""

# number = int(input())
# array = {}
# for i in range(number):
#     tm = input().split()
#     if int(tm[0]) in array:
#         array[int(tm[0])] += int(tm[1])
#     else:
#         array[int(tm[0])] = int(tm[1])
#
# sorted(array)
# for k, v in array.items():
#     print(k, v)

while True:
    try:
        num = int(input())
        output = {}
        for i in range(num):
            pair = input().split(' ')
            output[int(pair[0])] = output.setdefault(int(pair[0]), 0) + int(pair[1])

        output_list = sorted(output.keys())
        print(output_list)
        for key in output_list:
            print(key, output[key])
    except:
        break
