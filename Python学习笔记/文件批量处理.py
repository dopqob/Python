#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 15:46
# @Author  : Bilon
# @File    : 文件批量处理.py

""" 1.如何对多个文件中的内容进行替换 """
# ===================================================================
# 当前目录下有2个文件 test01.txt, test02.txt
# 我们需要把里面的Java全部替换为Python，一次搞定怎么做呢
# Python标准库里面有一个很强大的模块 fileinput，允许你循环一个或多个文本文件的内容
# ===================================================================
import fileinput
import glob
import os
import shutil


def update_content():
    """
    利用 glob 模块过滤出当前目录下所有的txt文件
    inplace=1 标准输出，比如print会被重定向到打开文件
    把每一行去掉回车，然后把Java替换为Python
    """
    for line in fileinput.input(glob.glob('*.txt'), inplace=1):
        print(line.strip().replace('Java', 'Python'))
    fileinput.close()   # 关闭文件句柄


""" 2.如何列出全目录结构 """
# =================================================
# 有的时候我们想列出当前目录下所有的文件和子目录
# 不需要用递归去处理，用Python内置的 os.walk() 函数一招搞定
# =================================================
def list_menu_tree():
    path = r'C:\Users\o_p_q_o\PycharmProjects\Python'
    for folder_name, sub_folders, file_names in os.walk(path):

        print('The current folder is : {}'.format(folder_name)) # 列出根目录

        for sub_folder in sub_folders:  # 列出子目录
            print(' ' * 10 + 'Subfolder of {} : {}'.format(folder_name, sub_folder))

        for filename in file_names: # 列出文件
            print(' ' * 20 + 'File inside {} : {}'.format(folder_name, filename))


""" 3.如何把多个文件copy到另外一个目录下"""
# ======================================================
# 有的时候我们需要把一个或者多个文件备份到另外一个目录下
# Python提供了一个高级文件模块 shutil
# 如果是要拷贝目录 用 shutil.copytree('folder', 'newfolder')
# 会自动创建 newfolder 文件夹并将 folder下的文件全部拷过去
# ======================================================
def copy_file():
    for file in os.listdir('.'):    # 列出当前目录的所有文件
        if os.path.splitext(file)[1] == '.txt': # 过滤出txt文件
            shutil.copy(file, os.path.join('backup', file)) # copy到backup目录下面


""" 4.删除目录以及所有子目录的文件 """
# ========================================
# 删除空目录用 os.rmdir('folder')
# 如果目录下有文件，用 shutil.rmtree('folder')
# ========================================
shutil.rmtree('backup')


