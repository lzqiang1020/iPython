# -*- coding: UTF-8 -*-
# @File  :  bubble_sort
# @Time  :  2019/9/2 18:42
# @Author:  liuzhiqiang

"""冒泡排序

它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

算法步骤：
    1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    3. 针对所有的元素重复以上的步骤，除了最后一个。
    4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
优化：
    立一个 flag，当在一趟序列遍历中元素没有发生交换，则证明该序列已经有序。
什么时候最快:
    当输入的数据已经是正序时（都已经是正序了，我还要你冒泡排序有何用啊）。
什么时候最慢:
    当输入的数据是反序时（写一个 for 循环反序输出数据不就行了，干嘛要用你冒泡排序呢，我是闲的吗）。
"""


def bubble_sort_1(data):
    length = len(data)
    for i in range(length-1):
        for j in range(length-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


def bubble_sort_2(data):
    length = len(data)
    for i in range(length-1):
        flag = False

        for j in range(length-1-i):
            if data[j] > data[j+1]:
                data[j], data [j+1] = data[j+1], data[j]
                flag = True

        if not flag:
            break
    return data


if __name__ == '__main__':
    import random

    data_list = list(range(10))
    random.shuffle(data_list)
    print("Origin data: {}".format(data_list))

    ordered_data = bubble_sort_2(data_list)
    print("Ordered data: {}".format(ordered_data))