#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 17:31
# @Author  : Bilon
# @File    : 异常处理.py

"""
# ======================================
#          9种常见的异常
# --------------------------------
# 1.不存在的变量 NameError
# 2.函数或方法名错误：AttributeError
# 3.索引越界：IndexError
# 4.语法错误：SyntaxError
# 5.变量类型错误：TypeError
# 6.数据类型错误：ValueError
# 7.访问未初始化的本地变量：UnboundLocalError
# 8.打开不存在的文件：IOError
# 9.除数为0：ZeroDivisionError
# ======================================
"""
import random


# 捕捉单个数据类型错误异常
num = random.randint(1, 10)
while True:
    try:
        guess = int(input('Enter 1~10:'))
    except Exception as e:
        print(e)
        print('Input error! Please enter num(1~10):')
        continue
    if guess > num:
        print('guess Bigger : ', guess)
    elif guess < num:
        print('guess Smaller : ', guess)
    else:
        print('Great,You guess correct.Game Over!')
        break


"""
# =====================================================
#                   主动抛出异常
# 语法：raise SomeException('Error')
# 参数SomeException是触发异常的名字，必须是一个字符串、类或者实例
# 参数'Error' 描述异常信息的元组，一般我们用字符串表示异常的原因
# =====================================================
"""
try:
    for i in range(1, 5):
        if i > 3:
            raise ValueError('i>3')
        else:
            print(i)
except ValueError as e:
    print('catch the value error: ', e)


"""
# =================================
# 利用assert（断言）来发现问题
# 语法：assert expression, "Error"
# expression：是一个条件判断表达式
# "Error"：是对条件判断出现错误的描述信息
# =================================
"""
x = 10
y = 20
assert x == y, 'x not equal y'


"""
# ================================
#     处理多个异常
# 可以分开处理
# 可以用一个代码块来处理
# ================================
"""
try:
    f = open('123.txt')
    line = f.read()
    num = int(line)
    print('read num = %d'%num)
except IOError as e:    # 捕捉文件不存在异常
    print('We catch IOError:', e)
except ValueError as e:     # 捕捉参数类型错误异常
    print('We catch ValueError:', e)
else:
    print('No error happend')
finally:
    print('Close file')
    # f.close()

try:
    f = open('123.txt')
    line = f.read()
    num = int(line)
    print('read num = %d'%num)
except (IOError, ValueError) as e:
    print('We catch error:', e)
else:
    print('No error happend')
finally:
    print('Close file')
    # f.close()
