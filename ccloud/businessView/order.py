#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 11:37
# @Author  : Bilon
# @File    : order.py
import random
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error


class Order(Common):

    @screenshot_error
    def add_product(self, kinds):
        """
        添加商品到购物车
        :param kinds: 商品种类
        """
        order_xpath = '//*[@id="home"]/div[3]/div[2]/a[1]'
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(order_xpath))
        self.driver.find_element_by_xpath(order_xpath).click()

        # 查看合计数量，如果数量不为0，先进购物车清空商品
        content = self.driver.find_element_by_id('totalNum').text
        if content[1] != '0':
            self.empty_cart()

        # 选择商品
        big = self.driver.find_elements_by_id('bigNum')  # 获取所有大单位输入框
        small = self.driver.find_elements_by_id('smallNum')  # 获取所有小单位输入框
        if big:
            for k in range(kinds):
                sleep(0.5)
                index = random.randint(1, len(big) - 1)
                big[index].click()
                WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div[5]/input'))
                self.driver.find_element_by_xpath('/html/body/div[5]/input').clear().send_keys(random.randint(1, 5))
                self.driver.find_element_by_id('confirm-input').click()

                sleep(0.5)
                small[index].click()
                WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div[5]/input'))
                self.driver.find_element_by_xpath('/html/body/div[5]/input').clear().send_keys(random.randint(1, 5))
                self.driver.find_element_by_id('confirm-input').click()

    # @screenshot_error
    def empty_cart(self):
        """ 清空购物车 """
        if self.driver.title == '产品列表':
            self.driver.find_element_by_id('shoppingCart').click()

            # 通过循环删除购物车所有商品
            if self.driver.title == '购物车':
                del_icons = self.driver.find_elements_by_class_name('icon-trash-o')
                for good in del_icons:
                    good.click()
                    self.driver.find_element_by_xpath('//a[text()="确定"]').click()
                    sleep(0.5)

                self.driver.find_element_by_id('addGoods').click()  # 返回商品列表

    # @screenshot_error
    def add_gift(self):
        """ 随机将购物车商品设为赠品 """
        if self.driver.title == '产品列表':
            self.driver.find_element_by_id('shoppingCart').click()

            # 获取所有的赠品框，随机勾选
            if self.driver.title == '购物车':
                gift_icons = self.driver.find_elements_by_name('isGift')
                gift_icons[random.randint(0, len(gift_icons) - 1)].click()

                self.driver.find_element_by_id('addGoods').click()  # 返回商品列表

    @screenshot_error
    def place_order(self, isgift=True):

        if isgift:
            sleep(0.5)
            self.add_gift()

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('placeOrder'))
        self.driver.find_element_by_id('placeOrder').click()  # 下单

        # 选客户 通过CSS获取客户列表，两种方法都可以
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="form"]/div[1]/div[1]'))
        self.driver.find_element_by_xpath('//*[@id="form"]/div[1]/div[1]').click()

        self.swich_webview(self.context)  # 切换到APP视图做swipe操作
        width = self.driver.get_window_size().get('width')  # 获取屏幕宽度
        height = self.driver.get_window_size().get('height')  # 获取屏幕高度
        self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1)  # 上滑加载更多客户
        sleep(1)
        self.swich_webview(self.h5_context)  # 切换到H5视图继续后面的操作

        customers = self.driver.find_elements_by_id('customerInfo')  # 获取客户列表
        index = random.randint(0, len(customers) - 2)  # 这个地方理论上应该-1，但取-1时会报错，-2时不会
        customers[index].click()

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('placeOrder'))
        self.driver.find_element_by_id('placeOrder').click()  # 提交订单

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('/html/body/div[4]/div[3]/a[2]'))
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/a[2]').click()  # 确定

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('/html/body/div[4]/div[2]/a[1]'))
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[1]').click()


if __name__ == '__main__':
    driver = appium_desired()
    order = Order(driver)
    flag = [True, False]
    order.enter_ccloud()
    for i in range(20):
        order.add_product(random.randint(1, 3))
        order.place_order(isgift=random.choice(flag))
        order.go_home()
    # order.add_product(3)
    # order.empty_cart()
