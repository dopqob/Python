#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 9:41
# @Author  : Bilon
# @File    : test_customer.py
import unittest
from HTMLTestRunner import HTMLTestRunner
from ccloud.common.myunit import StartEnd
from ccloud.businessView.customer import Customer


class CustomerTest(StartEnd):
    """客户：新增客户、客户拜访"""

    def test_add_customer(self):
        """新增客户"""
        c = Customer(self.driver)
        c.enter_ccloud()
        c.add_customer()

    def test_customer_visit(self):
        """客户拜访"""
        c = Customer(self.driver)
        c.enter_ccloud()
        c.go_func_group_page()
        c.customer_visit()


if __name__ == '__main__':
    file_path = StartEnd.create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))
