#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 11:49
# @Author  : Bilon
# @File    : 高阶函数.py

'''高阶函数'''

'''
定义：
①接受一个或多个函数作为参数
②返回一个函数
满足其一即为高阶函数
'''

# Example  返回一个函数
def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc

foo = counter(5)
print(foo())
f1 = counter(5)
f2 = counter(5)
print(id(f1), id(f2))


# Example 接受一个匿名函数作为参数
lst = [2, 4, 6, 4, 2, 3, 8, 3]      # sorted => newlist

def sort(lst, fn=lambda a,b: a<b):
    newlist = []
    for x in lst:
        for i,y in enumerate(newlist):
            if fn(x,y):
                newlist.insert(i, x)
                break
        else:
            newlist.append(x)
    return newlist

print(sort(lst))
print(sort(lst,lambda x,y: x>y))
# 跟内置的sorted函数对比
print(sorted(lst))
print(sorted(lst, reverse=True))