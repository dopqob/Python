#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 18:05
# @Author  : Bilon
# @File    : 创建多个进程.py
import multiprocessing
import os
from time import sleep, ctime

"""
# ==========================================
# 创建多个函数并将其作为多个进程
# ==========================================
"""


def func1(interval):
    print('Run child process func1 ({}) at: {}'.format(os.getpid(), ctime()))
    # print(os.getpid())
    sleep(interval)
    print('End func1 at: {}'.format(ctime()))


def func2(interval):
    print('Run child process func2 ({}) at: {}'.format(os.getpid(), ctime()))
    # print(os.getpid())
    sleep(interval)
    print('End func2 at: {}'.format(ctime()))


if __name__ == '__main__':
    print('Parent process id: {}'.format(os.getpid()))
    p1 = multiprocessing.Process(target=func1, args=(2,))
    p2 = multiprocessing.Process(target=func2, args=(4,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Process END')
