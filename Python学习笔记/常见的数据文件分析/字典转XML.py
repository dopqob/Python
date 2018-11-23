#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 9:33
# @Author  : Bilon
# @File    : 字典转XML.py
from xml.etree.ElementTree import Element, tostring

d1 = {'name': 'leo', 'age': 30, 'sex': 'male'}
def dict2xml(root, d):
    root_elem = Element(root)
    for key, val in d.items():
        sub_node = Element(key)
        sub_node.text = str(val)    # 一定要把内容的值str化
        root_elem.append(sub_node)
    return root_elem

root = dict2xml('Data', d1)
print(tostring(root))
