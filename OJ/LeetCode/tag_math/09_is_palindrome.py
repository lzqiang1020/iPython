# -*- coding: UTF-8 -*-
# @File  :  is_palindrome
# @Time  :  2019/8/23 9:59
# @Author:  liuzhiqiang

# def isPalindrome(x):
#     if x != 0 and x%10 == 0 or not str(x).isdigit():
#         return False
#
#     x_str = str(x)
#     length = len(x_str)
#     for i in range(length//2):
#         if x_str[i] != x_str[-i-1]:
#             return False
#     else:
#         return True

def isPalindrome(x):
    # return str(x) == str(x)[::-1]
    return str(x)[:x//2] == str(x)[:-x//2:-1]
isPalindrome(1001)
