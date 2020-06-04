# -*- coding: UTF-8 -*-
# @File  :  number_count
# @Time  :  2019/8/14 0:03
# @Author:  liuzhiqiang

import random

nums = []
for _ in range(10):
    nums.append(random.randint(1, 20))
print("Origin number: {}".format(nums))

length = len(nums)
same_nums = []
diff_nums = []
states = [0]*length

for i in range(length):
    flag = False
    if states[i] == 1:
        continue

    for j in range(i+1,length):
        if states[j] == 1:
            continue
        if nums[i] == nums[j]:
            states[j] = 1
            flag = True

    if not flag:
        diff_nums.append(nums[i])
    else:
        same_nums.append(nums[i])
        states[i] = 1

print("Same numbers = {}, Counter = {}".format(same_nums, len(same_nums)))
print("Diff numbers = {}, Counter = {}".format(diff_nums, len(diff_nums)))
print(list(zip(states, nums)))