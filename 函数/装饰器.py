#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 15:53
# @Author  : Bilon
# @File    : 装饰器.py

'''柯里化和装饰器'''

'''
什么是柯里化
指的是将原来接受两个参数的函数变成接受一个参数的新函数的过程
新的函数返回一个以原有第二个参数为参数的函数
z = f(x,y)转换成 z = f(x)(y)
'''

# 将下面加法代码柯里化
# def add(x,y):
#     return x + y
#
# print(add(4,5))
#
# def new_add(x):
#     def inner(y):
#         return x + y
#     return inner
#
# print(new_add(4)(5))


'''
装饰器
对原有业务函数进行一定的增强，在业务函数的前面或后面添加一些功能（比如记录日志，计算耗时，判断参数是否合法等等）
'''

'''无参装饰器'''
import datetime
import time

# 装饰器函数
def logger(func):
    def wrapper(*args, **kwargs):
        # 在业务函数前添加一些功能
        print('args={}, kwargs={}'.format(args, kwargs))
        start = datetime.datetime.now()     # 计时器开始时间

        # 业务函数
        busfunc = func(*args, **kwargs)

        # 在业务函数后面添加一些功能
        delta = (datetime.datetime.now() - start).total_seconds()   # 时间增值 业务函数执行时间
        print('{} 执行耗时 {}秒'.format(func.__name__, delta))

        return busfunc
    return wrapper


# 业务函数
@logger     # 等价于 add = logger(multiply)
def multiply(x,y):
    time.sleep(2)
    return x * y

# 常规调用
# foo = logger(multiply)
# print(foo(4,5))

# 演变
# multiply = logger(multiply)
print(multiply(4,5))


'''带参装饰器'''
from functools import wraps
import logging

def logged(level, name=None, message=None):
    '''
    Add logging to a function.level is the logging level,
    name is the logger name, and message is the log message.
    If name and message aren't specified, they default to the
    function's module and name
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG)
def add(x,y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

print(add(5,6))
spam()