# -*- coding: UTF-8 -*-
# @File  : count_down
# @Time  : 2019/8/9 11:15
# @Author: liuzhiqiang

import time

count_down = 5
for i in range(count_down, 0, -1):
    print_msg = u"系统将在 " + str(i) + u"秒 内自动退出。。。"
    print("\r"+print_msg, end='')
    time.sleep(1)
end_msg = u"倒计时结束!" + " "*len(print_msg)
print("\r"+end_msg)