# -*- coding: UTF-8 -*-
# @File    :  remove_duplicates
# @Author  :  liuzhiqiang
# @Time    :  2019/9/2 17:10


class Solution:
    def removeDuplicates(self, nums):
        # for i in range(len(nums)-1, 0, -1):
        #     if nums[i] == nums[i-1]: nums.pop(i)
        #
        # print(nums)
        # return len(nums)
        slow_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow_index]:
                nums[slow_index+1] = nums[i]
                slow_index += 1

        print(nums)
        return slow_index+1 if nums else 0
test = Solution()
a = test.removeDuplicates([2, 3, 3, 4, 4, 4])
print(a)
