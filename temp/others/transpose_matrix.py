# -*- coding: UTF-8 -*-
# @File  :  transpose_matrix
# @Time  :  2019/8/13 22:51
# @Author:  liuzhiqiang

"""
#定义一个方阵
#1 2 3          1 4 7
#4 5 6   ==>>   2 5 8
#7 8 9          3 6 9
"""

matrix = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
print(matrix)

for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)