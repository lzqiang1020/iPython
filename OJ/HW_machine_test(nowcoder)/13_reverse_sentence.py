# -*- coding: UTF-8 -*-
# @File        :  reverse_sentence
# @CreateTime  :  2019/9/19 11:01
# @Author      :  liuzhiqiang

"""
题目描述
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符

输入描述:
将一个英文语句以单词为单位逆序排放。

输出描述:
得到逆序的句子

示例1
输入
I am a boy
输出
boy a am I
"""

get_sentence = input()
get_sentence_list = get_sentence.split()
length = len(get_sentence)

print(' '.join(get_sentence_list[-1:-length-1:-1]))