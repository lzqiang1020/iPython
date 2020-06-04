# -*- coding: UTF-8 -*-
# @File        :  18_ip_check
# @CreateTime  :  2020/1/14 21:53
# @Author      :  liuzhiqiang

import sys


def check_ip(ip):
    if len(ip) != 4 and '' in ip:
        return False
    else:
        for i in range(4):
            if int(ip[i]) < 0 or int(ip[i]) > 255:
                return False
            else:
                return True

def check_mask(ms):
    if len(ms) != 4:
        return False