# -*- coding: UTF-8 -*-
# @File  :  select_sort
# @Time  :  2019/9/3 15:11
# @Author:  liuzhiqiang

"""选择排序

算法步骤：
    1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3. 重复第二步，直到所有元素均排序完毕。

优化：
    1. 二元思想，循环一次，确定两个数，即一个最大，一个最小
    2. 如果一轮比较后，极大值与极小值的值相等，说明比较的序列元素全部相等
"""


def select_sort_1(data):
    length = len(data)

    for i in range(length-1):
        min = i
        for j in range(i+1, length):
            if data[min] > data[j]:
                min = j

        if min != i:
            data[min], data[i] = data[i], data[min]

    return data


def select_sort_2(data):   # [9, 3, 7, 1]
    length = len(data)
    for i in range(length//2):
        min_index = i
        max_index = -i-1
        max_origin = max_index

        for j in range(i+1, length-i):
            if data[min_index] > data[j]:
                min_index = j
            if data[max_index] < data[-j-1]:
                max_index = -j-1

        if min_index != i:
            data[min_index], data[i] = data[i], data[min_index]
            if i == max_index or i == length + max_index:
                max_index = min_index
        if max_index != max_origin:
            data[max_index], data[max_origin] = data[max_origin], data[max_index]

    return data


def select_sort_3(data):  # [9, 3, 7, 1, 1, 1, 1, 1]
    length = len(data)
    for i in range(length//2):
        min_index = i
        max_index = -i-1
        max_origin = max_index

        for j in range(i+1, length-i):
            if data[min_index] > data[j]:
                min_index = j
            if data[max_index] < data[-j-1]:
                max_index = -j-1

        if data[min_index] == data[max_index]:
            break

        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
            if max_index == i or i == length + max_index:  # 如果极大值被交换过，则更新极大值索引
                max_index = min_index
        if max_origin != max_index:
            data[max_origin], data[max_index] = data[max_index], data[max_origin]

    return data


if __name__ == '__main__':
    import random

    data_list = list(range(10))
    random.shuffle(data_list)
    print("Origin data: {}".format(data_list))

    ordered_data = select_sort_3(data_list)
    print("Ordered data: {}".format(ordered_data))
