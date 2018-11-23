#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 18:21
# @Author  : Bilon
# @File    : 斐波那契丨生成器.py


# 普通方法
def nor_fibo(num):
    n, a, b = 0, 0, 1
    fibo_list = []
    while n < num:
        fibo_list.append(b)
        a, b = b, a+b
        n += 1
    return fibo_list


print(nor_fibo(10))


# 如果用生成器效果更好,能看到生成过程
def yield_fibo(num):
    n, a, b = 0, 0, 1
    fibo_list = []
    for i in range(num):
        fibo_list.append(b)
        yield fibo_list
        a, b = b, a+b


for n in yield_fibo(10):
    print(n)
