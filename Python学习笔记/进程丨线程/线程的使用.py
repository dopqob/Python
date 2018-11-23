#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 10:06
# @Author  : Bilon
# @File    : 线程的使用.py
import threading
from time import sleep, ctime


"""
# =====================================
# 线程的创建、启动、阻塞
# =====================================
"""


def loop(nsec):
    """
    先申明一个loop函数，传入一个sleep时间，打印一下启动时间，然后sleep几秒
    """
    print('Start loop: {:>30}'.format(ctime()))
    print('Sleep {} seconds'.format(nsec))
    sleep(nsec)


def main():
    """
    然后申明一个main函数，targe是要调用的函数名字，args是要传递给targe函数的参数
    args是一个元组，如果只有一个参数，后面要加逗号
    用t.start()来启动线程，用t.join()阻塞，一直等到线程完成，打印'All Done'
    """
    print('Starting: {:>30}'.format(ctime()))
    t = threading.Thread(target=loop, args=(3,))

    t.start()   # 开始线程
    t.join()    # 等待线程结束

    print('All Done: {:>30}'.format(ctime()))


if __name__ == '__main__':
    main()
