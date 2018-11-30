#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 11:22
# @Author  : Bilon
# @File    : mytools.py
import random


def wrap_print(func):
    """ 装饰打印，给上下加上*分隔符 """
    def wrapper(*args):
        print('*' * 100)
        func(*args)
        print('*' * 100 + '\n')
    return wrapper


@wrap_print
def my_print(*args):
    log = ''
    for arg in args:
        log += str(arg)
    print(log)


def creat_gbk(length):
    """
    随机生成指定长度的中文字符串
    :param length: 字符串长度
    """
    str_list = []
    for l in range(length):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x}{body:x}'
        s = bytes.fromhex(val).decode('gb2312')
        str_list.append(s)
    return ''.join(str_list)


def creat_phone():
    """ 随机生成11位手机号码 """
    # 第二位数字
    second = [3, 5, 6, 7, 8, 9][random.randint(0, 5)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        6: 6,
        7: [5, 6][random.randint(0, 1)],
        8: random.randint(0, 9),
        9: [8, 9][random.randint(0, 1)]
    }[second]

    # 最后八位数字
    suffix = ''.join(random.choice('0123456789') for i in range(0, 8))

    # 拼接手机号
    return '1{}{}{}'.format(second, third, suffix)
