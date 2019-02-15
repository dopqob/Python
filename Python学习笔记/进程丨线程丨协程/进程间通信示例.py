#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 9:20
# @Author  : Bilon
# @File    : 进程间通信示例.py
import multiprocessing
import time


# 我们虚拟一个取词和词典进程间的通信
def ocr(que):
    for value in ['one', 'two', 'three']:
        print('完成取词...')
        que.put(value)  # 将数据送出到进程共享队列
        time.sleep(1)


def dic(que):
    d = {'one': '一', 'two': '二', 'three': '三'}
    while True:
        value = que.get()  # 从进程共享队列获取到数据
        print(value, '：', d[value], sep='')


if __name__ == '__main__':
    que = multiprocessing.Queue()   # 创建进程共享队列
    process1 = multiprocessing.Process(target=ocr, args=(que,))
    process2 = multiprocessing.Process(target=dic, args=(que,))
    process1.start()
    process2.start()

    process1.join()  # 等待进程process1结束
    process2.terminate()  # 终止进程
