# -*- coding: UTF-8 -*-
# @File  :  remove_element
# @Time  :  2019/9/5 10:57
# @Author:  liuzhiqiang

def remove_element(nums, val):
    """
    给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
    :param nums:
    :param val:
    :return:
    """
    slow_index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[slow_index] = nums[i]
            slow_index += 1
    # print(nums[:slow_index])
    return slow_index


print(remove_element([0,1,2,2,3,0,4,2], 2))