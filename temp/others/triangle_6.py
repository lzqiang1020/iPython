# -*- coding: UTF-8 -*-
# @File  :  triangle_6
# @Time  :  2019/8/12 15:41
# @Author:  liuzhiqiang

triangle = []
n = 6

for i in range(n):
    row = [1]*(i+1)
    triangle.append(row)
    if i == 0:
        continue

    for j in range(1, i//2+1):
        val = triangle[i-1][j-1] + triangle[i-1][j]
        row[j] = val
        if i != 2j:
            row[-j-1] = val
print(triangle)