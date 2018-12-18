#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 9:03
# @Author  : Bilon
# @File    : customer.py
import random
import sys
from selenium.webdriver.support.wait import WebDriverWait
from Appium.setup import Setup
from common_tools import format_print, create_name, create_phone, create_gbk


class Customer(Setup):

    def add_customer(self, xpath='//*[@id="home"]/div[3]/div[2]/a[2]'):
        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(xpath))
            self.driver.find_element_by_xpath(xpath).click()    # 进入新增客户页面

            # 填写客户名、联系人、手机号
            types = ['小店', '副食', '酒楼', '批发', '烟酒', '便利店', '小卖部', '超市', '百货']
            customer_name = create_name() + types[random.randint(0,len(types)-1)]
            self.driver.find_element_by_id('customer_name').send_keys(customer_name)
            self.driver.find_element_by_id('contact').send_keys(create_name())
            self.driver.find_element_by_id('mobile').send_keys(create_phone())

            # 选择客户类型
            self.driver.find_element_by_id('default_customer_type').click()
            typelist = ['零售终端', '批发', '餐饮', '其他', '商超']
            types = self.driver.find_elements_by_xpath('/html/body/div[6]/div/div[2]/label')
            while True:
                t = int(random.randint(0, len(types)-1))
                if types[t].text in typelist:
                    # format_print(t, ' ', types[t].text)   # 取到的客户类型
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
            self.driver.swipe(width*0.25, height*0.9, width*0.25, height*0.1)   # 滑动
            self.driver.swipe(width*0.9, height*0.9, width*0.9, height*0.7)

            self.swich_webview(Setup.h5_context)  # 切换到H5视图继续后面的操作
            self.driver.find_element_by_xpath('//a[text()="完成"]').click()
            self.driver.find_element_by_id('address').send_keys(create_gbk(8))

            # 如果键盘弹出就关闭键盘
            # if self.driver.is_keyboard_shown():
            #     self.driver.hide_keyboard()

            self.driver.find_element_by_id('add').click()
            self.driver.find_element_by_xpath('//a[text()="确定"]').click()

        except Exception as e:
            format_print('新增客户失败 ', e)
            self.take_screenshot('新增客户失败')
            sys.exit(0)


if __name__ == '__main__':
    add_customer = Customer()
    for i in range(2):
        add_customer.add_customer()
        add_customer.go_home()
