# -*- coding: UTF-8 -*-
# @File    :  longest_common_prefix
# @Author  :  liuzhiqiang
# @Time    :  2019/8/27 8:54


class Solution(object):
    # def longestCommonPrefix(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #
    #     # 输入: ["flower","flow","flight"]
    #     # 输出: "fl"
    #     """
    #     length = min([len(item) for item in strs])
    #     if length == 0:
    #         return ""
    #     common_prefix = ''
    #     for i in range(length):
    #         for s in strs[1:]:
    #             if strs[0][i] != s[i]:
    #                 if i == 0:
    #                     return " "
    #                 else:
    #                     return common_prefix
    #
    #         common_prefix += strs[0][i]
    #
    #     return common_prefix

    def longest_common_prefix(self, strs):
        common_prefix = ''
        for s in zip(*strs):
            if len(set(s)) == 1:
                common_prefix += s[0]
            else:
                break

        return common_prefix

strs_box = [["dog","racecar","car"], ["flower","flow","flight"]]
strs = strs_box[1]
test = Solution()
print(test.longest_common_prefix(strs))