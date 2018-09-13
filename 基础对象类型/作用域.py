#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 15:44
# @Author  : Bilon
# @File    : part2.py

# 作用域 LNGB
# L     Local       本地作用域
# N     Nonlocal    上层函数作用域
# G     Global      全局作用域
# B     Built-in    内置作用域

def cfile():
    myfile = open('./myfile.txt', 'w')
    content = ['Hello', 'file', 'world!', 'You', 'are', 'great']
    for item in content:
        myfile.writelines(item + '\n')
    myfile.close()

def rfile():
    for line in open('myfile.txt'):
        print(line, end='')

y, z = 1, 2
def all_global():
    global x
    x = y + z

def maker(n):
    def action(x):
        return x ** n
    return action

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts

# acts = makeActions()
# for x in range(5):
#     print(acts[x](2))

# def tester(start):
#     state = start
#     def nested(label):
#         print(label, state)
#     return nested
#
# F = tester(0)
# F('Bilon')
# F('Larry')

def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

# F = tester(0)
# F('Bilon')
# F('Larry')
#
# G = tester(40)
# G('Jacky')
# G('Flower')



