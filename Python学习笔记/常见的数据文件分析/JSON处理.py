#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 17:20
# @Author  : Bilon
# @File    : JSON处理.py
import json

"""
# ===========================================
# Python中处理Json的4个重要函数
# 1.dumps() 2.loads() 3.dump() 4.load()
#
#           转换前后对比
#   Python              JSON
#   dict                object
#   list,tuple          array
#   str,unicode         string
#   int,float           number
#   True                true
#   False               false
#   None                null
# ===========================================
"""

"""
# ===========================================
# 1.dumps()   把Python数据转换成Json数据
# ===========================================
"""
def python_to_json():
    python_data = {'name': 'Leo', 'sex': 'man', 'other': None, 'is': True}
    converted_date = json.dumps(python_data)
    print(type(converted_date))
    print(converted_date)

python_to_json()

# dumps()里面还有一些其他的参数，比如可以去掉一些空的字符
list1 = [10, 20, 'abc', {'name': 'Leo', 'age': 20}]
print(json.dumps(list1, separators=(',', ':')))

# 输出的字典的键值排序
list2 = {'c': 0, 'b': 0, 'a': 0}
print(json.dumps(list2, sort_keys=True))


"""
# ===========================================
# 2.loads()   把Json数据转换成Python数据
# ===========================================
"""
def json_to_python():
    json_data = '{"name": "Lili", "isMan": false, "w": 100, "IQ": null}'
    converted_date = json.loads(json_data)
    print(type(converted_date))
    print(converted_date)

json_to_python()


"""
# ==============================================================================
# 3.dump()
# dump()函数和dumps()函数的区别在于dump文件把python数据写到json文件里面，里面会多一个文件句柄
# ==============================================================================
"""
with open('demo.json', 'wb') as wf:
    python_dict = {'a': 'Hi', 'b': 'Python', 'c': True, 'd': None}
    json.dump(python_dict, wf)


"""
# ==============================================================================
# 3.load()
# load()和loads()函数的差别也是一个读json数据，一个是读json文件句柄
# ==============================================================================
"""
with open('demo.json', 'rb') as rf:
    print(json.load(rf))
