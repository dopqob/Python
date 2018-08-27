#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/26 21:19
# @Author  : o_p_q_o
# @File    : function.py

"""
***keyword-only参数***
如果在一个星号参数后，或者一个位置可变参数后出现的普通参数，实际上已经不是普通的参数了
而是keyword-only参数
"""


def fn(*args, x, y, **kwargs):      # Example
    print(x)
    print(y)
    print(args)
    print(kwargs)


fn(3, 5)                            # error
fn(3, 5, 7)                         # error
fn(3, 5, a=1, b='python')           # error
fn(7, 9, y=5, x=3, a=1, b='python')

# 另一种写法


def fn(*, x, y):    # 等价于def fn(*args, x, y)
    print(x, y)

