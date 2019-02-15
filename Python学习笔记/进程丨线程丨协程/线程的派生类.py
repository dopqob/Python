#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 11:20
# @Author  : Bilon
# @File    : 线程的派生类.py
import threading
from time import sleep, ctime


"""
# ========================================
# 当代码多的时候，用线程的派生类很干净整洁，容易维护
# ========================================
"""


class MyThread(threading.Thread):
    """
    声明一个MyThread类，这个类要继承threading.Thread
    在init函数里初始化一下类
    """
    def __init__(self, args):
        threading.Thread.__init__(self)
        self.args = args

    def run(self):
        """
        这个类里面有一个run函数，一般我们把要跑的task放在这个函数里
        当类启动的时候就会执行run这个函数
        """
        nloop, nsec = self.args
        print('{} start loop{} at: {}'.format(self.name, nloop, ctime()))
        sleep(nsec)
        print('loop{},done at: {}'.format(nloop, ctime()))


def main():
    """
    声明一个main函数，这个函数里面做了3件事
    第一：创建了2个MyThread类的对象
    第二：把这两个子类对象放到一个列表(threads)里面
    第三：把threads里面的线程类一一启动，调用threads[i].start()启动线程
    这时就会去调用run函数，然后用threads[i].join()等待所有的线程完成
    """
    print('Starting at: {}'.format(ctime()))
    threads = []
    loops = [2, 4]
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread((i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('All Done At: {}'.format(ctime()))


if __name__ == '__main__':
    main()
