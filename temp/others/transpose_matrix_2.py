# -*- coding: UTF-8 -*-
# @File  :  transpose_matrix_2
# @Time  :  2019/8/13 23:14
# @Author:  liuzhiqiang

"""
#定义一个方阵
#1 2 3          1 4
#4 5 6   ==>>   2 5
#               3 6
"""
import datetime

matrix = [[1, 2, 3], [4, 5, 6]]
tm = []
for row in matrix:
    for i, col in enumerate(row):
        if len(tm) < i + 1:
            tm.append([])
        tm[i].append(col)
print(matrix)
print(tm)