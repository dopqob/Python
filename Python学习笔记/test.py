#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 17:30
# @Author  : Bilon
# @File    : test.py

import random

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