# -*- coding: UTF-8 -*-
# @File  :  romanToInt
# @Time  :  2019/8/23 17:56
# @Author:  liuzhiqiang

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # roman_dict = {
        #     'M': 1000,
        #     'D': 500,
        #     'C': 100,
        #     'L': 50,
        #     'X': 10,
        #     'V': 5,
        #     'I': 1
        # }
        roman_dict = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        res_int = 0

        # for i in range(len(s)-1):
        #     if roman_dict[s[i]] < roman_dict[s[i+1]]:
        #         res_int += -roman_dict[s[i]]
        #     else:
        #         res_int += roman_dict[s[i]]
        # res_int += roman_dict[s[-1]]
        #
        # return res_int

        i = 0
        while i < len(s)-1:
            if roman_dict[s[i]]<roman_dict[s[i+1]]:
                res_int += roman_dict[s[i:i+2]]
                if i == len(s)-2:
                    return res_int
                i += 2
                continue
            res_int += roman_dict[s[i]]
            i += 1
        res_int += roman_dict[s[-1]]
        return res_int

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
#         return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))

test = Solution()
print(test.romanToInt("IV"))