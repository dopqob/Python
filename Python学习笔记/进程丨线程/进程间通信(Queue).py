#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 18:56
# @Author  : Bilon
# @File    : 进程间通信(Queue).py
"""
# ======================================================
# Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递
# put方法用来插入数据到队列中，get方法可以从队列读取并且删除一个元素
# ======================================================
"""

from multiprocessing import Process, Queue
from time import ctime, sleep
import os


def worker(my_queue):
    print('worker process:{} at {:<28}'.format(os.getpid(), ctime()))
    for task in ['task' + str(i) for i in range(1, 4)]:
        print('Worker put {} into the queue'.format(task))
        my_queue.put(task)


def consumer(my_queue):
    print('\nconsumer process:{} at {:<28}'.format(os.getpid(), ctime()))
    sleep(0.05)
    while True:
        try:
            res = my_queue.get(block=False)
            print('Consumer get {} from queue'.format(res))
        except:
            print('Queue is empty at: {}'.format(ctime()))
            break


def main():
    """
    创建一个Queue对象，然后把它塞进两个进程里面，作为传递数据的媒人
    队列里面放3个task，worker不断的put, consumer不断的get
    当Queue为空的时候，就会抛异常，我们用try/except捕捉一下，然后退出while
    """
    q = Queue()
    process_worker = Process(target=worker, args=(q,))
    process_consumer = Process(target=consumer, args=(q,))
    process_worker.start()
    process_consumer.start()
    process_worker.join()
    process_consumer.join()


if __name__ == '__main__':
    main()
