#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 11:21
# @Author  : Bilon
# @File    : stydy2.py

# 打印九九乘法表
# for i in range(1, 10):
#     for ii in range(1, i+1):
#         n = ii * i
#         print(str(ii) + 'x' + str(i) + '=' + str(n)),
#     print('')

# 打印菱形
# n = int(input('>>>'))   # 请输入一个奇数
# for i in range(1, n, 2):
#     m1 = (n-i)/2
#     print(' '*m1 + '*'*i + ' '*m1)
# for j in range(n, 0, -2):
#     m2 = (n-j)/2
#     print(' '*m2 + '*'*j + ' '*m2)

# 打印100以内斐波那契数列
a = 1
for i in range(100):
    a += i
    print(a)

