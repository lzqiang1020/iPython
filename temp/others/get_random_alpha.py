# -*- coding: UTF-8 -*-
# @File    :  get_random_alpha
# @Author  :  liuzhiqiang
# @Time    :  2019/8/27 17:13


import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

words = []
for _ in range(100):
    words.append(''.join(random.sample(alphabet, 2)))

d = {}
for x in words:
    d[x] = d.get(x, 0) +1
print(d)
print("="*100)
d1 = sorted(d.items(), reverse=True)
print(d1)