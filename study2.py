#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 11:21
# @Author  : Bilon
# @File    : study2.py

# 打印九九乘法表
# for i in range(1, 10):
#     for ii in range(1, i+1):
#         n = ii * i
#         print(str(ii) + 'x' + str(i) + '=' + str(n)),
#     print('')

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={:<2} '.format(j, i, j*i), end='\t')
#     print()

# for i in range(1, 10):
#     s = ''
#     for j in range(i, 10):
#         s += '{}x{}={:<2} '.format(i, j, j*i)
#     print(' '*7*i + s)

# 打印菱形
# n = int(input('>>>'))   # 请输入一个奇数
# m = n//2
# s1, s2 = ' ', '*'
# for i in range(-m, n-m):
#     j = -i if i < 0 else i
#     print(s1 * j + s2 * (n - 2*j))
#   或者用绝对值
#   print(s1 * abs(i) + s2 * (n - 2*abs(i)))
# print()

# 打印对顶三角
# for i in range(-m, n-m):
#     j = -i if i < 0 else i
#     print(s1 * (m-j) + s2 * (2*j+1))
#   或者用绝对值
#   print(s1 * (m-abs(i)) + s2 * (2*abs(i)+1))
# print()

# 打印闪电
# for i in range(-m, n-m):
#     if i > 0:
#         print(s1*m + s2*(n-m-i))
#     elif i == 0:
#         print(s2*n)
#     else:
#         print(s1*-i + s2*(n+i-m))

# 打印100以内斐波那契数列
# a = 0
# b = 1
# c = 0
# print(b, end=' ')
# while True:
#     c = a + b
#     if c > 100:
#         break
#     print(c, end=' ')
#     a = b
#     b = c

# print(b, end=' ')
# for i in range(1, 101):
#     if i == a + b:
#         print(i, end=' ')
#         a = b
#         b = i

# 求斐波那契数列第101项
# a = 0
# b = 1
# for i in range(2, 102):
#     a, b = b, a+b
#     if i == 101:
#         print(b)

# 打印10万以内的斐波那契数列
a = 0
b = 1
for i in range(2, 102):
    a, b = b, a+b
    if i == 101:
        print(b)