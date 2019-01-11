#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 11:17
# @Author  : Bilon
# @File    : test.py

# 去掉字符串首尾空格
import random
import re
import threading
import unittest


def trim(s):
    while len(s) > 0:
        if s[0] == ' ':
            s = s[1:]
        elif s[-1] == ' ':
            s = s[:-1]
        else:
            return s
    return ''


# 查找一个List中的最大和最小值
def find_min_and_max(list1):
    if len(list1):
        _min = list1[0]
        _max = list1[0]
        for l in list1:
            if l > _max:
                _max = l
            if l < _min:
                _min = l
        return _min, _max
    return None, None


# 将一个列表中的所有字符串转换成小写，生成一个新的列表
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [l.lower() for l in L1 if isinstance(l, str)]  # isinstance(item, type)判断类型


# 斐波那契数列
def fib(maxlen):
    n, a, b = 0, 0, 1
    while n < maxlen:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# 杨辉三角
from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        print(e)
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


def fact(n):
    '''
    Calculate 1*2*...*n

    fact(1)
    1
    fact(10)
    3628800
    fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''

    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


def create_gbk(length):
    """
    随机生成指定长度的中文字符串
    :param length: 字符串长度
    """
    str_list = []
    for l in range(length):
        # head = random.randint(0xb0, 0xf7)
        head = 0xa0+random.randint(16,56)
        # body = random.randint(0xa1, 0xfe)
        body = 0xa0+random.randint(1,95)
        val = f'{head:x}{body:x}'
        s = bytes.fromhex(val).decode('gb2312', 'ignore')
        str_list.append(s)
    return ''.join(str_list)


# str1 = 'this is my desktop, Is it beautiful?'
# print(str1.upper())
# print(str1.lower())
# print(str1.swapcase())
# print(str1.capitalize())
# print(str1.title())

def synthesis():
    count = int(input('请放入宝石：'))
    while True:
        if count < 3:
            count += int(input('宝石太少，请再放入一些宝石：'))
        else:
            break

    def execute():
        result = count // 3  # 调用外部变量进行整除运算
        print('您放入了%s颗宝石，合成了%s颗高级宝石！' % (count,result))

    return execute

# exe = synthesis() # 调用函数
# print('------------------开始合成------------------')
# exe() #执行闭包内容

lst=['邢佳栋','李学庆','高昊','潘粤明','戴军','薛之谦','贾宏声','于波','李连杰','王斑','蓝雨','刘恩佑','任泉','李光洁','姜文','黑龙','张殿菲','邓超','张杰','杨坤','沙溢','李茂','黄磊','于小伟','刘冠翔','秦俊杰','张琳','陈坤','黄觉','邵峰','陈旭','马天宇','杨子','邓安奇','赵鸿飞','马可','黄海波','黄志忠','李晨','后弦','王挺','何炅','朱亚文','胡军','许亚军','张涵予','贾乃亮','陆虎','印小天','于和伟','田亮','夏雨','李亚鹏','胡兵','王睿','保剑锋','于震','苏醒','胡夏','张丰毅','刘翔','李玉刚','林依轮','袁弘','朱雨辰','丁志诚','黄征','张子健','许嵩']

def get_index(lst, str, lower, upper):
    if lower == upper:
        return upper
    else:
        middle = (lower + upper) // 2
        if str in lst[lower:middle+1]:
            return get_index(lst, str, lower, middle)
        else:
            return get_index(lst, str, middle+1, upper)


# print(get_index(lst, input('请输入姓名：'), 0, len(lst)))
# print(list(filter(lambda x: x[0] == '李', lst)))

str1 = '剩余：599件2瓶'
# print(str1.split('：')[1][0:-3])

def fibonacci(count):
    x = 0  # 定义初始值变量
    y = 1  # 定义初始值变量
    # i = count  # 定义计数变量
    while count > 0:  # 如果计数大于零进行数值计算
        x, y = y, x + y
        count -= 1  # 计数递减
        yield x  # 生成计算结果

print(list(fibonacci(10)))
print(fib(10))
