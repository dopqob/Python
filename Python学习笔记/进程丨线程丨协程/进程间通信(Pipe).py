#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 9:33
# @Author  : Bilon
# @File    : 进程间通信(Pipe).py
"""
# ====================================================================================
# multiprocessing.Pipe()
# 管道模式，调用Pipe()返回管道两端的connection，(conn1,conn2)代表一个管道的两端
# Pipe仅仅适用于只有两个进程之间的对话，其中又分单双工情况
# Pipe方法有duplex参数，如果duplex参数为True(默认值),那么这个管道是全双工模式(conn1和conn2均可收发)
# 如果duplex为False，conn1只负责接收消息，conn2只负责发送消息
# ====================================================================================
"""
from multiprocessing import Process, Pipe


def receiver(rece_conn):
    while True:
        try:
            res = rece_conn.recv()
            print('recv:{}'.format(res))
        except EOFError:
            break


if __name__ == '__main__':
    """
    创建一个管道，一头是send_conn,另一头是recv_conn
    父进程负责发送数据，receiver子进程负责接收数据，当父进程发送完毕之后，就会调用关闭管道
    如果管道已经被关闭，那么子进程recv会抛出EOFError，剥啄到异常后，就停止发送数据
    """
    print('Starting...')
    send_conn, recv_conn = Pipe()
    p1 = Process(target=receiver, args=(recv_conn,))
    p1.start()

    for i in range(1, 5):
        send_conn.send(i)
        print('send:{}'.format(i))

    send_conn.close()
    p1.join()
    print('End!!!')
