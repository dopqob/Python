#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 9:41
# @Author  : Bilon
# @File    : test_customer.py
import logging
import unittest
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from ccloud.common.myunit import StartEnd
from ccloud.businessView.customer import Customer


class CustomerTest(StartEnd):
    """客户、拜访"""

    def test_add_customer_with_photo(self):
        """新增客户-带照片"""
        logging.info('******************** test_add_customer_with_photo ********************')
        c = Customer(self.driver)
        c.enter_ccloud()
        c.add_customer()
        sleep(3)
        self.assertEqual(self.driver.title, '客户列表')

    def test_add_customer_without_photo(self):
        """新增客户-不带照片"""
        logging.info('******************** test_add_customer_without_photo ********************')
        c = Customer(self.driver)
        c.enter_ccloud()
        c.add_customer(photo=False)
        self.assertEqual(self.driver.title, '客户列表')

    def test_customer_visit(self):
        """客户拜访"""
        logging.info('******************** test_customer_visit ********************')
        c = Customer(self.driver)
        c.enter_ccloud()
        c.go_func_group_page()
        c.customer_visit()
        self.assertEqual(self.driver.title, '选择客户')


if __name__ == '__main__':
    file_path = StartEnd.create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))
