# -*- coding: UTF-8 -*-
# @File  :  std_lib_datetime
# @Time  :  2019/8/15 18:16
# @Author:  liuzhiqiang

# % % time
# nums = [2, 7, 11, 15]
# target = 9
nums = [2, 2, 3, 3, 4, 4]
target = 6

_dict = {}
for i, m in enumerate(nums):
    _dict[m] = i
    print("m={}, i={}".format(m, i))

for i, m in enumerate(nums):
    j = _dict.get(target - m)
    if j is not None and i != j:
        print([i, j])
print(_dict)