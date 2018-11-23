#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 14:39
# @Author  : Bilon
# @File    : 装饰器妙用.py
"""
# ========================
# 斐波那契数列（兔子数列）
# ========================
"""
import time


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


# 我们打印前40项，看看需要花多少时间
# start = time.time()
# [fib(n) for n in range(40)]
# end = time.time()
# print('fib耗时：{}秒'.format(end-start))
# 40项需要花70多妙，如果50项耗时更多，因为有大量重复的计算


def fib2(n, cache=None):
    """接着演变，我们现在构造一个缓冲区cache"""
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 1 or n == 0:
        return 1
    else:
        cache[n] = fib2(n-2, cache) + fib2(n-1, cache)
    return cache[n]


start = time.time()
print([fib2(n) for n in range(40)])
end = time.time()
print('fib2耗时：{}秒'.format(end-start))
print('-'*50)


"""
# =========================================
# 爬楼梯
# 比如有7阶台阶，我们可以用两种爬发，一次一步或者两步
# 只能进不能退，算算有多少种爬法
# =========================================
"""


# 我们先简单分析一下：
# 若只有一阶台阶，那么不管是一次选择一步还是两步，都只有一种爬法
# 若只有两阶台阶，选择一步or两步，会有两种爬法
# 若只有三阶台阶，选择一步然后一步然后一步，或者一步，两步，或者两步，一步，这样有3种爬法
# 若只有四阶台阶，选择一步，然后剩下3阶台阶的爬法，这3阶爬法可以直接取前面3阶台阶的计算结果
def climb(n, steps):
    """这个爬楼梯一样存在重复计算的问题，会非常耗时"""
    count = 0
    if n <= 1:
        count = 1
    else:
        for step in steps:
            count += climb(n-step, steps)
    return count


start = time.time()
print(climb(30, [1, 2]))
end = time.time()
print('climb(40, [1, 2])耗时：{}秒'.format(end-start))
print('-'*50)

"""
# =========================================
# 装饰器封装
# 对于兔子序列和爬楼梯，我们用装饰器去封装一下
# =========================================
"""


# 创建一个缓存装饰器
def decorate(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@decorate
def wrap_fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return wrap_fib(n-2) + wrap_fib(n-1)


@decorate
def wrap_climb(n, steps):
    count = 0
    if n <= 1:
        count = 1
    else:
        for step in steps:
            count += climb(n-step, steps)
    return count


start = time.time()
print([wrap_fib(n) for n in range(40)])
end = time.time()
print('wrap_fib(40)耗时：{}秒'.format(end-start))
print('-'*50)

start = time.time()
print(wrap_climb(40, (1, 2)))
end = time.time()
print('wrap_climb(40, (1, 2))耗时：{}秒'.format(end-start))
