#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 16:16
# @Author  : Bilon
# @File    : 玩转字符串.py

''' 1.字符串的连接和合并 '''
# 字符串连接直接用 '+'
str1 = 'Hello '
str2 = 'World'
new_str1 = str1 + str2   # Hello World
# 合并 用join
url = ['www', 'python', 'org']
print('.'.join(url))

''' 2.字符串切片 '''
str3 = 'Monday is a busy day'
print(str3[0:7])    # 表示取第一个到第七个的字符串    Monday
print(str3[-3:])   # 表示取倒数第三个字符开始到结尾   day
print(str3[::])     # 复制字符串

""" 3.字符串的分割 """
# 普通的分割 用split
phone = '400-800-800-1234'
print(phone.split('-'))
# 复杂的分割
import re
line = 'hello world;  python, I ,like,    it'
print(re.split(r'[;,s]\s*', line))

""" 4.字符串的开头和结尾处理 """
# 比如要差一个文件的名字是以什么开头或什么结尾
filename = 'trace.h'
print(filename.endswith('h'))
print(filename.startswith('trace'))

""" 5.字符串的查找和匹配 """
# 一般查找 用find 若找到返回字符串所在位置的索引 找不到返回-1
title = 'Python can be easy to pick up and powerfullanguages'
print(title.find('pick up'))
# 复杂的匹配
mydate = '11/27/2016'
if re.match(r'\d+/\d+/\d+', mydate):
    print('ok, match')
else:
    print('ko, not match')

""" 6.字符串的替换 """
# 普通替换 用replace
text = 'Python is an easy to learn, powerful programming language'
print(text.replace('learn', 'study'))
# 复杂的替换 处理复杂或多个的替换，用re模块的sub函数
students = 'Boy 103, girl 105'
print(re.sub(r'\d+', '100', students))

""" 7.字符串中去掉一些字符 """
# 去除行首尾空格用 strip
new_line = '  Congratulations, you guessed it.  '
print(new_line.strip())
# 复杂的文本清理可以用 str.translate
# str.translate(map)
# bytes.translate(table[, delete])
# bytearray.translate(table[, delete])
# 先构建一个转换表， table是一个翻译表， 表示把 't' 'o' 转成大写的 'T' 'O'
instr = 'to'
outstr = 'TO'
table = str.maketrans(instr, outstr)
old_str = 'Hello world, welcome to use Python. 123456'
new_str = old_str.translate(table)
print(new_str)

# 用 bytes.translate(table[, delete]) 添加 delete 参数
# 先删除 delete 参数匹配到的值 再通过 table 转换
inbytes = b'to'
outbytes = b'TO'
table = bytes.maketrans(inbytes, outbytes)
old_bytes = old_str.encode(encoding='utf-8')        # 把 str 转换成 bytes
new_bytes = old_bytes.translate(table, b'12345')
new_str = new_bytes.decode()    # 把 bytes 转换成 str
print(old_bytes)
print(new_bytes)
print(new_str)