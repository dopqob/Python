#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 18:32
# @Author  : Bilon
# @File    : 杨辉三角丨生成器.py

"""
# ===========================================
# 下面的算法最巧妙在于构建一个[1,0],[1,1,0]这样的序列
# ===========================================
"""
def triangle(num):
    tr_list = [1]
    n = 0
    while n < num:
        yield tr_list
        tr_list.append(0)
        tr_list = [tr_list[i-1] + tr_list[i] for i in range(len(tr_list))]
        n += 1


for t in triangle(10):
    print(t)
