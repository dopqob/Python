#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 15:50
# @Author  : Bilon
# @File    : inter2.py


# 交集
def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

# 并集
def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

# 测试
# s1, s2, s3 = 'SPAM', 'SCAM', 'SLAM'
# print('交集:', intersect(s1, s2))
# print('并集:', union(s1,s2))


# 传入任意个参数，获取最大和最小值
def minmax(test, *args):
    res = args[0]
    for arg in args:
        if test(arg, res):
            res = arg
    return res

# 测试
# def lessthan(x,y):return x<y
# def morethan(x,y):return x>y
#
# print(minmax(lessthan,3,5,2,13,22,1,7))
# print(minmax(morethan,3,5,2,13,22,1,7))

# example
def func1(a, b=4, c=5):
    print(a, b, c)

func1(1, 2)         # 1 2 5

def func2(a, b, c=5):
    print(a, b, c)

func2(1, c=3, b=2)  # 1 2 3

def func3(a, *args):
    print(a, args)

func3(1, 2, 3)      # 1 (2,3)

def func4(a, **kwargs):
    print(a, kwargs)

func4(a=1, c=3, b=2)    # 1, {'c':3, 'b':2}

def func5(a, b, c=3, d=4):print(a, b, c, d)

func5(1, *(5,6))    # 1 5 6 4