#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 15:28
# @Author  : Bilon
# @File    : refund.py
import random
import logging
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error


class Refund(Common):

    # id
    refund_button = 'refund'    # 退货按钮
    date_filter = 'date'        # 日期筛选
    big_num = 'bigNum'          # 大单位输入框
    small_num = 'smallNum'      # 小单位输入框
    confirm_input = 'confirm-input'     # 确认输入
    next_step = 'placeOrder'    # 选好商品后进入下一步
    customers = 'customerInfo'  # 客户
    choose_warehouse = 'warehouseName'  # 选择仓库

    # class
    check_label = 'weui-check_label'


    # xpath
    refund_request = '//p[text()="申请退货"]'   # 进入申请退货
    add_refund = '/html/body/div[1]/a/img'      # 新建自由退货
    num_input = '/html/body/div[5]/input'       # 数量输入框
    choose_customer = '//*[@id="form"]/div[1]/div[1]'   # 选择客户
    submit = '//button[text()="提交订单"]'  # 提交订单
    confirm = '//a[text()="确定"]'    # 二次确认
    no_exchange = '//a[text()="否"]'    # 出现是否退换货时选择否
    goto_refund_list = '//a[text()="查看订单"]'     # 查看退货单列表

    @screenshot_error
    def enter_refund(self):
        """进入申请退货"""
        logging.info('========== enter_refund ==========')
        self.driver.find_element_by_xpath(self.refund_request).click()

    def filter_order(self):
        """查找可退货的订单"""
        logging.info('========== filter_order ==========')
        # 如果今天没有可退货的订单，循环调整时间直到发现可退货的订单
        if not self.is_element_exist(self.refund_button, 'id'):
            i = 1
            while True:
                self.driver.find_element_by_id(self.date_filter).click()
                conditions = self.driver.find_elements_by_class_name(self.check_label)
                conditions[i].click()
                sleep(1)
                if self.is_element_exist(self.refund_button, 'id'):
                    return self.driver.find_element_by_id(self.refund_button)
                i += 1
                if i == len(conditions):
                    break
            return None

        return self.driver.find_element_by_id(self.refund_button)  # 返回待退货订单

    def add_product(self, kinds):
        """
        添加商品到购物车
        :param kinds: 商品种类,默认为1
        """
        logging.info('========== add_product ==========')

        # 选择商品
        big = self.driver.find_elements_by_id(self.big_num)  # 获取所有大单位输入框
        small = self.driver.find_elements_by_id(self.small_num)  # 获取所有小单位输入框
        for k in range(kinds):
            index = random.randint(1, len(big) - 1)
            big[index].click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.num_input))
            self.driver.find_element_by_xpath(self.num_input).clear().send_keys(random.randint(0, 3))
            self.driver.find_element_by_id(self.confirm_input).click()
            sleep(0.5)

            small[index].click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.num_input))
            self.driver.find_element_by_xpath(self.num_input).clear().send_keys(random.randint(1, 4))
            self.driver.find_element_by_id(self.confirm_input).click()
            sleep(0.5)

    @screenshot_error
    def order_refund(self):
        """订单退货"""
        logging.info('========== order_refund ==========')

        order = self.filter_order()
        if order:
            order.click()   # 点击退货按钮
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.submit))
            self.driver.find_element_by_xpath(self.submit).click()  # 提交订单
            self.driver.find_element_by_xpath(self.confirm).click()     # 再次确认
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.no_exchange))
            self.driver.find_element_by_xpath(self.no_exchange).click()     # 点击继续退货按钮
            sleep(1)
        else:
            logging.info('没有可退货的订单')

    @screenshot_error
    def free_refund(self):
        """自由退货"""
        logging.info('========== free_refund ==========')
        self.driver.find_element_by_xpath(self.add_refund).click()
        self.add_product(random.randint(1, 3))
        self.driver.find_element_by_id(self.next_step).click()
        self.driver.find_element_by_xpath(self.choose_customer).click()

        self.swich_webview(self.context)  # 切换到APP视图做swipe操作
        width = self.driver.get_window_size().get('width')  # 获取屏幕宽度
        height = self.driver.get_window_size().get('height')  # 获取屏幕高度
        self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1)  # 上滑加载更多客户
        sleep(3)
        self.swich_webview(self.h5_context)  # 切换到H5视图继续后面的操作

        customers = self.driver.find_elements_by_id(self.customers)  # 获取客户
        index = random.randint(0, len(customers) - 2)  # 这个地方理论上应该-1，但取-1时会报错，-2时不会
        customers[index].click()

        self.driver.find_element_by_id(self.choose_warehouse).click()  # 选择仓库
        warehouses = self.driver.find_elements_by_class_name(self.check_label)
        warehouses[random.randint(0, len(warehouses) - 1)].click()

        self.driver.find_element_by_id(self.next_step).click()  # 确认退货

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.confirm))
        self.driver.find_element_by_xpath(self.confirm).click()  # 下单二次确定

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.goto_refund_list))
        self.driver.find_element_by_xpath(self.goto_refund_list).click()  # 跳转退货单列表


if __name__ == '__main__':
    driver = appium_desired()
    r = Refund(driver)
    r.enter_ccloud()
    r.go_mycenter()
    r.enter_refund()
    r.order_refund()
    # r.free_refund()
