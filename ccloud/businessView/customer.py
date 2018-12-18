#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 15:05
# @Author  : Bilon
# @File    : customer.py
import random
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error
from common_tools import create_gbk, create_name, create_phone, format_print


class Customer(Common):

    @screenshot_error
    def add_customer(self):
        """新增客户"""
        add_customer_xpath = '//*[@id="home"]/div[3]/div[2]/a[2]'
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(add_customer_xpath))
        self.driver.find_element_by_xpath(add_customer_xpath).click()  # 进入新增客户页面

        # 填写客户名、联系人、手机号
        kinds = ['小店', '副食', '酒楼', '批发', '烟酒', '便利店', '小卖部', '超市', '百货']
        customer_name = create_name() + random.choice(kinds)
        self.driver.find_element_by_id('customer_name').send_keys(customer_name)
        self.driver.find_element_by_id('contact').send_keys(create_name())
        self.driver.find_element_by_id('mobile').send_keys(create_phone())

        # 选择客户类型
        self.driver.find_element_by_id('default_customer_type').click()
        typelist = ['零售终端', '批发', '餐饮', '其他', '商超']
        types = self.driver.find_elements_by_xpath('/html/body/div[6]/div/div[2]/label')
        while True:
            t = int(random.randint(0, len(types) - 1))
            if types[t].text in typelist:
                types[t].click()
                break

        # 选择客户等级
        self.driver.find_element_by_id('subType').click()
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/label[1]').click()

        # 选择配送地址
        self.driver.find_element_by_id('delivery-address').click()
        self.swich_webview(self.context)  # 切换到APP视图做swipe操作，滑动选择省市区
        width = self.driver.get_window_size().get('width')  # 获取屏幕宽度
        height = self.driver.get_window_size().get('height')  # 获取屏幕高度
        self.driver.swipe(width * 0.25, height * 0.9, width * 0.25, height * 0.1)  # 滑动
        self.driver.swipe(width * 0.9, height * 0.9, width * 0.9, height * 0.7)

        self.swich_webview(self.h5_context)  # 切换到H5视图继续后面的操作
        self.driver.find_element_by_xpath('//a[text()="完成"]').click()
        self.driver.find_element_by_id('address').send_keys(create_gbk(8))

        # 如果键盘弹出就关闭键盘
        # if self.driver.is_keyboard_shown():
        #     self.driver.hide_keyboard()

        self.driver.find_element_by_id('add').click()
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()

    @screenshot_error
    def customer_visit(self):
        """常规拜访"""
        # 进入"常规拜访"
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("photo"))
        self.driver.find_element_by_id('photo').click()
        sleep(1)

        # 随机拍1-5张照片
        self.take_photo()

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('//button[contains(text(),"提交")]'))
        self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("visitEnd"))
        self.driver.find_element_by_id('visitEnd').click()  # 点击拜访完成按钮
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()


if __name__ == '__main__':
    driver = appium_desired()
    customer = Customer(driver)
    # customer.add_customer()
    customer.go_func_group_page()
    customer.customer_visit()
