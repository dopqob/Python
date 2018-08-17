#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 16:08
# @Author  : Bilon
# @File    : study1.py

# 打印一个边长为n的正方形
# l = int(input(">>>"))
# print(l*'*')
# a = l - 2
# for i in range(a):
#     print('*' + ' '*a + '*')
# print(l*'*')

# l = int(input(">>>"))
# for i in range(l):
#     if i == 0 or i == l - 1:
#         print('*' * l)
#     else:
#         print('*' + ' ' * (l - 2) + '*')

# 求100内所有奇数的和
# sum = 0
# for i in range(1,100,2):
#     sum += i
# print(sum)

# 给一个数，判断它是否为质数
num = int(input(">>>"))
for i in range(2, num):
    if num % i == 0:
        print("Can be divisible by " + str(i))      # 能被i整除
        print(str(num) + " is not a prime number")  # 不是质数
        break
else:
    print(str(num) + " is a prime number")