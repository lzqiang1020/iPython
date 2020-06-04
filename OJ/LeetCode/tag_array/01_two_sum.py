# -*- coding: UTF-8 -*-
# @File        :  01_two_sum
# @CreateTime  :  2019/10/12 17:58
# @Author      :  liuzhiqiang

def two_sum(nums, target):
    """

    :param nums:
    :param target:
    :return:
    """
    nums_dict = {}
    for k, v in enumerate(nums):
        if target-v in nums and k != nums.index(target-v):
            return [k, nums.index(target-v)]

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))