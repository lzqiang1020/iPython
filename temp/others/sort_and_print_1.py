# -*- coding: UTF-8 -*-
# @File  :  sort_and_print_1
# @Time  :  2019/8/10 14:41
# @Author:  liuzhiqiang

"""
#依次接收用户输入的3个数，排序后打印
"""

nums = []
out = None
for  i in range(3):
    nums.append(int(input("\r请输入第 {} 个数: ".format(i+1))))

if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        if nums[1] > nums[2]:
            out = [2, 1, 0]
        else:
            out = [1, 2, 0]
    else:
        out = [1, 0, 2]
else:
    if nums[0] > nums[2]:
        out = [2, 0, 1]
    else:
        if nums[1] > nums[2]:
            out = [0, 2, 1]
        else:
            out = [0, 1, 2]
out.reverse()    #将序列倒序
for i in out:
    print(nums[i], end=', ')

print(i1, i2, i3)
