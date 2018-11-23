#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 16:15
# @Author  : Bilon
# @File    : CSV实战.py
import urllib.request   # Python3.7的urlretrieve函数在urllib.request模块里，而Python2.7直接在urllib模块里
import csv


# 首先用urllib.request模块里的urlretrieve()方法抓取五粮液股票的csv文件
# 这是一个20年的五粮液成交记录，是一个很大的csv文件
# 第一行是头部信息，分 日期/开盘价/最高价/最低价/收盘价/成交量/已调整的收盘价
url = 'http://table.finance.yahoo.com/table.csv?s=000858.sz'    # 这个URL已经被封了，访问不了
urllib.request.urlretrieve(url, 'WuLiangYe.csv')

with open('WuLiangYe.csv') as rf:
    """
    获取二十年来的股票成交量超过2亿元的数据，然后写入到一个新的csv文件里
    """
    read_csv = csv.reader(rf)
    header = next(read_csv)

    with open('new_WuLiangYe.csv', 'wb') as wf:
        writer_csv = csv.writer(wf)
        writer_csv.writerow(header)

        for row in read_csv:
            if int(row[5]) >= 200000000:
                writer_csv.writerow(row)


with open('WuLiangYe.csv') as rf:
    """
    获取五粮液近20年的最高收盘价和对应的日期
    """
    read_csv = csv.reader(rf)   # 清洗数据，去掉头部
    stock_dict = {row[0]: float(row[4]) for row in list(read_csv)[1:]}   # 迭代器转成列表，并把日期和古交
    high_price = max(stock_dict.values())

    for k, v in stock_dict.items():
        if v == high_price:
            print(k, v)
