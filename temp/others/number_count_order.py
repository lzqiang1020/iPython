# -*- coding: UTF-8 -*-
# @File  :  number_count_order
# @Time  :  2019/8/10 17:52
# @Author:  liuzhiqiang

nums = []
while len(nums) < 5:
    num = input("Please input a number: ").strip().lstrip('0')
    if not num.isdigit():
        continue
    print("The length of {} is {}".format(num, len(num)))
    nums.append(int(num))
print(nums)

lst = nums.copy()
lst.sort()    #就地修改
print(lst)

#冒泡法
for i in range(len(nums)):
    flag = False
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            flag = True
    if not flag:
        break
print(nums)


