# -*- coding: UTF-8 -*-
# @File        :  125_is_palindrome
# @CreateTime  :  2019/10/15 10:41
# @Author      :  liuzhiqiang

"""
125 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""


def is_palindrome(s):
    """

    :param s:
    :return: bool
    """
    s = s.strip().lower()
    length = len(s)

    if length <= 1:
        return True

    left = 0
    right = length -1
    flag = True    # 判断前假定是回文数
    while left < right:   # 如果正向索引大于等于反向索引时，则停止遍历
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            flag = False
            break

    return flag


def is_palindrome_1(s):
    if not s:
        return True

    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


s = "\"af6??6f\"32=a"
s = "A man, a plan, a canal=> Panama"
print(is_palindrome(s))
