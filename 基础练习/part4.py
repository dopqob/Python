#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 10:46
# @Author  : Bilon
# @File    : part4.py

'''
第四章习题
'''


# def adder(x,y):
#     return x+y

# print(adder(1,2))
# print(adder('so ','easy'))
# print(adder([1,2],[5,6]))
# adder({'a':10},{'name':'bob'})
# adder()

# def adder(*args):
#     res = args[0]
#     for arg in args[1:]:
#         res += arg
#     return res
#
# print(adder('a','b','c'))
# print(adder({'a':1},{'b':2}))

# def adder(x=3,y=5,z=2):
#     return x+y+z
#
# print(adder('a', 'b', 'c'))
# print(adder(x=1,z=5))

def adder1(*args):
    res = args[0]
    for arg in args[1:]:
        res += arg
    return res


def adder2(**kwargs):
    keylist = list(kwargs.keys())
    res = kwargs[keylist[0]]
    for key in keylist[1:]:
        res += kwargs[key]
    return res


def adder3(**kwargs):
    valuelist = list(kwargs.values())
    x = valuelist[0]
    for value in valuelist[1:]:
        x += value
    return x


def adder4(**kwargs):
    return adder1(*kwargs.values())


# print(adder1(1,2,3), adder1('python ','is ','so easy'))
# print(adder2(a=1,b=2,c=3), adder2(a='python ',b='is ',c='so easy'))
# print(adder3(a=1,b=2,c=3), adder3(a='python ',b='is ',c='so easy'))
# print(adder4(a=1,b=2,c=3), adder4(a='python ',b='is ',c='so easy'))


def copyDict(old:dict):             # 字典复制
    new = {}
    for key in old.keys():
        new[key] = old[key]
    return new

# print(copyDict({'a':'python ', 'b':'is ', 'c':'so ', 'd':'easy'}))


def addDict(dict1, dict2):          # 两个字典求并集
    new = {}
    for key in dict1.keys():
        new[key] = dict1[key]
    for key in dict2.keys():
        new[key] = dict2[key]
    return new

# print(addDict({'bob': 22, 'sam': 19},{'sam': 21, 'jo': 23}))


def prime(num):
    if num <= 1:
        print('{} is not prime'.format(num))
    else:
        mid = num // 2
        while mid > 1:
            if num % mid == 0:
                print('{} has factor {}'.format(num, mid))
                break
            mid -= 1
        else:
            print('{} is prime'.format(num))

# prime(13)
# prime(13.0)
# prime(15)
# prime(15.0)
# prime(-3)

def sqrt(x):            #求平方根
    # return x ** 0.5
    return pow(x, .5)

def newList1(old):
    return list(map(sqrt, old))

def newList2(old):
    return [x ** 0.5 for x in old]

import math
def newList3(old):
    new = []
    for x in old:
        new.append(math.sqrt(x))
    return new

# print(newList1([2, 4, 9, 16, 25]))
# print(newList2([2, 4, 9, 16, 25]))
# print(newList3([2, 4, 9, 16, 25]))

message = "First version"
def printer():
    print(message)