#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 15:50
# @Author  : Bilon

"""
# =============================================
# 现实中会经常碰到字典的合并操作，如何实现呢?
# 方法一：借助dict(d1.items() + d2.items())的方法
# 方法二：借助字典的update()方法
# 方法三：借助字典的dict(d1, **d2)方法
# 方法四：借助字典的常规处理方法
# =============================================
"""

d1 = {'name': 'Jack', 'age': 23}
d2 = {'post': 'developer', 'pay': 8000}

# ===================================================================
# 方法一(不推荐）
# 1. d1.items()获取字典的键值对，得到的是一个可迭代对象
# 2. list(d1.items())将可迭代对象转换成列表
# 3. list(d1.items()) + list(d2.items())拼成一个新的列表
# 4. dict(list(d1.items()) + list(d2.items()))将合并成的列表转变成新的字典
# ===================================================================
d3 = dict(list(d1.items()) + list(d2.items()))
print('d3:', d3)

# 方法二：字典的update()方法
d4 = {}
d4.update(d1)   # 或者 d4 = d1.copy()
d4.update(d2)
print('d4:', d4)

# 方法三：借助字典的dict(d1,**d2)方法
d5 = dict(d1, **d2)
print('d5:', d5)

# 方法四：字典的常规处理方法
d6 = {}
for k, v in d1.items():
    d6[k] = v
for k, v in d2.items():
    d6[k] = v
print('d6:', d6)
