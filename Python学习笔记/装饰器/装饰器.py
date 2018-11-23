#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 11:44
# @Author  : Bilon
# @File    : 装饰器.py
"""
# ================================================
#       装饰器的真面目
# 装饰器其实就是对函数进行再次包装，它能够在不改变函数的前提下
# 增加函数的功能，可以在函数执行之前或者执行之后执行一段代码
# ================================================
"""


"""
# =================================================================
# 例子
# 我们有一个主题函数word()是输出一个字符串
# 有一个函数是把字符串变粗体，另一个函数是变斜体
# 有了装饰器之后我们可以非常灵活的组合，扩展函数的功能
# =================================================================
"""


def makebold(func):
    def wrapper():
        return '<b>'+func()+'</b>'
    return wrapper


def makeitalic(func):
    def wrapper():
        return '<i>'+func()+'</i>'
    return wrapper


@makebold
@makeitalic
def word():
    return 'hello'


# 有一点要注意，如果装饰器的顺序变了，结果是不一样的
@makeitalic
@makebold
def word1():
    return 'world'


print(word())
print(word1())


