# -*- coding: UTF-8 -*-
# @File  :  triangle_5
# @Time  :  2019/8/12 15:12
# @Author:  liuzhiqiang

"""计算前半部分"""
triangle = []
n = 6
for i in range(n):
    row = [1]
    for k in range(i):
        row.append(1) if k == i-1 else row.append(0)
    triangle.append(row)
    if i == 0:
        continue

    for j in range(1, i//2+1):
        val = triangle[i-1][j-1] + triangle[i-1][j]
        row[j] = val
        if j != i-j:
            row[-j-1] = val
print(triangle)