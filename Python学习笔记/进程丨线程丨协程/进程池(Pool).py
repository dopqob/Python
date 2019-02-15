#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 9:33
# @Author  : Bilon
# @File    : 进程池(Pool).py
import multiprocessing
import time


def task01(name):
    print(name)
    time.sleep(0.01)
    print(name)


def task02(name):
    print(name)
    time.sleep(0.01)
    print(name)


def task03(name):
    print(name)
    time.sleep(0.01)
    print(name)


if __name__ == '__main__':
    task_lst = [task01, task02, task03]  # 创建需运行函数的列表
    processes = multiprocessing.Pool(3)  # 创建进程池对象，设定并行最大进程数为3个
    for i in range(len(task_lst)):
        # 维持执行的进程总数为3个，当一个进程执行完毕后会添加新的进程进去
        processes.apply_async(task_lst[i], args=('进程' + str(i + 1),))
    processes.close()  # 关闭进程池对象，禁止再加入新的进程
    processes.join()  # 等待所有子进程结束
