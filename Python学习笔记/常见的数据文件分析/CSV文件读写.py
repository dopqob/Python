#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 14:39
# @Author  : Bilon
# @File    : CSV文件读写.py
import csv

"""
# ==================================
# 读取CSV文件
# ==================================
"""
# 1.用csv里面的reader函数
with open('some.csv', 'r') as f:
    reader = csv.reader(f)

    header = next(reader)
    print(header)

    for row in reader:
        # 对读取出来的每一行进行一些操作
        pass


# 2.我们也可以把数据读到字典中
with open('some.csv', 'r') as rf:
    reader = csv.DictReader(rf)
    # csv里面的DictReader函数可以把文件读成字典列表，通过for循环把每一行都读出来
    # 每一行其实就是一个字典，可以根据key,value灵活处理
    for row_dict in reader:
        print(row_dict)


"""
# ==================================
# 写入CSV文件
# ==================================
"""
with open('some.csv', 'w') as f:
    writer = csv.writer(f)
    content = ['This is the first word written to the file.']
    writer.writerows(content)
