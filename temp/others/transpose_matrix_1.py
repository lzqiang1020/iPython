# -*- coding: UTF-8 -*-
# @File  :  transpose_matrix_1
# @Time  :  2019/8/13 23:07
# @Author:  liuzhiqiang

matrix = [[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12], [1, 2, 3, 4]]
length = len(matrix)
for i in range(length):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)