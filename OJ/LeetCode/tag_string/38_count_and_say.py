# -*- coding: UTF-8 -*-
# @File        :  38_count_and_say
# @CreateTime  :  2019/10/13 13:58
# @Author      :  liuzhiqiang

"""
38.报数
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221

1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"
"""

def count_and_say(n):
    """

    :param n: int
    :return: str
    """
    pre_person = '1'
    for i in range(1, n):         # 1211  (-> 111221)
        next_person = ''
        num = pre_person[0]
        count = 1

        for j in range(1, len(pre_person)):
            if pre_person[j] == num:
                count += 1
            else:
                next_person += str(count) + num
                num = pre_person[j]
                count = 1
        next_person += str(count) + num
        pre_person = next_person
        print("{}:  {}".format(i+1, pre_person))
    return pre_person


def count_and_say_2(n):
    first = '1'
    cur = first

    for i in range(2, n + 1):
        pre, cur, count = cur, '', 1
        left = 0
        length = len(pre)

        while left + count < length:
            if pre[left] == pre[left + count]:
                count += 1
            else:
                cur += str(count) + pre[left]
                left += count
                count = 1

        cur += str(count) + pre[left]

    return cur


print(count_and_say_2(8))
