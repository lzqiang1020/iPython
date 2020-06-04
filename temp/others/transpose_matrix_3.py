# -*- coding: UTF-8 -*-
# @File  :  transpose_matrix_3
# @Time  :  2019/8/13 23:51
# @Author:  liuzhiqiang

matrix = [[1, 2, 3], [4, 5, 6]]
tm = [[0 for col in range(len(matrix))] for row in range(len(matrix[0]))]   #[[0, 0], [0, 0], [0, 0]]

for i, row in enumerate(tm):
    for j, col in enumerate(row):
        tm[i][j] = matrix[j][i]

print(matrix)
print(tm)