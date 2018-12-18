#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 15:41
# @Author  : Bilon
# @File    : test_order.py
import unittest
from HTMLTestRunner import HTMLTestRunner
from ccloud.common.myunit import StartEnd
from ccloud.businessView.order import Order


class OrderTest(StartEnd):
    """订单相关功能"""

    def test_add_product(self):
        """添加商品"""
        o = Order(self.driver)
        o.enter_ccloud()
        o.add_product(5)

    def test_empty_cart(self):
        """清空购物车"""
        o = Order(self.driver)
        o.enter_ccloud()
        o.add_product(3)
        o.empty_cart()

    def test_order_one_normal(self):
        """普通订单-单一商品"""
        o = Order(self.driver)
        o.enter_ccloud()
        o.add_product(1)
        o.place_order(isgift=False)

    def test_order_one_gift(self):
        """赠品单-单一商品"""
        o = Order(self.driver)
        o.enter_ccloud()
        o.add_product(1)
        o.place_order()

    def test_order_normal(self):
        """普通订单-多种商品"""
        o = Order(self.driver)
        o.enter_ccloud()
        o.add_product(3)
        o.place_order(isgift=False)

    def test_order_gift(self):
        """多种商品-含赠品"""
        o = Order(self.driver)
        o.enter_ccloud()
        o.add_product(3)
        o.place_order()


if __name__ == '__main__':
    file_path = StartEnd.create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))
