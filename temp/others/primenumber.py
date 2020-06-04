# -*- coding: UTF-8 -*-
# @File  :  primenumber
# @Time  :  2019/8/12 10:45
# @Author:  liuzhiqiang

import math

n = 100
count = 0
for x in range(2, n):
    for i in range(2, math.ceil(math.sqrt(x))):
        if x % i == 0:
            break
    else:
        print(x)
        count += 1
print("Total : {}".format(count))