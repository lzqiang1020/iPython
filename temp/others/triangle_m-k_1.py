# -*- coding: UTF-8 -*-
# @File  :  triangle_m-k_1
# @Time  :  2019/8/13 16:25
# @Author:  liuzhiqiang

m = 5
k = 4
triangle = []
for i in range(m):
    row = [1]
    triangle.append(row)
    if i == 0:
        continue

    for j in range(1, i):
        row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)
    # triangle.append(row)

print(triangle)
print("-"*50)
print(triangle[m-1][k-1])