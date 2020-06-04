# -*- coding: UTF-8 -*-
# @File  :  is_digit
# @Time  :  2019/8/10 16:53
# @Author:  liuzhiqiang

num = ''
while True:
    num = input("Input a positive number >>> ").strip().lstrip('0')
    if num.isdigit():
        break

print("The length of {} is {}.".format(num, len(num)))

print("Negative range: ", end=' ')
for i in range(len(num), 0, -1):
    print(num[i-1], end=' ')
print()

print("Method reversed: ", end='')
for i in reversed(num):
    print(i, end=' ')
print()

print("Negative index: ", end='')
for i in range(len(num)):
    print(num[-i-1], end=' ')
print()

print("Count of Digit appeared: ")
counter = [0]*10
for i in range(10):
    counter[i] = num.count(str(i))
    if counter[i]:
        print("The count of {} is {}".format(i, counter[i]))
print("~"*20)

counter = [0]*10
for x in num:
    i = int(x)
    if counter[i] == 0:
        counter[i] = num.count(x)
        print("The count of {} is {}".format(x, counter[i]))
print("~"*20)

counter = [0]*10
for x in num:
    i = int(x)
    counter[i] += 1
for i in range(len(counter)):
    if counter[i]:
        print("The count of {} is {}".format(i, counter[i]))
