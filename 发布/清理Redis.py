#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 20:52
# @Author  : Bilon
# @File    : 清理Redis.py

from redis import Redis
host = '116.62.170.64'
port = 6380
pwd = 'Jiayan@2018*hjx'
db = 0

r = Redis(host, port, pwd, decode_responses=True)
