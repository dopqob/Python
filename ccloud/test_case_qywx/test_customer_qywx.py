#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 9:41
# @Author  : Bilon
# @File    : test_customer_qywx.py
import logging
import unittest
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from ccloud.common.myunit import StartEndQYWX, create_report_file
from ccloud.businessView.customer import Customer


class CustomerTest(StartEndQYWX):
    """客户/拜访"""

    def test_add_customer_with_photo(self):
        """新增客户-带照片"""
        logging.info('******************** 新增客户-带照片 ********************')
        c = Customer(self.driver)
        c.enter_ccloud(flag=False)
        c.add_customer()
        sleep(3)
        self.assertEqual(self.driver.title, '客户列表')

    def test_add_customer_without_photo(self):
        """新增客户-不带照片"""
        logging.info('******************** 新增客户-不带照片 ********************')
        c = Customer(self.driver)
        c.enter_ccloud(flag=False)
        c.add_customer(photo=False)
        self.assertEqual(self.driver.title, '客户列表')

    def test_customer_visit(self):
        """常规拜访"""
        logging.info('******************** 常规拜访 ********************')
        c = Customer(self.driver)
        c.enter_ccloud(flag=False)
        c.go_func_group_page()
        c.customer_visit(flag=False)
        c.return_home_page()

    def test_customer_visit_supplement(self):
        """常规拜访-补录"""
        logging.info('******************** 常规拜访-补录 ********************')
        c = Customer(self.driver)
        c.enter_ccloud(flag=False)
        c.go_func_group_page()
        c.customer_visit_supplement(flag=False)
        c.return_home_page()


if __name__ == '__main__':
    file_path = create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))
