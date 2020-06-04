# -*- coding: UTF-8 -*-
# @File  :  triangle_m-k_2
# @Time  :  2019/8/13 22:33
# @Author:  liuzhiqiang

m = 9
k = 5

# c(n, r) = n!/(r!(n-r)!)
n = m - 1
r = k - 1
d = n - r
targets = []
factorial = 1
for i in range(1, n+1):
    factorial *= i
    if i == r:
        targets.append(factorial)
    if i == d:
        targets.append(factorial)
    if i == n:
        targets.append(factorial)

print(targets[2]//(targets[0]*targets[1]))