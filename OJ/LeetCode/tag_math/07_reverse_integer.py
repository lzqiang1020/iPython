# -*- coding: UTF-8 -*-
# @File  :  temp
# @Time  :  2019/8/23 9:10
# @Author:  liuzhiqiang

# x = 123
def reverse(x):
    if x == 0:
        return 0
    else:
        x_str = list(str(x).strip('0'))
    x_str.reverse()
    x_revs = str()

    for i in x_str:
        x_revs += i
    else:
        if x_revs[-1] == '-':
            x_revs = '-' + x_revs[:-1]
        x_revs = int(x_revs)

    if -2 ** 31 <= x_revs <= (2 ** 31 - 1):
        return x_revs
    else:
        return 0

if __name__ == '__main__':
    print(reverse(-1230))