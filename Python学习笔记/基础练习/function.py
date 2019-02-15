#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/26 21:19
# @Author  : o_p_q_o
# @File    : function.py

"""
变量作用域
Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找
"""

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
