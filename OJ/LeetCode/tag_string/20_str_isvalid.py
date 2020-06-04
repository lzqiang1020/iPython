# -*- coding: UTF-8 -*-
# @File    :  str_isvalid
# @Author  :  liuzhiqiang
# @Time    :  2019/8/28 8:43


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


test = Solution()
print(test.isValid("{[]}"))