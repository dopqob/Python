#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 15:44
# @Author  : Bilon
# @File    : part2.py


def cfile():
    myfile = open('./myfile.txt', 'w')
    content = ['Hello', 'file', 'world!', 'You', 'are', 'great']
    for item in content:
        myfile.writelines(item + '\n')
    myfile.close()


def rfile():
    for line in open('myfile.txt'):
        print(line, end='')


cfile()
rfile()

