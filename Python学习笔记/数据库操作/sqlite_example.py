#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 15:38
# @Author  : Bilon
# @File    : sqlite_example.py
import sqlite3

# 创建/连接数据库
conn = sqlite3.connect('student.db')    # connect()函数 能够创建数据库连接对象，并且当数据库不存在时，创建新的数据库
cur = conn.cursor()     # 创建游标

try:
    # 执行SQL语句 创建score表
    cur.execute('DROP TABLE IF EXISTS score')
    cur.execute('''
    CREATE TABLE score(
        StuId   INTEGER    PRIMARY KEY NOT NULL,
        StuName TEXT    NOT NULL,
        ChineseScore    REAL    DEFAULT 0   CHECK(ChineseScore>=0 AND ChineseScore<=100),
        MathScore   REAL    DEFAULT 0   CHECK(ChineseScore>=0 AND ChineseScore<=100)
        )
    ''')

    # 逐行读取文件并将数据插入score表
    query = 'INSERT INTO score VALUES(?,?,?,?)'  # 定义SQL语句
    with open(r'.\score.txt', encoding='utf-8') as file:  # 打开文件
        for line in file:  # 读取文件每一行
            values = [i.strip("'") for i in line.split(',')]  # 以逗号为分隔符，将每一行内容变为值,去除单引号后存入列表。
            conn.execute(query, values)  # 将列表中的值代入SQL语句，并执行SQL语句。
    conn.commit()

    query1 = 'select * from score'
    cur.execute(query1)
    for _ in range(10):
        print(cur.fetchone())
except:
    raise
finally:
    cur.close()
    conn.close()
