# -*- coding: UTF-8 -*-
# @File  :  sort_and_print
# @Time  :  2019/8/10 10:00
# @Author:  liuzhiqiang

"""
#依次接收用户输入的3个数，排序后打印
"""

nums = []
for i in range(3):
    nums.append(int(input("请输入第 {} 个数: ".format(i+1))))

if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        i3 = nums[0]
        if nums[1] > nums[2]:
            i2 = nums[1]
            i1 = nums[2]
        else:
            i2 = nums[2]
            i1 = nums[1]
    else:
        i1 = nums[1]
        i2 = nums[0]
        i3 = nums[2]
else:   #0<1
    if nums[0] > nums[2]:
        i1 = nums[2]
        i2 = nums[0]
        i3 = nums[1]
    else:   #0<2
        if nums[1]<nums[2]:
            i1 = nums[2]
            i2 = nums[1]
            i3 = nums[0]
        else:
            i1 = nums[2]
            i2 = nums[1]
            i3 = nums[0]

print(i1, i2, i3)
