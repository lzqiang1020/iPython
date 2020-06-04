# -*- coding: UTF-8 -*-
# @File  :  shell_sort
# @Time  :  2019/9/4 15:45
# @Author:  liuzhiqiang

def shell_sort(data):
    """
    希尔排序：

    步骤：

    优化及应用：

    :param data:
    :return:
    """
    pass
    return data


if __name__ == '__main__':
    data_list = [
        [1, 9, 8, 5, 6, 7, 4, 3, 2],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    for i in range(len(data_list)):
        print("-"*100)
        data = data_list[i]
        print("Origin data[{}]: {}".format(i, data))
        ordered_data = insert_sort(data)
        print("Ordered data: {}".format(ordered_data))
