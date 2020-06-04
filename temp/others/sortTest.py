 # sorted

lst = [1, 5, 3, 4]

# init
# def sort(iterable, reverse=False):
#     ret = []
#     for x in iterable:
#         for i, y in enumerate(ret):
#             flag = x<y if not reverse else x>y
#             if flag:
#                 ret.insert(i, x)
#                 break
#         else:
#             ret.append(x)
#     return ret

# 优化
# def comp(a, b, reverse):   #reverse 为布尔值
#     return a<b if not reverse else a>b
#
# def sort(iterable, reverse=False):
#     ret = []
#     for x in iterable:
#         for i, y in enumerate(ret):
#             if comp(x, y, reverse):
#                 ret.insert(i, x)
#                 break
#         else:
#             ret.append(x)
#     return ret

#优化
def comp(a, b):
    return a<b

def sort(iterable, reverse=False):
    ret = []
    for x in iterable:
        for i, y in enumerate(ret):
            if comp(x, y, reverse):
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret

print(sort(lst))
