#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 16:39
# @Author  : Bilon
# @File    : test_z_output_qywx.py
import logging
import unittest
from HTMLTestRunner import HTMLTestRunner
from ccloud.common.myunit import StartEndQYWX, create_report_file
from ccloud.businessView.output import Output


class OutputTest(StartEndQYWX):
    """APP端出库"""

    def test_single_output(self):
        """单个出库"""
        logging.info('******************** test_single_output ********************')
        o = Output(self.driver)
        o.enter_ccloud(flag=False)
        o.go_mycenter()
        o.enter_output_list()
        o.single_output()
        o.return_home_page()

    def test_batch_output(self):
        """批量出库"""
        logging.info('******************** test_batch_output ********************')
        o = Output(self.driver)
        o.enter_ccloud(flag=False)
        o.go_mycenter()
        o.enter_output_list()
        o.batch_output()
        o.return_home_page()


if __name__ == '__main__':
    file_path = create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))
