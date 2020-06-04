# -*- coding: UTF-8 -*-
# @File  :  insert_sort
# @Time  :  2019/9/3 17:29
# @Author:  liuzhiqiang

def insert_sort(data):
    """
    插入排序： 将原序列分成已排序和未排序两个子序列，在已排序的序列中从后向前扫描，将待排序的数插入到合适的位置
    步骤：
        1. 将第一个数看成是有序序列，其余剩下的看出未排序序列；
        2. 增加一个哨兵，放入待比较值（即未排序序列）；
        3. 哨兵与已排序序列值比较，并放入合适的位置；
    优化：
        拆半插入法
    稳定性及应用场景：
        稳定排序算法
        使用在小规模数据的排序
    :param data: list[int]
    :return: list[int]
    """

    # data = [0] + data
    length = len(data)

    for i in range(1, length):
        sentinel = data[i]
        pre_index = i-1

        if data[pre_index] > sentinel:
            while pre_index >= 0 and data[pre_index] > sentinel:
                data[pre_index+1] = data[pre_index]
                pre_index -= 1
            data[pre_index+1] = sentinel

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
