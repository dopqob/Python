#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/17 22:24
# @Author  : o_p_q_o
# @File    : study3.py

# D = {'a': 1, 'b': 2, 'c': 3}
# Ks = list(D.keys())
# Ks.sort()
# for key in Ks:
#     print(key + '=>' + str(D[key]), end='\n')

# 杨辉三角
# ls = [[1], [1, 1]]
# for i in range(2, 4):
#     pre = ls[i-1]
#     cur = [1]
#     for j in range(i-1):
#         print(pre[j])
#         print(pre[j+1])
#         cur.append(pre[j]+pre[j+1])
#     cur.append(1)
#     ls.append(cur)
# print(ls)

ls = []
for i in range(0, 11):
    if i == 0:
        ls.append([1])
    else:
        pre = ls[i-1]
        cur = [1]
        for j in range(i-1):
            cur.append(pre[j]+pre[j+1])
        cur.append(1)
        ls.append(cur)
for i in range(len(ls)):
    print(ls[i], end='\n')