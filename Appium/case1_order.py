#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 19:32
# @Author  : Bilon
# @File    : case1_order.py
import random
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Appium.setup import Setup
from Appium.mytools import my_print


class Order(Setup):

    def empty_cart(self):
        """ 清空购物车 """
        if self.driver.title == '产品列表':
            self.driver.find_element_by_id('shoppingCart').click()

            # 通过循环删除购物车所有商品
            if self.driver.title == '购物车':
                # while True:
                #     del_icons = self.driver.find_elements_by_class_name('icon-trash-o')
                #     if del_icons:
                #         del_icons[0].click()
                #         self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/a[2]').click()
                #     else:
                #         break
                del_icons = self.driver.find_elements_by_class_name('icon-trash-o')
                for i in del_icons:
                    i.click()
                    self.driver.find_element_by_xpath('//a[text()="确定"]').click()

                self.driver.find_element_by_id('addGoods').click()  # 返回商品列表

    def add_gift(self):
        """ 随机将购物车商品设为赠品 """
        if self.driver.title == '产品列表':
            self.driver.find_element_by_id('shoppingCart').click()

            # 获取所有的赠品框，随机勾选
            if self.driver.title == '购物车':
                gift_icons = self.driver.find_elements_by_name('isGift')
                gift_icons[random.randint(0, len(gift_icons)-1)].click()

                self.driver.find_element_by_id('addGoods').click()  # 返回商品列表

    def add_order(self, xpath='//*[@id="home"]/div[3]/div[2]/a[1]'):
        try:
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(xpath))
            self.driver.find_element_by_xpath(xpath).click()

            self.empty_cart()

            # 选择商品
            big_inputs = self.driver.find_elements_by_id('bigNum')  # 获取所有大单位输入框
            small_inputs = self.driver.find_elements_by_id('smallNum')  # 获取所有小单位输入框
            if big_inputs:
                # 随机选一个商品输入1-5
                big_num = random.randint(1, len(big_inputs)-1)
                big_inputs[big_num].click()
                WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div[5]/input'))
                self.driver.find_element_by_xpath('/html/body/div[5]/input').clear().send_keys(random.randint(1, 5))
                self.driver.find_element_by_id('confirm-input').click()

                small_num = random.randint(1, len(small_inputs)-1)
                small_inputs[small_num].click()
                WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div[5]/input'))
                self.driver.find_element_by_xpath('/html/body/div[5]/input').clear().send_keys(random.randint(1, 5))
                self.driver.find_element_by_id('confirm-input').click()

            self.add_gift()

            self.driver.find_element_by_id('placeOrder').click()    # 下单

            # 选客户 通过CSS获取客户列表，两种方法都可以
            self.driver.find_element_by_xpath('//*[@id="form"]/div[1]/div[1]').click()
            # customers = self.driver.find_elements(By.CSS_SELECTOR, '#customerList div')
            customers = self.driver.find_elements_by_css_selector('#customerList div')
            customers[random.randint(0, len(customers)-1)].click()

            self.driver.find_element_by_id('placeOrder').click()    # 提交订单

            self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/a[2]').click()

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath('/html/body/div[4]/div[2]/a[1]'))
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[1]').click()
        except Exception as e:
            my_print('下单失败 ', e)
            self.take_screenShot('下单失败')
            sys.exit(0)

if __name__ == '__main__':
    order = Order()
    for i in range(2):
        order.add_order()
        order.go_home()
