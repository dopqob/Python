#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 17:42
# @Author  : Bilon
# @File    : customer_visit.py
import random
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from Appium.setup import Setup
from common_tools import format_print


class CustomerVisit(Setup):

    # 常规拜访
    def customer_visit(self):
        try:
            # 进入"常规拜访"
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("photo"))
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
                self.driver.find_element_by_id('com.android.camera:id/shutter_button').click()   # Vivo x9 拍照
                self.driver.find_element_by_id('com.android.camera:id/done_button').click()      # Vivo x9 确定
                sleep(3)    # 等待图片上传完成

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
            format_print('拍照出现异常 ', e)
            self.take_screenshot('拍照异常')


if __name__ == '__main__':
    action = CustomerVisit()
    for i in range(2):
        action.go_func_group_page()
        action.customer_visit()
        action.driver.switch_to.default_content()   # 切换到主页面
        action.go_home()
