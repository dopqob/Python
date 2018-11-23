#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 9:12
# @Author  : Bilon
# @File    : XML生成.py
"""
# ==============================================
# 比如要生成如下的XML的数据结构
# <?xml version = "1.0" encoding = "utf-8"?>
# <data>
#     <people name="jack">
#         <age>30</age>
#         <sex>male</sex>
#     </people>
# </data>
# 分如下几步
# ==============================================
"""
# 1.引入几个重要模块Element,ElementTree,tostring
from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, ElementTree, tostring

# 2.先创建根节点
root = Element('Data')

# 3.再创建子节点people，并设置它的属性
node = Element('people')
node.set('name', 'jack')

# 4.再创建子节点里面的两个孙节点
sub_node = Element('age')
sub_node.text = '30'    # 数字30一定要写成字符串，不能是数字

sub_node2 = Element('sex')
sub_node2.text = 'male'

# 5.把所有的Element串起来
node.append(sub_node)
node.append(sub_node2)
root.append(node)
print(tostring(root))   # tostring()可以把xml数据方便的转成str，然后打印出来

# 6.生成xml文件
et = ElementTree(root)
et.write('demo.xml')

# 7.美化打印
dom = parseString(tostring(root))
print(dom.toprettyxml('    ', encoding='UTF-8'))    # 第一个参数是缩进空格的数量
