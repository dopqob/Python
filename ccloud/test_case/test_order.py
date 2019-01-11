#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 15:41
# @Author  : Bilon
# @File    : test_order.py
import logging
import unittest
from HTMLTestRunner import HTMLTestRunner
from ccloud.common.myunit import StartEnd
from ccloud.businessView.order import Order


class OrderTest(StartEnd):
    """订单相关功能"""

    def test_add_product(self):
        """添加商品"""
        logging.info('******************** test_add_product ********************')
        o = Order(self.driver)
        o.enter_ccloud()
        o.enter_normal_order()
        o.add_product(3)

    def test_empty_cart(self):
        """清空购物车"""
        logging.info('******************** test_empty_cart ********************')
        o = Order(self.driver)
        o.enter_ccloud()
        o.enter_normal_order()
        o.add_product(3)
        o.empty_cart()

    # @unittest.skip('')
    def test_order_one_normal(self):
        """普通订单-单一商品"""
        logging.info('******************** test_order_one_normal ********************')
        o = Order(self.driver)
        o.enter_ccloud()
        o.enter_normal_order()
        o.add_product()
        o.place_order(isgift=False)
        self.assertEqual(self.driver.title, '我的订单')

    # @unittest.skip('')
    def test_order_one_gift(self):
        """普通订单-赠品单-单一商品"""
        logging.info('******************** test_order_one_gift ********************')
        o = Order(self.driver)
        o.enter_ccloud()
        o.enter_normal_order()
        o.add_product()
        o.place_order()
        self.assertEqual(self.driver.title, '我的订单')

    # @unittest.skip('')
    def test_order_variety_normal(self):
        """普通订单-多种商品"""
        logging.info('******************** test_order_variety_normal ********************')
        o = Order(self.driver)
        o.enter_ccloud()
        o.enter_normal_order()
        o.add_product(3)
        o.place_order(isgift=False)
        self.assertEqual(self.driver.title, '我的订单')

    # @unittest.skip('')
    def test_order_variety_gift(self):
        """普通订单-多种商品-含赠品"""
        logging.info('******************** test_order_variety_gift ********************')
        o = Order(self.driver)
        o.enter_ccloud()
        o.enter_normal_order()
        o.add_product(3)
        o.place_order()
        self.assertEqual(self.driver.title, '我的订单')

    def test_mashup_one_normal(self):
        """聚合订单-单一商品"""
        logging.info('******************** test_mashup_one_normal ********************')
        o = Order(self.driver)
        o.enter_ccloud()
        o.go_func_group_page()
        o.enter_mashup_order()
        o.add_product()
        o.mashup_order(isgift=False)

    def test_mashup_one_gift(self):
        """聚合订单-赠品单-单一商品"""
        logging.info('******************** test_mashup_one_gift ********************')
        o = Order(self.driver)
        o.enter_ccloud()
        o.go_func_group_page()
        o.enter_mashup_order()
        o.add_product()
        o.mashup_order()

    def test_mashup_variety_normal(self):
        """聚合订单-多种商品"""
        logging.info('******************** test_mashup_variety_normal ********************')
        o = Order(self.driver)
        o.enter_ccloud()
        o.go_func_group_page()
        o.enter_mashup_order()
        o.add_product(3)
        o.mashup_order(isgift=False)

    def test_mashup_variety_gift(self):
        """聚合订单-多种商品-含赠品"""
        logging.info('******************** test_mashup_variety_gift ********************')
        o = Order(self.driver)
        o.enter_ccloud()
        o.go_func_group_page()
        o.enter_mashup_order()
        o.add_product(3)
        o.mashup_order()


if __name__ == '__main__':
    file_path = StartEnd.create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))
