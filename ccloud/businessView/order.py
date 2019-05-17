#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 11:37
# @Author  : Bilon
# @File    : order.py
import random
import logging
from time import sleep
from selenium.webdriver.common.by import By
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error


class Order(Common):
    ELEMENT = {
        '合计数量': (By.ID, 'totalNum'),
        '大单位输入框': (By.ID, 'bigNum'),
        '小单位输入框': (By.ID, 'smallNum'),
        '确认输入': (By.ID, 'confirm-input'),
        '购物车': (By.ID, 'shoppingCart'),
        '添加商品': (By.ID, 'addGoods'),
        '勾选赠品': (By.NAME, 'isGift'),
        '下单': (By.ID, 'placeOrder'),
        '侧边客户列表': (By.ID, 'combin-filter'),
        '客户': (By.ID, 'customerInfo'),
        '提交订单': (By.ID, 'placeOrder'),
        '聚合下单': (By.ID, 'order'),
        '拜访完成': (By.ID, 'visitEnd'),
        '删除商品': (By.CLASS_NAME, 'icon-trash-o'),
        '首页下单': (By.XPATH, '//*[@id="home"]/div[3]/div[2]/a[1]'),
        '输入商品数量': (By.XPATH, '/html/body/div[5]/input'),
        '删除确认': (By.XPATH, '//a[text()="确定"]'),
        '选择客户': (By.XPATH, '//*[@id="form"]/div[1]/div[1]'),
        '下单二次确认': (By.XPATH, '/html/body/div[4]/div[3]/a[2]'),
        '跳转订单列表': (By.XPATH, '/html/body/div[4]/div[2]/a[1]'),
        '拜访完成二次确认': (By.XPATH, '//a[contains(text(),"确定")]'),
    }

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
        self.click(self.ELEMENT['首页下单'])

    @screenshot_error
    def add_product(self, kinds=1):
        """
        添加商品到购物车
        :param kinds: 商品种类,默认为1
        """
        logging.info('========== add_product ==========')

        # 查看合计数量，如果数量不为0，先进购物车清空商品
        content = self.find_element(self.ELEMENT['合计数量']).text
        if content[1] != '0':
            self.empty_cart()

        # 选择商品
        big = self.find_elements(self.ELEMENT['大单位输入框'])  # 获取所有大单位输入框
        small = self.find_elements(self.ELEMENT['小单位输入框'])  # 获取所有大单位输入框
        if big:
            for k in range(kinds):
                sleep(0.5)
                _i = random.randint(0, len(big)-1)
                big[_i].click()
                self.send_keys(self.ELEMENT['输入商品数量'], random.randint(0, 3))
                self.click(self.ELEMENT['确认输入'])

                sleep(0.5)
                small[_i].click()
                self.send_keys(self.ELEMENT['输入商品数量'], random.randint(1, 3))
                self.click(self.ELEMENT['确认输入'])
        sleep(1)

    # @screenshot_error
    def empty_cart(self):
        """ 清空购物车 """

        logging.info('========== empty_cart ==========')

        if self.driver.title == '产品列表':
            self.click(self.ELEMENT['购物车'])

            # 通过循环删除购物车所有商品
            if self.driver.title == '购物车':
                del_icons = self.find_elements(self.ELEMENT['删除商品'])
                for icon in del_icons:
                    icon.click()
                    self.click(self.ELEMENT['删除确认'])
                    sleep(0.5)

                self.click(self.ELEMENT['添加商品'])

    # @screenshot_error
    def add_gift(self):
        """ 随机将购物车商品设为赠品 """

        logging.info('========== add_gift ==========')

        if self.driver.title == '产品列表':
            self.click(self.ELEMENT['购物车'])

            # 获取所有的赠品框，随机勾选
            if self.driver.title == '购物车':
                select_gift = self.find_elements(self.ELEMENT['勾选赠品'])
                random.choice(select_gift).click()

                self.click(self.ELEMENT['添加商品'])

    @screenshot_error
    def place_order(self, isgift=True):
        """首页下单"""

        logging.info('========== place_order ==========')
        if isgift:
            sleep(0.5)
            self.add_gift()

        self.click(self.ELEMENT['下单'])

        self.click(self.ELEMENT['选择客户'])

        self.swich_webview(self.context)  # 切换到APP视图做swipe操作

        width = self.get_window_size()['width']  # 获取屏幕宽度
        height = self.get_window_size()['height']  # 获取屏幕高度
        self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1)  # 上滑加载更多客户
        sleep(2)
        self.swich_webview(self.h5_context)  # 切换到H5视图继续后面的操作

        customers = self.find_elements(self.ELEMENT['客户'])  # 获取客户列表
        random.choice(customers).click()
        sleep(0.5)

        # assert self.element_is_dispalyed(self.ELEMENT['侧边客户列表'])

        while True:
            if self.element_is_dispalyed(self.ELEMENT['侧边客户列表']):
                logging.WARNING('********** 重新选择客户 **********')
                random.choice(customers).click()
            else:
                break

        self.click(self.ELEMENT['提交订单'])
        sleep(0.5)
        self.click(self.ELEMENT['下单二次确认'])
        sleep(0.5)
        self.click(self.ELEMENT['跳转订单列表'])

    @screenshot_error
    def enter_mashup_order(self):
        """进入聚合下单"""

        logging.info('========== enter_mashup_order ==========')

        self.click(self.ELEMENT['聚合下单'])
        sleep(1)

    @screenshot_error
    def mashup_order(self, isgift=True):
        """聚合下单"""

        logging.info('========== mashup_order ==========')
        if isgift:
            sleep(0.5)
            self.add_gift()

        self.find_element(self.ELEMENT['下单'])
        sleep(1)
        
        self.find_element(self.ELEMENT['提交订单'])
        sleep(1)

        self.find_element(self.ELEMENT['下单二次确认'])

        self.find_element(self.ELEMENT['拜访完成按钮'])
        sleep(1)

        self.find_element(self.ELEMENT['拜访完成二次确认'])
        sleep(1)


if __name__ == '__main__':
    driver = appium_desired()
    order = Order(driver)
    flag = [True, False]
    order.enter_ccloud()
    # for i in range(50):
    #     order.enter_normal_order()
    #     order.add_product(random.randint(1, 3))
    #     order.place_order(isgift=random.choice(flag))
    #     order.return_home_page()

    # order.go_func_group_page()
    # order.enter_mashup_order()
    # order.add_product(random.randint(1, 3))
    # order.mashup_order(isgift=random.choice(flag))
    # order.return_home_page()
    order.enter_normal_order()
    order.add_product(3)
    order.empty_cart()
