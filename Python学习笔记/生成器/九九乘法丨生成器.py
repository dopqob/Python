#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 17:01
# @Author  : Bilon
# @File    : 九九乘法丨生成器.py


# 普通写法
def normal_9_9(num=9):
    n = 1
    table_list = []
    while n <= num:
        e = ['{}*{}={}'.format(i, n, i * n) for i in range(1, n + 1)]
        n += 1
        table_list.append(e)
    return table_list


T = normal_9_9()
for t in T:
    print(t)


# 用生成器的写法
def yeild_9_9(num=9):
    n = 1
    while n <= num:
        e = ['{}*{}={}'.format(i, n, i * n) for i in range(1, n + 1)]
        n += 1
        yield e


T = yeild_9_9()
for t in T:
    print(t)