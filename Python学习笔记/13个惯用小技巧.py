#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 11:02
# @Author  : Bilon
# @File    : 13个惯用小技巧.py
from collections import defaultdict

# 1.遍历一个序列
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
    print(color)

# 2.遍历倒序
for color in reversed(colors):
    print(color)

# 3.遍历2个collection
names = ['leo', 'lili', 'sam']
for name, color in zip(names, colors):
    print(name, '--->', color)

# 4.遍历排序的序列
for color in sorted(colors):    # 正序
    print(color)
for color in sorted(colors, reverse=True):  # 倒序
    print(color)

# 5.自定义排序
print(sorted(colors, key=len))


"""
# 6.遍历文件遇到指定字符退出
# blocks = []
# if block in iter(partial(f.read, 32), ''):
#     blocks.append(block)
# iter是一个内置函数用来产生迭代器，partial不断读入文件中32字节
# 注意iter引入第二个参数，表示当读入的内容是''的时候，会出发生成器stop
"""


# 7.函数遍历多出口问题
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1

    return i


# 8.字典的循环
d = {'apple': 'red', 'banana': 'yellow', 'peach': 'peak'}
for k in list(d.keys()):
    if k.startswith('a'):
        del d[k]
for k in d:
    print(k)

# 9.字典的统计
colors = ['red', 'green', 'red', 'blue', 'yellow', 'green', 'red']
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1  # 巧妙的利用字典的get方法，取不到value的时候用缺省值0

# 10.字典的统计
names = ['leo', 'sam', 'jack', 'peter', 'joe', 'susuanna']
# 比如按名字的长度排序
nums = [len(n) for n in names]
contain = {}
for k1, k2 in zip(nums, names):
    print(k1, k2)
    if k1 not in contain:
        contain[k1] = [k2]
    else:
        contain[k1].append(k2)
print(contain)

# 更好的方法
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
print(d)

# 11.展开序列
p = ['Leo', 'Xin', 30, 'coder']
# 传统思维
# fname = p[0]
# lname = p[1]
# age = p[2]
# email = p[3]

# 更好的方法
fname, lname, age, email = p


# 12.交换变量
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x + y


# 13.更新序列
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa']
# 一般方法
del names[0]
names.pop(0)
names.insert(0, 'mark')

# 更好的方法
import collections
names = collections.deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa'])
del names[0]
names.popleft()
names.appendleft('mark')