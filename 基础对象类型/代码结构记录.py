#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/11 17:23
# @Author  : Bilon
# @File    : 代码结构记录.py

'''简洁易懂系列'''

'''快速构成一个字典序列'''
print(dict(zip('abcd',range(4))))

'''用类似三目运算符输出'''
a = 1
print('ok' if a==1 else 'ko')

'''直接return条件判断'''
def test(m):
    return 'a' if m==1 else 'b'

'''推导列表生成字典'''
list1 = [(1,'a'), (2,'b')]
print({x[0]:x[1] for x in list1})
print({x:y for x in range(4) for y in range(10,13)})

'''排序，取最大值，取最小值'''
import heapq
nums = [10,2,9,100,80]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

students = [{'names': 'CC', 'score': 60, 'height': 189},
            {'names': 'BB', 'score': 10, 'height': 169},
            {'names': 'AA', 'score': 80, 'height': 179}]
print(heapq.nsmallest(2, students, key=lambda x:x['score']))

'''从一个很长的列表里找某一个或某一类元素，用lambda配合filter过滤'''
list2 = ['to_pickle', 'to_records', 'to_sparse', 'to_sql', 'transpose', 'truediv',
         'truncate', 'shift', 'tz_convert', 'tz_localize', 'unstack', 'update',
         'value', 'var', 'where', 'xs']
print(list(filter(lambda x:x.startswith('to_'), list2)))
# print(filter(lambda x:x.startswith('to_'), list2))        # Python2的写法

'''如果里诶包里面是一个一个字典'''
list3 = [{'aa':100, 'bb':200}, {'a1':300, 'cc':400}]
print(list(filter(lambda x: 'aa' in x.keys(), list3)))

