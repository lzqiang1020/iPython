# -*- coding: UTF-8 -*-
# @File  :  circle_progress
# @Time  :  2019/8/9 13:08
# @Author:  liuzhiqiang

import time


count_down = 5
interval_refresh = 0.25
for i in range(0, int(count_down/interval_refresh)):
    ch_list = ['\\', '|', '/', '-']
    index = i % 4
    msg = "程序运行中 " + ch_list[index]
    print("\r"+msg, end='')
    time.sleep(interval_refresh)

print("\r结束"+" "*len(msg))