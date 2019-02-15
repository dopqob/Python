#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 16:58
# @Author  : Bilon
# @File    : 常用函数工具.py


# 常用函数工具

# map 把每一项传递给函数并收集结果
counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)              # [11, 12, 13, 14]
# 等价于
def inc(x): return x + 10
list(map(inc, counters))                # [11, 12, 13, 14]
# 用lambda函数
list(map((lambda x:x+10), counters))    # [11, 12, 13, 14]
# 接受多个序列作为参数
list(map(pow, [1,2,3], [2,3,4]))        # [1, 8, 81]    1**2,2**3,3**4


# filter 收集函数返回True值的项(过滤）
list(range(-5, 5))                              #[-5, -4, -3, -2, -1, 0, 1, 2, 3 ,4]
list(filter((lambda x: x > 0),range(-5, 5)))    #[1, 2, 3 ,4]


# reduce 通过对一个累加器和后续应用函数来计算一个单个的值
from functools import reduce
reduce((lambda x, y: x + y), [1, 2, 3, 4])      #10     1+2+3+4
reduce((lambda x, y: x * y), [1, 2, 3, 4])      #24     1*2*3*4



'''
列表解析
'''
L = [x ** 2 for x in range(10)]     # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
L = [x ** 2 for x in range(10) if x % 2 == 0]   # [0, 4, 16, 36, 64]

# 嵌套多循环
'''
[ expression for target1 in iterable1 [if condition1]
             for target2 in iterable2 [if condition2] ...
             for targetN in iterableN [if conditionN] ]
'''
RES = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]   # [100, 200, 300, 101, 201, 301, 102, 202, 302]
RES = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 ==1]   # [(0,1),(0,3),(2,1),(2,3),(4,1),(4,3)]

# 列表解析和矩阵
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

N = [[2,2,2],
     [3,3,3],
     [4,4,4]]

# [2,4,6,12,15,18,28,32,36]
RES = [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
# [[2,4,6],[12,15,18],[28,32,36]]
RES = [[M[row][col] * N[row][col] for row in range(3)] for col in range(3)]


# 对模块计时
import time
reps = 1000
repslist = range(reps)

def timer(func, *args, **kwargs):
    start = time.clock()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = time.clock() - start
    return (elapsed, ret)

import sys
newreps = 10000
newreplist = range(newreps)

def forLoop():
    res = []
    for x in newreplist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in newreplist]

def mapCall():
    return list(map(abs, newreplist))

def genExpr():
    return list(abs(x) for x in newreplist)

def genFunc():
    def gen():
        for x in newreplist:
            yield abs(x)
    return list(gen())

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, elapsed, result[0], result[-1]))
    