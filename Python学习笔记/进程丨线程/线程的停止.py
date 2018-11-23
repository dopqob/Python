#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 14:56
# @Author  : Bilon
# @File    : 线程的停止.py

"""
# ==================================================
# 线程的停止
# 可以用join()等待它自己结束
# 可以设定成daemon(即守护线程)，当主线程完成，子线程会自动销毁
# 更好的办法是自己构建一个方法，调度线程的属性或者一些高级操作
# ==================================================
"""
import threading
import time


class CountDownTask:
    """
    创建一个CountDownTask类，里面声明一个_running实例变量用来做线程的控制
    """
    def __init__(self):
        self._running = True

    def terminate(self):
        # 通过改变状态让线程终止
        self._running = False

    def run(self, n):
        """
        run函数里面是一个死循环，我们在while入口的地方留了两个出路(_running变量和n)
        当_running变成False 或者 n<=0 时，线程会停止
        """
        while self._running and n > 0:
            print('running {} {}'.format(n, time.ctime()))
            n -= 1
            time.sleep(1)


c = CountDownTask()
t = threading.Thread(target=c.run, args=(6,))
t.start()
# 本来线程要执行到6秒之后才会停止，我们在sleep3秒之后，就调用类的terminate函数把_running置成False, 就可以直接线程停止
time.sleep(3)
c.terminate()
print('Terminate... {}'.format(time.ctime()))
