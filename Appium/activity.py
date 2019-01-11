#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 10:00
# @Author  : Bilon
# @File    : activitycommon.py
import random
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from Appium.setup import Setup
from common_tools import format_print


class Activity(Setup):

    def take_activity(self, delay=1):
        try:
            # 进入"活动快捷执行"
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("activity_quick"))
            self.driver.find_element_by_id('activity_quick').click()
            # sleep(delay)

            # 选择活动
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("activity_title"))
            self.driver.find_element_by_id('activity_title').click()
            sleep(0.5)
            acts = self.driver.find_elements_by_tag_name('label')
            acts[random.randint(0, len(acts)-1)].click()
            sleep(delay)

            # 选择费用明细
            self.driver.find_element_by_id('expenses_ids').click()
            sleep(0.5)
            costs = self.driver.find_elements_by_tag_name('label')
            costs[random.randint(0, len(costs)-1)].click()
            self.driver.find_element_by_xpath('//a[text()="确定"]').click()
            sleep(delay)

            # 输入赠送数量
            self.driver.find_element_by_id('apply_num').send_keys(random.randint(1, 5))

            # 输入赠送金额
            if self.is_element_exist('apply_amount', 'id'):
                if self.driver.find_element_by_id('apply_amount').is_displayed():
                    amount_list = [0, 10, 200, 50, 100]
                    available_amount = self.driver.find_element_by_id('ableMoney').text[1:-1]  # 赠送金额剩余数字
                    while True:
                        amount = random.sample(amount_list, 1)[0]  # 从列表中随机选择一个元素
                        if amount <= int(available_amount):
                            self.driver.find_element_by_id('apply_amount').clear().send_keys(amount)
                            break

            # 随机拍1-5张照
            for i in range(random.randint(1, 5)):

                # self.driver.find_element_by_class_name('picture3BtnId').click()
                self.driver.find_element_by_xpath('//*[@id="form"]/div/section/div[5]/div/div/div/div/div').click()

                self.swich_webview(Setup.context)  # 切换到微信视图控制相机拍照
                self.driver.find_element_by_id('com.android.camera:id/shutter_button').click()  # Vivo x9 拍照
                self.driver.find_element_by_id('com.android.camera:id/done_button').click()  # Vivo x9 确定
                sleep(3)  # 等待图片上传完成

                self.driver.switch_to.context(Setup.h5_context)  # 切换到H5视图继续操作

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath('//button[contains(text(),"提交")]'))
            self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

            # 如果出现继续上传的提示，点击继续上传
            if self.is_element_exist('//a[contains(text(),"继续上传")]', 'xpath'):
                self.driver.find_element_by_xpath('//a[contains(text(),"继续上传")]').click()
                sleep(3)
                self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
            sleep(delay)

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath('/html/body/div[2]'))
            self.driver.find_element_by_xpath('/html/body/div[2]').click()
        except Exception as e:
            format_print('拍照出现异常 ', e)
            self.take_screenshot('拍照异常')


if __name__ == '__main__':
    act = Activity()
    for i in range(2):
        act.go_func_group_page()
        act.take_activity(delay=1)
        act.go_home()
