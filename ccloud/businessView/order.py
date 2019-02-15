#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 11:37
# @Author  : Bilon
# @File    : order.py
import random
import logging
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error


class Order(Common):

    # id
    total_num_id = 'totalNum'   # 合计数量
    big_num_id = 'bigNum'       # 大单位输入框
    small_num_id = 'smallNum'   # 小单位输入框
    confirm_input_id = 'confirm-input'  # 确认输入
    shopping_cart_id = 'shoppingCart'  # 购物车
    add_goods_id = 'addGoods'  # 添加商品
    gift_id = 'isGift'  # 赠品勾选框
    place_order_id = 'placeOrder'  # 商品页面的下单按钮
    customer_info_id = 'customerInfo'  # 客户
    submit_order_id = 'placeOrder'  # 提交订单
    mashup_order_id = 'order'   # 聚合下单入口
    visit_complete_id = 'visitEnd'  # 拜访完成按钮

    # class
    del_class = 'icon-trash-o'  # 删除商品

    # xpath
    order_enter_xpath = '//*[@id="home"]/div[3]/div[2]/a[1]'    # 首页下订单入口
    num_input_xpath = '/html/body/div[5]/input'     # 商品数量输入
    del_confirm_xpath = '//a[text()="确定"]'  # 删除确认
    customer_xpath = '//*[@id="form"]/div[1]/div[1]'  # 选择客户按钮
    order_confirm_xpath = '/html/body/div[4]/div[3]/a[2]'  # 下单二次确认
    goto_orderlist_xpath = '/html/body/div[4]/div[2]/a[1]'  # 跳转订单列表
    visit_complete_confirm = '//a[contains(text(),"确定")]'  # 拜访完成二次确认

    def enter_normal_order(self):
        """通过首页进入下单页面"""

        logging.info('========== enter_normal_order ==========')
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.order_enter_xpath))
        self.driver.find_element_by_xpath(self.order_enter_xpath).click()

    @screenshot_error
    def add_product(self, kinds=1):
        """
        添加商品到购物车
        :param kinds: 商品种类,默认为1
        """
        logging.info('========== add_product ==========')

        # 查看合计数量，如果数量不为0，先进购物车清空商品
        content = self.driver.find_element_by_id(self.total_num_id).text
        if content[1] != '0':
            self.empty_cart()

        # 选择商品
        big = self.driver.find_elements_by_id(self.big_num_id)  # 获取所有大单位输入框
        small = self.driver.find_elements_by_id(self.small_num_id)  # 获取所有小单位输入框
        if big:
            for k in range(kinds):
                sleep(0.5)
                index = random.randint(1, len(big) - 1)
                big[index].click()
                WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.num_input_xpath))
                self.driver.find_element_by_xpath(self.num_input_xpath).clear().send_keys(random.randint(0, 3))
                self.driver.find_element_by_id(self.confirm_input_id).click()

                sleep(0.5)
                small[index].click()
                WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.num_input_xpath))
                self.driver.find_element_by_xpath(self.num_input_xpath).clear().send_keys(random.randint(1, 4))
                self.driver.find_element_by_id(self.confirm_input_id).click()

    # @screenshot_error
    def empty_cart(self):
        """ 清空购物车 """

        logging.info('========== empty_cart ==========')

        if self.driver.title == '产品列表':
            self.driver.find_element_by_id(self.shopping_cart_id).click()

            # 通过循环删除购物车所有商品
            if self.driver.title == '购物车':
                del_icons = self.driver.find_elements_by_class_name(self.del_class)
                for icon in del_icons:
                    icon.click()
                    self.driver.find_element_by_xpath(self.del_confirm_xpath).click()
                    sleep(0.5)

                self.driver.find_element_by_id(self.add_goods_id).click()  # 返回商品列表

    # @screenshot_error
    def add_gift(self):
        """ 随机将购物车商品设为赠品 """

        logging.info('========== add_gift ==========')

        if self.driver.title == '产品列表':
            self.driver.find_element_by_id(self.shopping_cart_id).click()

            # 获取所有的赠品框，随机勾选
            if self.driver.title == '购物车':
                gift_icons = self.driver.find_elements_by_name(self.gift_id)
                gift_icons[random.randint(0, len(gift_icons) - 1)].click()

                self.driver.find_element_by_id(self.add_goods_id).click()  # 返回商品列表

    @screenshot_error
    def place_order(self, isgift=True):
        """首页下单"""

        logging.info('========== place_order ==========')
        if isgift:
            sleep(0.5)
            self.add_gift()

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.place_order_id))
        self.driver.find_element_by_id(self.place_order_id).click()  # 下单

        # 选择客户按钮
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.customer_xpath))
        self.driver.find_element_by_xpath(self.customer_xpath).click()

        self.swich_webview(self.context)  # 切换到APP视图做swipe操作
        width = self.driver.get_window_size().get('width')  # 获取屏幕宽度
        height = self.driver.get_window_size().get('height')  # 获取屏幕高度
        self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1)  # 上滑加载更多客户
        sleep(1)
        self.swich_webview(self.h5_context)  # 切换到H5视图继续后面的操作

        customers = self.driver.find_elements_by_id(self.customer_info_id)  # 获取客户
        index = random.randint(0, len(customers) - 2)  # 这个地方理论上应该-1，但取-1时会报错，-2时不会
        customers[index].click()

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.submit_order_id))
        self.driver.find_element_by_id(self.submit_order_id).click()  # 提交订单

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.order_confirm_xpath))
        self.driver.find_element_by_xpath(self.order_confirm_xpath).click()  # 下单二次确定

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.goto_orderlist_xpath))
        self.driver.find_element_by_xpath(self.goto_orderlist_xpath).click()  # 跳转订单列表

    @screenshot_error
    def enter_mashup_order(self):
        """进入聚合下单"""

        logging.info('========== enter_mashup_order ==========')
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(self.mashup_order_id))
        self.driver.find_element_by_id(self.mashup_order_id).click()

    @screenshot_error
    def mashup_order(self, isgift=True):
        """聚合下单"""

        logging.info('========== mashup_order ==========')
        if isgift:
            sleep(0.5)
            self.add_gift()

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.place_order_id))
        self.driver.find_element_by_id(self.place_order_id).click()  # 下单

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.submit_order_id))
        self.driver.find_element_by_id(self.submit_order_id).click()  # 提交订单

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.order_confirm_xpath))
        self.driver.find_element_by_xpath(self.order_confirm_xpath).click()  # 下单二次确定

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.visit_complete_id))
        self.driver.find_element_by_id(self.visit_complete_id).click()  # 点击拜访完成按钮
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath(self.visit_complete_confirm))
        self.driver.find_element_by_xpath(self.visit_complete_confirm).click()
        sleep(1)


if __name__ == '__main__':
    driver = appium_desired()
    order = Order(driver)
    flag = [True, False]
    order.enter_ccloud()
    for i in range(3):
        order.enter_normal_order()
        order.add_product(random.randint(1, 3))
        order.place_order(isgift=random.choice(flag))
        order.return_home_page()

        # order.go_func_group_page()
        # order.enter_mashup_order()
        # order.add_product(random.randint(1, 3))
        # order.mashup_order(isgift=random.choice(flag))
        # order.return_home_page()
    # order.add_product(3)
    # order.empty_cart()
