# -*- coding: UTF-8 -*-
# @File        :  67_add_binary
# @CreateTime  :  2019/10/14 17:25
# @Author      :  liuzhiqiang

"""
67 二进制求和
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"
示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# def add_binary(a, b):
#     """
#
#     :param a:
#     :param b:
#     :return: str
#     """
#
#     length_diff = len(a) - len(b)
#     if length_diff == 0:
#         length = len(a)
#     elif length_diff > 0:
#         length = len(a)
#         b = '0' * length_diff + b
#     else:
#         length = len(b)
#         a = '0' * abs(length_diff) + a
#
#     sum = ''
#     flag = 0
#     for i in range(-1, -length-1, -1):
#         tem = int(a[i]) + int(b[i]) + flag
#         if tem < 2:
#             sum += str(tem)
#             flag = 0
#         if tem == 3:
#             sum += '1'
#             flag = 1
#         if tem == 2:
#             sum += '0'
#             flag = 1
#
#         if flag and i == -length:
#             sum += '1'
#
#     return sum[::-1]

# def add_binary_1(a, b):
#     return bin(int(a, 2) + int(b, 2))[2:]

# def add_binary_2(a, b):
#     r, p = '', 0
#     d = len(b) -len(a)
#     a = '0' * d + a
#     b = '0' * -d + b
#
#     for i, j in zip(a[::-1], b[::-1]):
#         s = int(i) + int(j) + p
#         r = str(s % 2) + r
#         p = s // 2
#
#     # return p * '1' + r
#     return '1' + r if p else r


def add_binary_3(a, b):
    max_length = max(len(a), len(b))
    a, b = a.zfill(max_length), b.zfill(max_length)

    carry, res = 0, ''
    for i in range(-1, -max_length-1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1

        if carry % 2 == 1:
            res = '1' + res
        else:
            res = '0' + res
        carry //= 2

    if carry == 1:
        res = '1' + res
    return res


a = '1101'
b = '10101'
print(add_binary_3(a, b))
