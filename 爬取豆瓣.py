#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/2 21:40
# @Author  : o_p_q_o
# @File    : 爬取豆瓣.py

import requests
import json

requests = {}
requests['url'] = ''
requests['headers'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'

def film_info(file_name):
    # 定义一个容器来管理不同的start部分
    start_list = [0,20,40,60,76]
    # 定义一个索引 排名 得分最高
    index = 1   # 得分第一
    # 开始操作文件
    with open(file_name,'w',encoding='utf-8') as f:
        # 获取每一个动态请求对应的URL
        for num in start_list:
            url = 'https://movie.douban.com/j/chart/top_list?' \
                  'type=22&interval_id=100%3A90&action=&start=' + str(num) + '&limit=20'
            # 开始发送http请求
            response_json = requests.get(url=url,headers=headers).text
            print(type(response_json))
            response_obj = json.loads(response_json)    # 参数
            for item in response_json:
                rating = eval(item.get('rating'))[0]    # 评分
                url = item.get('url')                   # 影评链接地址
                title = item.get('title')               # 电影名称
                # 信息写入到文件中
                f.write(str(index) + ':' + title + ',' + str(rating) + ',' + url + '\n')
                index += 1                              # 索引自增
        print('电影信息爬取完毕，已经写入文件')

if __name__=='__main__':
    film_info('show_films.txt')