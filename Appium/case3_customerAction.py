#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 17:42
# @Author  : Bilon
# @File    : case3_customerAction.py
import random
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from Appium.setup import Setup
from Appium.mytools import my_print
from selenium.webdriver.common.alert import Alert


class CustomerAction(Setup):

    # 进入客户列表并随机选择一个客户
    def syn_page(self):
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("customerVisits"))
        self.driver.find_element_by_id("customerVisits").click()
        sleep(5)

        customers = self.driver.find_elements_by_xpath('//*[@id="customerList"]/div')   # 获取当前页客户
        if customers:
            customers[random.randint(0, len(customers)-1)].click()  # 随机选一个用户
            sleep(5)
        else:
            my_print('没有客户，请先添加客户')

    # 常规拜访
    def customer_visit(self):
        try:
            # 处理弹窗，未成功
            # al = self.driver.switch_to_alert()
            # my_print(type(al))
            # my_print(al.text)
            # al.accept()

            self.driver.switch_to.frame('layui-layer-iframe1')  # 切换到弹窗

            if self.is_element_exist('/html/body/div[6]/div[3]/a[2]', 'xpath'):
                self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/a[2]').click()
                sleep(1)

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("photo"))
            self.driver.find_element_by_id('photo').click()
            sleep(1)

            # 随机拍1-5张照片
            for i in range(random.randint(1, 5)):
                shot_xpath = '//*[@id="form"]/section[2]/div[3]/div/div/div/div/div'

                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(shot_xpath))
                self.driver.find_element_by_xpath(shot_xpath).click()

                self.swich_webview(Setup.context)   # 切换到微信视图控制相机拍照

                # self.driver.find_element_by_id('com.android.gallery3d:id/shutter_button').click() # Meizu MX3
                # self.driver.find_element_by_id('com.android.gallery3d:id/image_capture_done_img').click() # Meizu MX3
                self.driver.find_element_by_id('com.android.camera:id/shutter_button').click()   # Vivo x9
                sleep(1)
                self.driver.find_element_by_id('com.android.camera:id/done_button').click()      # Vivo x9
                sleep(5)

                self.driver.switch_to.context(Setup.h5_context)

            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//button[contains(text(),"提交")]'))
            self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()

            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("visitEnd"))
            self.driver.find_element_by_id('visitEnd').click()  # 点击拜访完成按钮
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        except Exception as e:
            my_print('拍照出现异常 ', e)
            self.take_screenShot('拍照异常')


if __name__ == '__main__':
    action = CustomerAction()
    for i in range(50):
        action.syn_page()
        action.customer_visit()
        action.driver.switch_to.default_content()   # 切换到主页面
        action.go_home()
