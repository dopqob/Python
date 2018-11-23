#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 17:30
# @Author  : Bilon
# @File    : 创建单个进程.py
import multiprocessing
import time

"""
# ==========================================
# 创建函数并将其作为单个进程
# ==========================================
"""

def f(name):
    print('hello', name)
    time.sleep(3)

if __name__ == '__main__':
    print('Start {}'.format(time.ctime()))
    p = multiprocessing.Process(target=f, args=('python',))
    p.start()
    p.join()
    print('End {}'.format(time.ctime()))
