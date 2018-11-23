#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 15:56
# @Author  : Bilon
# @File    : 生成器.py


"""
# ==================================================
# 何为生成器（Generator)
# 生成器不会把结果保存在一个系列中，二是保存生成器的状态
# 在每次进行迭代时才返回一个值，直到遇到StopIteration异常结束
# 生成器表达式：和列表解析语法类似，只不过把列表解析的[]换成()
# ==================================================
"""
L = [x**2 for x in range(1, 5)]     # 列表
print(L)
g = (x**2 for x in range(1, 5))     # 生成器
print(g)


"""
# ==================================================================
# 生成器函数
# 函数中只要出现了yield语句就会将其转变成一个生成器函数
# yield的作用就是把一个函数变成一个generator，带有yield的函数不再是一个普通函数
# 生成器值在迭代操作的时候才能运行，yield可以把函数中断，保存状态和继续执行的能力
# ===================================================================
"""
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('done')

c = countdown(3)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# 正确的方法是使用for循环，因为generator也是可迭代对象
for n in c:
    print(n)
