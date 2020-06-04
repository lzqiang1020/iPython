# -*- coding: UTF-8 -*-
# @File  :  str_str
# @Time  :  2019/9/6 9:30
# @Author:  liuzhiqiang


"""
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。
"""

# str.partition()方法
# def str_str(haystack, needle):
#     """
#     :param haystack:
#     :param needle:
#     :return:
#     """
#     if len(needle):
#         part_arr = haystack.partition(needle)
#     else:
#         return 0
#
#     return len(part_arr[0]) if part_arr[1] else -1


def str_str_1(haystack, needle):
    return haystack.find(needle)


# 暴力匹配算法
def str_str_2(haystack, needle):
    s_len = len(haystack)
    p_len = len(needle)
    i, j = 0, 0
    while i < s_len and j < p_len:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1  # 如果失配，将i回溯到之前i-j+1的位置
            j = 0

    if j == p_len:
        return i - j
    else:
        return -1


print(str_str_1(haystack="501201234pi", needle="n"))
# print(str_str_1(haystack = "aaaaa", needle = "bba"))
