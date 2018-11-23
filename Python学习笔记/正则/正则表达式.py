#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 15:27
# @Author  : Bilon
# @File    : 正则表达式.py

"""
# ======================================
符号          功能
^            匹配一行的开头位置
$            匹配一行的结束位置
\b           匹配单词的边界
.            匹配单个任意字符
[]           匹配单个列出的字符
[^]          匹配单个未列出的字符
?            容许匹配一次，但非必须
*            匹配 0~任意次
+            匹配 1~任意次
{min,max}    至少min次，至多max次
"""
import re

str = 'cative'
patt = re.compile(r'^cat')
print(re.match(patt, str))

"""
1.匹配以c开头的
patt=re.compile(r'^cat')

2.以BR或者Bestregards结尾的
patt=re.compile(r'(BR|Bestregards)$')

3.#匹配包含有'the'的字符串
\bthe         #匹配任何以'the'开始的字符串
\bthe\b       #仅仅匹配单词'the'
\Bthe         #匹配任意包含'the'但不以'the'开头的单词

4.匹配'grey'或者'gray'
patt=re.compile(r'gr[ea]y')

5.用'|'来匹配任意子表达式
'am'|'pm'

6.比如6月4号，这个6月可能写成'June'也可以写成'Jun',而且日期也有可能写作'fourth'或者'4th'或者4
第一部分:(June|Jun)改为(June?),什么意思呢
意思是说'?'出现在一个e后面，表示e是可选的
第二部分:(fourth|4th|4)改为(fourth|4(th)?),什么意思呢
意思是说'?'出现在一个括号后面,表示这个括号内的内容是可选的
最后变成 June?(fourth|4(th)?)

7.重复出现用+和*表示,但是二者有一些小的区别
+加号表示: 前面紧邻的元素出现一次或者多次，也就是至少出现一次
*星号表示: 前面紧邻的元素出现任意多次，或者不出现
a*          #匹配a,aa,aaa,...还有'' 
a+          #匹配a,aa,aaa,...

8.匹配内容重复出现的次数
patt=re.compile(r'.*a{3}')      a字母重复出现三次
patt=re.compile(r'([1-9]{3})')  连续三次出现1-9之间的任意数字

9.找出字母 g 后面不是 u 或 i 的单词
patt = re.compile(r'.*g[^ui]')

10.只能输入整数或小数的正则表达式
patt = re.compile(r'^[0-9]+([.]{1}[0-9]+){0,1}$')
"""