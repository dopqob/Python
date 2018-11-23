#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 9:38
# @Author  : Bilon
# @File    : XML实战.py
from xml.etree.ElementTree import ElementTree, tostring, parse
import urllib.request

url = 'http://www.zhihu.com/rss'    # RSS订阅里面的数据都是标准的XML格式
u = urllib.request.urlopen(url)
print(type(u))
doc = parse(u)  # 用parse把xml数据转成ElementTree对象

top_news = []
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    # print(title)
    link = item.findtext('link')
    if title and link:
        top_news.append(title + '\n' + link)

with open('zhihu_topnews.txt', 'w') as wf:
    for index, each in enumerate(top_news):
        # new_each = each.encode('utf-8')
        # new_each = each.encode('gbk')
        wf.write('{}:\n{}\n'.format(str(index+1), each))
