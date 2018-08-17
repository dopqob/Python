#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 15:02
# @Author  : Bilon
# @File    : 集合(set).py

x = set('abcde')
y = set('bdxyz')

# >>> x
# set(['a','c','b','e','d'])
# >>> y
# set(['y','x','b','d','z'])

print('e' in x)
# True

print(x - y)
# set(['a', 'c', 'e'])

print(x | y)
# set(['a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'])

print(x & y)
# set(['b', 'd'])

print(x ^ y)
# set(['a', 'c', 'e', 'y', 'x', 'z'])

z = x.intersection(y)       # same as x & y
z.add('SPAM')
z.update(set(['X', 'Y']))
z.remove('b')

# 用表达式操作时必须两边都是集合(set)
S = set([1, 2, 3])
S | set([3, 4])
S | [3, 4]      # TypeError: unsupported operand type(s) for |: 'set' and 'list'

# 用set自带的方法可以是任何对象
S.add(4)
S.union([3, 4])
S.intersection((1, 3, 5))
S.issubset(range(-5, 5))        # 判断是否是子集