# -*- coding: UTF-8 -*-
# @File  :  primenumber_1
# @Time  :  2019/8/12 10:52
# @Author:  liuzhiqiang

import math

n  = 100
count = 0
primenumber = []
for x in range(2, n):
    for i in primenumber:
        if x%i == 0:
            break
    else:
        print(x)
        primenumber.append(x)
        count += 1
print("Total : {}".format(count))