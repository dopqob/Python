#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 9:12
# @Author  : Bilon
# @File    : 字典里的5个黑魔法.py

from collections import OrderedDict

""" 1.字典的排序 """
# 用万金油 sorted() 函数  原始的 my_dict 本身顺序不会变
my_dict = {'cc': 100, 'aa': 200, 'bb': 10}
print(sorted(my_dict.items(), key=lambda x: x[0]))   # 表示按 key 排序
print(sorted(my_dict.items(), key=lambda x: x[1]))   # 表示按 value 排序

# 另外一种做法，因为字典是无序，若你一开始设计的时候就希望这个数据结构，按照添加的顺序进行有序排列
# 利用 collection 模块里面的 OrderedDict() 处理
# OrderedDict() 虽然是好东西，但数据量很大的话会非常耗内存
orderDict = OrderedDict()
orderDict['a'] = 1
orderDict['b'] = 2
orderDict['c'] = 3
print(orderDict)
# 对比一下，若是普通的 dict 是乱序的
orderDict1 = dict()
orderDict1['a'] = 1
orderDict1['b'] = 2
orderDict1['c'] = 3
print(orderDict1)

''' 2.字典的取值 '''
# 字典中取值大家很容易想到用 dict[key],确实一般取值是这样的
# 但若取的值不存在，就会发生异常，风险很大
prices = {'apple': 10, 'orange': 5, 'banana': 8}
# print(prices['peach'])    # KeyError

# 尽量用 dict.get() 来代替 dict[key]
print(prices.get('peach'))  # 当键值不存在时返回None,而不是异常
# get还有一个工厂方法，就是 dict.get(key, somethingelse)
print(prices.get('apple', 'Not found'))
print(prices.get('peach', 'Not found'))     # 若键值不存在就返回Not found

''' 3.字典中提取部分子集 '''
students_score = {'jack': 80, 'james': 91, 'leo': 100, 'sam': 60}
# 提取分数超过90分的学生信息，并变成字典
good_score = {name: score for name, score in students_score.items() if score > 90}
print(good_score)

''' 4.字典的计算 '''
# 比如我们有一个字典是记录股票的价格，一般key是股票的名字，value是价格
# 我们希望得到里面的 最大值，最小值
stocks = {'wanke': 25.6, 'wuliangye': 32.3, 'maotai': 299.5, 'huatai': 18.6}
# 方法一：利用字典的values()
print(min(stocks.values()))
print(max(stocks.values()))
# 方法二：利用神奇的zip()
new_stocks = list(zip(stocks.values(), stocks.keys()))    # zip()翻转keys,values，变成一个可迭代对象
print(min(new_stocks))      # (18.6, 'huatai')
print(max(new_stocks))      # (299.5, 'maotai')

''' 5.字典的翻转 '''
# 在处理复杂的数据结构的时候，有的时候希望把字典翻转，一般用推导列表进行过渡，然后用dict()转换成字典
invert_stocks = dict([(v, k) for k, v in stocks.items()])
print(invert_stocks)
# 也可以用 zip()
invert_stocks2 = dict(zip(stocks.values(), stocks.keys()))
print(invert_stocks2)
