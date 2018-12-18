#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 16:38
# @Author  : Bilon
# @File    : mysql数据库.py
import mysql.connector


conn = mysql.connector.connect(user='root', password='123456', database='test')
cursor = conn.cursor()

# 创建user表：
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录
# cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'dong'])
# print(cursor.rowcount)

# 提交事务
# conn.commit()
# cursor.close()


# 运行查询
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)   # 查询结果

# 关闭cursor和connection
cursor.close()
conn.close()
