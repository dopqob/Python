#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 14:49
# @Author  : Bilon
# @File    : 几个正则的例子.py
import re

"""
# =================================================
# 找出列表里在10到59的数字
# =================================================
"""
mylist = ['xy', 10, 'w33', 18, 211, 32, 458, 63, 59, '55w']
patt = r'\b[1-5][0-9]\b'
newlist = []
for i in mylist:
    if re.match(patt, str(i)):
        # print(i)
        newlist.append(i)
# print(newlist)


"""
# =================================================
# 过滤字符串中只含2个字母的字符，并且第一个字母是大写A或B或C
# =================================================
"""
str1 = 'xy,13,Bla,285,Ad,Co,BB,Ace,Boo,aBc'
mylist1 = str1.split(',')
patt = r'\b[A-C][a-zA-Z]\b'
newlist1 = []
for i in mylist1:
    if re.match(patt, i):
        newlist1.append(i)
# print(newlist1)


"""
# =================================================
# 过滤一个字符串中只含3个字母的字符
# =================================================
"""
str2 = 'xyhh,a,1aaa,2abc,?,123@sohu,Ab,w1,Cz,xyh,abcd'
patt = r'\b[a-zA-Z]{3}\b'
mylist2 = str2.split(',')
newlist2 = []
for i in mylist2:
    if re.match(patt, i):
        newlist2.append(i)
# print(newlist2)


"""
# =================================================
# 匹配12小时制时间
# =================================================
"""
mylist3 = ['10:00am', '99:90am', '8:00am', '12:49pm', '3:51pm', '15:00pm', '23:23pm', '29:19pm']
patt = r'\b([1-9]|1[0-2])(:)([0-5][0-9][ap]m)'
newlist3 = []
for i in mylist3:
    if re.match(patt, i):
        newlist3.append(i)
# print(newlist3)


"""
# =================================================
# 匹配24小时制时间
# =================================================
"""
str3 = '10:00,99:90,8:00am,12:49,3:51pm,15:00,23:23pm,29:19,00:30,0:30,24:25'
patt = r'\b(1?[0-9]|2[0-3])(:)([0-5][0-9])\b'
match = re.findall(patt, str3)
if match:
    print(list(''.join(x) for x in match))