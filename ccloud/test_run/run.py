#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 14:03
# @Author  : Bilon
# @File    : run.py
import unittest
from HTMLTestRunner import HTMLTestRunner
from ccloud.common.myunit import StartEnd


# 用例目录
dir = '../test_case'

# 加载测试用例，目录下以 "test" 开头的 ".py"文件
discover = unittest.defaultTestLoader.discover(dir, pattern='test*.py')

# 报告输出路径
file = StartEnd.create_report_file()

# 运行用例并生成测试报告
with open(file, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:')
    runner.run(discover)

