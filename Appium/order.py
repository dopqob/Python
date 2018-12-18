#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 19:32
# @Author  : Bilon
# @File    : order.py
import random
import sys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from Appium.setup import Setup
from common_tools import format_print


class Order(Setup):

    def empty_cart(self):
        """ 清空购物车 """
        if self.driver.title == '产品列表':
            self.driver.find_element_by_id('shoppingCart').click()

            # 通过循环删除购物车所有商品
            if self.driver.title == '购物车':
                del_icons = self.driver.find_elements_by_class_name('icon-trash-o')
                for i in del_icons:
                    i.click()
                    self.driver.find_element_by_xpath('//a[text()="确定"]').click()
                    sleep(0.5)

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

    def test_order(self, xpath='//*[@id="home"]/div[3]/div[2]/a[1]', gift=True):
        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(xpath))
            self.driver.find_element_by_xpath(xpath).click()

            # 查看合计数量，如果数量不为0，先进购物车清空商品
            content = self.driver.find_element_by_id('totalNum').text
            if content[1] != '0':
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
                sleep(1)

                small_num = random.randint(1, len(small_inputs)-1)
                small_inputs[small_num].click()
                WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div[5]/input'))
                self.driver.find_element_by_xpath('/html/body/div[5]/input').clear().send_keys(random.randint(1, 5))
                self.driver.find_element_by_id('confirm-input').click()

            if gift:
                self.add_gift()

            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('placeOrder'))
            self.driver.find_element_by_id('placeOrder').click()    # 下单

            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="form"]/div[1]/div[1]'))
            self.driver.find_element_by_xpath('//*[@id="form"]/div[1]/div[1]').click()

            self.swich_webview(Setup.context)  # 切换到APP视图做swipe操作
            width = self.driver.get_window_size().get('width')  # 获取屏幕宽度
            height = self.driver.get_window_size().get('height')  # 获取屏幕高度
            self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1) # 上滑加载更多客户
            self.swich_webview(Setup.h5_context)  # 切换到H5视图继续后面的操作
            sleep(1)

            customers = self.driver.find_elements_by_id('customerInfo')  # 获取客户列表
            index = random.randint(0, len(customers)-2) # 这个地方理论上应该-1，但取取到最大值时会报错，-2时不会
            customers[index].click()

            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('placeOrder'))
            self.driver.find_element_by_id('placeOrder').click()    # 提交订单

            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div[4]/div[3]/a[2]'))
            self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/a[2]').click()

            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div[4]/div[2]/a[1]'))
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[1]').click()

            return len(customers), index

        except Exception as e:
            format_print('下单失败 ', e)
            self.take_screenshot('下单失败')
            sys.exit(0)

if __name__ == '__main__':
    order = Order()
    for i in range(2):
        # order.test_order(gift=False)
        format_print(i + 1, ' ', order.test_order(gift=False))
        order.go_home()
