#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 16:40
# @Author  : Bilon
# @File    : 文件常用场景和用法.py

import os

''' 1.文件的处理 '''
# 假设在当前的目录下有一个'abc.txt'
# 重命名文件
os.rename('abc.txt', 'a123.txt')
# 删除文件
os.remove('a123.txt')
# 但是在删除之前最好先判断'a123.txt'是否存在
if os.path.exists('a123.txt'):
    os.remove('a123.txt')

''' 2.文件路径的处理 '''
# 假设有一个文件路径
path = '/users/Python/Data/info.txt'
# 获取路径
print(os.path.dirname(path))    # /users/Python/Data
# 分割文件名
print(os.path.basename(path))   # info.txt
# 分割文件的后缀
print(os.path.split(path))      # ('/users/Python/Data', 'info.txt')

''' 3.创建并访问目录 '''
# 比如创建 test01, test02 目录
os.mkdir('test01')  # 在当前目录下创建一个 test01 目录
os.mkdir('test02')  # 在当前目录下创建一个 test02 目录
# 最好在创建之前先判断目录是否存在，否则会报错
if not os.path.exists('test01'):
    os.mkdir('test01')
if not os.path.exists('test02'):
    os.mkdir('test02')
# 列出当前目录下的所有文件和文件夹
print(os.listdir('.'))
# 有同学说我不知道这个test01是文件还是文件夹啊，不急有高招
print(list(os.walk('.')))   # walk('.')会生成当前目录下的所有文件和目录
# 返回当前的目录
print(os.getcwd())
# 删除空目录
# 若test02里面还有其他文件和目录需要用高级模块shutil来处理
os.rmdir('test02')

''' 4.判断是否为文件或者目录 '''
# 判断是否为文件
print(os.path.isfile('test01'))
# 判断是否为目录
print(os.path.isdir('test01'))
# 判断是否为符号link
print(os.path.islink('link_file'))
# 判断文件或者目录是否存在
print(os.path.exists('test01'))


''' 例子一 '''
# 把 abc1109.txt 里面的内容读出来，写到一个新的文件,格式如下：
# Google    -->     1: Google
# Micrisoft -->     2: Micrisoft
# Baidu     -->     3: Baidu
# Facebook  -->     4: Facebook
def read_file(filepath):    # 把读取文件抽象成一个函数
    with open(filepath, 'r') as f:
        read_lines_from_file = f.readlines()
        return read_lines_from_file

def write_file(newpath, content = list):   # 把写文件抽象成一个函数，传入的参数必须是一个列表
    with open(newpath, 'w') as f:
        f.writelines(content)

new_lines = []
# 遍历列表，把每一行都加上下标
for index, line in enumerate(read_file('abc1109.txt')):
    new_lines.append('{}: {}'.format(str(index+1), line))

# 写入到新文件 new_abc1109.txt
write_file('new_abc1109', new_lines)


''' 例子二 '''
# 文件批量改名
def rename_files():
    file_list = os.listdir('.')     # 列出当前目录下的所有文件
    for file_name in file_list:
        if file_name.endswith('txt'):   # 找出txt文件进行改名
            # 去掉文件名里的数字
            table = str.maketrans('_', '_','0123456789')
            new_file_name = file_name.translate(table)
            os.rename(file_name, new_file_name)

rename_files()
