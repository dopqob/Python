#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 11:29
# @Author  : Bilon
# @File    : output.py
import logging
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error


class Output(Common):

    # id
    status_filter = 'status'    # 订单状态筛选
    date_filter = 'date'        # 日期筛选
    stock_out = 'allOut'        # 单个订单出库
    batch = 'batchOutStock'     # 批量出库

    # class
    check_label = 'weui-check_label'
    order_list = 'list-layer'   # 订单列表

    # xpath
    delivery_list = '//p[text()="出库单"]'     # 进入出库单
    confirm = '//a[text()="确定"]'            # 单个退货二次确认
    batch_confirm = '//span[text()="确认"]'   # 批量退货二次确认

    @screenshot_error
    def enter_output_list(self):
        """进入出库单列表"""
        logging.info('========== enter_output_list ==========')
        self.driver.find_element_by_xpath(self.delivery_list).click()

    def filter_order(self):
        """筛选待出库的订单"""
        logging.info('========== filter_order ==========')
        self.driver.find_element_by_id(self.status_filter).click()  # 点击订单状态
        self.driver.find_elements_by_class_name(self.check_label)[1].click()  # 选择待出库
        sleep(1)

        # 如果今天没有待出库的订单，循环调整时间直到发现待出库的订单
        if not self.driver.find_elements_by_class_name(self.order_list):
            i = 1
            while True:
                self.driver.find_element_by_id(self.date_filter).click()
                conditions = self.driver.find_elements_by_class_name(self.check_label)
                conditions[i].click()
                sleep(1)
                if self.driver.find_elements_by_class_name(self.order_list):
                    return self.driver.find_elements_by_class_name(self.order_list)
                i += 1
                if i == len(conditions):
                    break

        return self.driver.find_elements_by_class_name(self.order_list)  # 待出库订单列表

    @screenshot_error
    def single_output(self):
        """APP单个出库"""
        logging.info('========== single_output ==========')
        order_list = self.filter_order()
        if order_list:  # 如果存在待出库的订单
            order_list[0].click()   # 点击第一个订单展开详情
            sleep(0.5)
            self.driver.find_element_by_id(self.stock_out).click()  # 点击出库
            sleep(0.5)
            self.driver.find_element_by_xpath(self.confirm).click()     # 确认
        else:
            logging.info('没有待出库的订单')

    @screenshot_error
    def batch_output(self):
        """APP批量出库"""
        logging.info('========== batch_outbound ==========')
        order_list = self.filter_order()
        if order_list:
            self.driver.find_element_by_id(self.batch).click()
            self.driver.find_element_by_xpath(self.batch_confirm).click()
            sleep(3)
        else:
            logging.info('没有待出库的订单')


if __name__ == '__main__':
    driver = appium_desired()
    o = Output(driver)
    o.enter_ccloud()
    o.go_mycenter()
    o.enter_output_list()
    o.single_output()
    # o.batch_output()
    o.return_home_page()
