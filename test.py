#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 11:17
# @Author  : Bilon
# @File    : test.py

# import random
# i = random.randint(0,2-1)
# print(i)
# list1 = [0, 0, 1]
# list2 = list1[:10]
# print(list2)

# line = 'hello world; python, I ,like,    it'
# import re
# print(re.split(r'[;,]', line))
# print(re.split(r'[;,]\s*', line))
# print(re.split(r'[;,s]\s*', line))
# print(re.split(r'\s*[;,s]\s*', line))
# import re
# from bs4 import BeautifulSoup
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# def explain(msg):
#     print('-'*20 + msg + '-'*20)
#
# # print('-'*20 + '获取所有连接' + '-'*20)
# explain('获取所有连接')
# links = soup.find_all('a')
# for link in links:
#     print(link.name, link['href'], link.get_text())
#
# explain('获取Lacie的链接')
# link_node = soup.find(id="link2")
# # link_node = soup.select('#link2')
# print(link_node.name, link_node['href'], link_node.get_text())
#
# explain('正则匹配')
# link_node = soup.find('a', href=re.compile(r'ill'))
# print(link_node.name, link_node['href'], link_node.get_text())
#
# explain('获取P段落文字')
# p_node = soup.find('p', class_='title')
# print(p_node.name, p_node.get_text())

aInfo={'Wangdachui':3000,'NiuYun':2000,'LinLing':4500,'Tianqi':8000}
template='''
Welcome to the pay wall.
NiuYun' salary is %(NiuYun)s.
Wangdachui's salary is %(Wangdachui)s.
'''
print(template%aInfo)

template1=f'''
Welcome to the pay wall.
NiuYun' salary is {aInfo['NiuYun']}.
Wangdachui's salary is {aInfo['Wangdachui']}.
'''
# print(aInfo['NiuYun'])
# print(template1.format(aInfo['NiuYun'], aInfo['Wangdachui']))
print(template1)