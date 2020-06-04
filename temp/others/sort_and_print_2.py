# -*- coding: UTF-8 -*-
# @File  :  sort_and_print_2
# @Time  :  2019/8/10 14:41
# @Author:  liuzhiqiang

"""
#依次接收用户输入的3个数，排序后打印
"""

nums = []
out = None
for i in range(3):
    nums.append(int(input("{}: ".format(i))))

while True:
    cur = min(nums)
    print(cur)
    nums.remove(cur)
    if len(nums) ==1:
        print(nums[0])
        break

# nums.sort()
# print(nums)
