# -*- coding: UTF-8 -*-
# @File  :  progress_bar
# @Time  :  2019/8/9  11:43
# @Author:  liuzhiqiang

import time


count_down = 15
interval_refresh = 3
for i in range(int(count_down/interval_refresh) + 1):
    print("加载进度：0%", end='')
    time.sleep(interval_refresh)
    print("\r加载进度：{}  {:.0%}".format("▇"*i, interval_refresh/count_down*i), end='')

print("\n加载完成。")