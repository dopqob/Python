#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 9:03
# @Author  : Bilon
# @File    : case2_addCustomer.py
import random
import sys
from selenium.webdriver.support.wait import WebDriverWait
from Appium.setup import Setup
from Appium.mytools import my_print, creat_gbk, creat_phone


class AddCustomer(Setup):

    def add_customer(self, xpath='//*[@id="home"]/div[3]/div[2]/a[2]'):
        try:
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(xpath))
            self.driver.find_element_by_xpath(xpath).click()    # 进入新增客户页面

            # 填写客户名、联系人、手机号
            self.driver.find_element_by_id('customer_name').send_keys(creat_gbk(4))
            self.driver.find_element_by_id('contact').send_keys(creat_gbk(2))
            self.driver.find_element_by_id('mobile').send_keys(creat_phone())

            # 选择客户类型
            self.driver.find_element_by_id('default_customer_type').click()
            typelist = ['零售终端', '批发', '餐饮', '其他', '商超']
            types = self.driver.find_elements_by_xpath('/html/body/div[6]/div/div[2]/label')
            while True:
                t = int(random.randint(0, len(types)-1))
                if types[t].text in typelist:
                    # my_print(t, ' ', types[t].text)   # 取到的客户类型
                    types[t].click()
                    break

            # 选择客户等级
            self.driver.find_element_by_id('subType').click()
            self.driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/label[1]').click()

            # 选择配送地址
            self.driver.find_element_by_id('delivery-address').click()
            self.swich_webview(Setup.context)    # 切换到APP视图做swipe操作，滑动选择省市区
            width = self.driver.get_window_size().get('width')  # 获取屏幕宽度
            height = self.driver.get_window_size().get('height')    # 获取屏幕高度
            self.driver.swipe(width*0.25, height*0.9, width*0.25, height*0.2)   # 滑动
            self.driver.swipe(width*0.9, height*0.9, width*0.9, height*0.75)

            self.swich_webview(Setup.h5_context)  # 切换到H5视图继续后面的操作
            self.driver.find_element_by_xpath('//a[text()="完成"]').click()
            self.driver.find_element_by_id('address').send_keys(creat_gbk(8))

            # 如果键盘弹出就关闭键盘
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()

            self.driver.find_element_by_id('add').click()
            self.driver.find_element_by_xpath('//a[text()="确定"]').click()

        except Exception as e:
            my_print('新增客户失败 ', e)
            self.take_screenShot('新增客户失败')
            sys.exit(0)


if __name__ == '__main__':
    add_customer = AddCustomer()
    for i in range(50):
        add_customer.add_customer()
        add_customer.go_home()
