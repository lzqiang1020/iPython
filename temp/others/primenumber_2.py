# -*- coding: UTF-8 -*-
# @File  :  primenumber_2
# @Time  :  2019/8/12 10:58
# @Author:  liuzhiqiang

import math

primenumber = []
flag = False
count = 0
for x in range(2, 100):
    for i in primenumber:
        if x%i == 0:
            flag = True
            break
        if i >= math.ceil(math.sqrt(x)):
            flag = False
            break

    if not flag:
        print(x)
        primenumber.append(x)
        count += 1

print("Total : {}".format(count))