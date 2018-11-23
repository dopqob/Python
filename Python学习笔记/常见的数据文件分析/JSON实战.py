#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 18:06
# @Author  : Bilon
# @File    : JSON实战.py
"""
# ==============================================
# 获取Github上的最火开源项目
# ==============================================
"""

# 1.获取JSON文件
import json
import requests


def json_demo():
    # 链接已失效
    url = 'https://api.github.com/search/repositories?q=language:python$sort=stars'
    r = requests.get(url)
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def display_each_repo_info(repo_dicts):
    for repo_dict in repo_dicts:
        print('Name: {}'.format(repo_dict['name']))
        print('Owner: {}'.format(repo_dict['owner']['login']))
        print('Stars: {}'.format(repo_dict['stargazers_count']))
        print('created_at: {}'.format(repo_dict['created_at']))
        print('Description: {}'.format(repo_dict['description']))

repo_dicts = json_demo()
display_each_repo_info(repo_dicts)
