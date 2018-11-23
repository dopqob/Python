#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 19:32
# @Author  : Bilon
# @File    : case1_order.py
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from Appium.ccloudinit import my_print, CcloudInit


class Order(CcloudInit):
    def __init__(self, *args):
        CcloudInit.__init__(self, *args)

    def add_order(self, xpath='//*[@id="home"]/div[3]/div[2]/a[1]'):
        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(xpath))
            self.driver.find_element_by_xpath(xpath).click()

            big_inputs = self.driver.find_elements_by_id('bigNum')
            small_inputs = self.driver.find_elements_by_id('smallNum')
            if big_inputs:
                for big_input in big_inputs:
                    self.driver.execute_script('getElementsById("bigNum").value = "5"')
                    sleep(1)
                    # self.driver.find_element_by_xpath('/html/body/div[5]/input').send_keys(5)
                    # self.driver.find_element_by_xpath('confirm-input').click()
            self.driver.find_element_by_id('placeOrder').click()
        except Exception as e:
            my_print(e)


if __name__ == '__main__':
    official_account_id = 'com.tencent.mm:id/azl'  # 消息列表联系人
    application_id = 'com.tencent.mm:id/po'  # 订单云平台入口ID
    h5_webview = 'WEBVIEW_com.tencent.mm:tools' # 应用H5视图
    exit_id = 'com.tencent.mm:id/jc'    # 应用左上角的X

    order = Order()
    order.enter_wechat_official_account(official_account_id, '武汉珈研')
    order.enter_app(application_id, h5_webview)
    order.add_order()

