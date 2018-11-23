#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 16:37
# @Author  : Bilon
# @File    : 温度转换(正则).py
import re


"""
# =========================================
# 温度转换
# 以c或C结尾代表输入的是摄氏度，转换为华氏度输出
# 以f或F结尾代表输入的是华氏度，转换为摄氏度输出
# =========================================
"""
content = input('请输入一个温度（摄氏度以C结尾,华氏度以F结尾）:\n').strip()
print('您的输入是: {}'.format(content))

# 只能以 - + 或者数字开头，至多允许出现一次小数点，小数点后必须是数字，最后以C或F结尾
patt = re.compile(r'^([+-]?[0-9]+([.]{1}[0-9]+){0,1})([CF])$')
m = re.match(patt, content)
if m:
    match_group = m.groups()
    print(m.groups())
    temperature = match_group[0]
    if match_group[-1] == 'C':
        # 如果输入的是摄氏度就转换成华氏度
        fahrenheit = (float(temperature)*9/5) + 32
        print('转换后的华氏度: {}℉'.format(fahrenheit))
    else:
        celsius = (float(temperature) - 32)*5/9
        print('转换后的摄氏度: {}℃'.format(celsius))
else:
    print('Sorry, I don\'t understand your input {}'.format(content))