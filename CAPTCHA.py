#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 10:28
# @Author  : Bilon
# @File    : CAPTCHA.py

import random
# 生成随机验证码(由数字和大小写字母组成)
def getrand(num, many): #num:验证码长度  many:验证码个数
    for i in range(many):
        s = ''
        for i in range(num):
            n = random.randint(1, 2)        # 1是数字 2是字母
            # 为数字时从0-9随机生成一个转为字符串放进去
            if n == 1:
                num1 = random.randint(0, 9)
                s += str(num1)
            else:
                nn = random.randint(1, 2)   # 1是大写字母 2是小写字母
                num2 = random.randint(1, 26)
                if nn == 1:
                    s = s + chr(64 + num2)
                else:
                    s = s + chr(96 + num2)
        print (s)
getrand(8,5)