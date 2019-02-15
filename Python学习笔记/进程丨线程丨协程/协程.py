#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 10:26
# @Author  : Bilon
# @File    : 协程.py
import time


def fun():
    i = 0
    while True:
        value = yield i
        if value is not None:
            print('接到任务...')
            time.sleep(1)
            i = value + 1
            print('完成任务...')


def run(cor):
    next(cor)
    for i in range(3):
        num = cor.send(i)  # 执行其它子程序
        print('当前数字：', num)
    cor.close()


def odds(max_num):  # 定义子生成器
    odd = 1  # 起始奇数
    count = 0  # 获取次数
    while odd <= max_num:  # 循环获取到最大奇数值
        value = yield odd  # 生成奇数
        odd += 2  # 计算下一个奇数
        count += 1  # 生成次数递增
        if value is None or True:  # 获取外部传入的值
            print('第', count, '个奇数生成成功...')
    return count  # 返回生成次数


def copy_odds(max_num):  # 定义委托生成器
    print('-' * 8, '开始', '-' * 8)
    count = yield from odds(max_num)  # 获取生成器部分操作以及返回值
    print('-' * 8, '完成', '-' * 8)
    print('共生成了', count, '个奇数。')


if __name__ == '__main__':

    # cor = fun()
    # run(cor)

    gen = copy_odds(9)  # 创建生成器对象
    print(gen.send(None))  # 挂起生成器
    while True:
        try:
            print(gen.send(True))  # 运行一次生成器并将值传入
        except:  # 迭代结束跳出循环
            break
