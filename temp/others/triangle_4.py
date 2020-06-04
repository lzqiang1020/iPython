# -*- coding: UTF-8 -*-
# @File  :  triangle_4
# @Time  :  2019/8/12 15:06
# @Author:  liuzhiqiang

"""for method"""
n = 6
oldline = []
newline = [1]
print(newline)

for i in range(1, n):
    oldline = newline.copy()
    oldline.append(0)
    newline.clear()
    for j in range(i+1):
        newline.append(oldline[j-1] + oldline[j])
    print(newline)