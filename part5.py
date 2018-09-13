#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 17:26
# @Author  : Bilon
# @File    : part5.py

'''
第五章练习
'''

def countLines(name):
    tot = 0
    # 加入编码防止被读取文件中含中文字符报错
    for line in open(name, encoding='utf-8'): tot += 1
    return tot

def countChars(name):
    tot = 0
    for line in open(name, encoding='utf-8'): tot += len(line)
    return tot

def test(name):
    return countLines(name),countChars(name)

"""
实现传入文件对象，只打开文件一次
使用内置文件对象的seek方法：file.seek(0)，文件的read方法会从文件当前位置开始读起
调整后的代码如下：
"""

def countLines1(file):
    file.seek(0)
    return len(file.readlines())

def countChars1(file):
    file.seek(0)
    return len(file.read())

def test1(name):
    file = open(name, encoding='utf-8')
    return countLines1(file),countChars1(file)

# if __name__ == '__main__':
#     print(test1('part5.py'))

if __name__ == '__main__':
    print(test1(input('Enter file name:')))

# if __name__ == '__main__':
#     import sys
#     print(test1(sys.argv[1]))