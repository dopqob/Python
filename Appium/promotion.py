#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 16:39
# @Author  : Bilon
# @File    : promotion.py
import random
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from Appium.setup import Setup
from common_tools import format_print, create_name, create_phone, create_gbk


class Promotion(Setup):

    def enter_promotion(self):
        try:
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath('//p[text()="营销推广"]'))
            self.driver.find_element_by_xpath('//p[text()="营销推广"]').click()
        except Exception as e:
            format_print('进入营销推广失败', e)
            self.take_screenshot('进入营销推广失败')

    # 消费培育活动
    def take_consume(self):
        try:
            # 进入消费培育活动
            act_kinds = self.driver.find_elements_by_tag_name('input')
            act_kinds[0].click()
            sleep(3)

            # 选择活动
            self.driver.find_element_by_id('activity_title').click()
            acts = self.driver.find_elements_by_tag_name('label')
            acts[random.randint(0, len(acts)-1)].click()
            sleep(1)

            # 选择费用明细
            self.driver.find_element_by_id('expenses_ids').click()
            expenses = self.driver.find_elements_by_tag_name('label')
            expenses[random.randint(0, len(expenses)-1)].click()
            self.driver.find_element_by_xpath('//a[text()="确定"]').click()
            sleep(1)

            # 培育对象名称
            self.driver.find_element_by_id('customerNames').send_keys(create_name())

            # 培育对象电话
            self.driver.find_element_by_id('customerMobile').send_keys(create_phone())

            # 培育地点
            self.driver.find_element_by_id('customerAddress').send_keys(create_gbk(6))

            # 品鉴人数
            self.driver.find_element_by_id('people').send_keys(random.randint(1, 3))

            # 赠送数量
            self.driver.find_element_by_id('apply_num').clear().send_keys(random.randint(1, 3))

            # 赠送金额
            if self.is_element_exist('apply_amount', 'id'):
                if self.driver.find_element_by_id('apply_amount').is_displayed():
                    amount_list = [0, 100, 200, 500, 1000]
                    available_amount = self.driver.find_element_by_id('ableMoney').text[1:-1]  # 赠送金额剩余数字
                    while True:
                        amount = random.sample(amount_list, 1)[0]  # 从列表中随机选择一个元素
                        if amount <= int(available_amount):
                            self.driver.find_element_by_id('apply_amount').clear().send_keys(amount)
                            break

            # 随机拍1-5张照
            for i in range(random.randint(1, 5)):
                self.driver.find_element_by_class_name('picture1BtnId').click()
                # self.driver.find_element_by_xpath('//*[@id="form"]/div/section/div[2]/div/div/div/div/div').click()

                self.swich_webview(Setup.context)  # 切换到微信视图控制相机拍照
                self.driver.find_element_by_id('com.android.camera:id/shutter_button').click()  # Vivo x9 拍照
                self.driver.find_element_by_id('com.android.camera:id/done_button').click()  # Vivo x9 确定
                sleep(600)  # 等待图片上传完成

                self.driver.switch_to.context(Setup.h5_context)  # 切换到H5视图继续操作

            WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element_by_xpath('//button[contains(text(),"提交")]'))
            self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

            WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
            sleep(1)

        except Exception as e:
            format_print('拍照出现异常 ', e)
            self.take_screenshot('拍照异常')

    # 团购直销活动
    def take_group_purchase(self):
        try:
            # 进入团购直销活动
            act_kinds = self.driver.find_elements_by_tag_name('input')
            act_kinds[1].click()
            sleep(3)

            # 选择活动
            self.driver.find_element_by_id('activity_title').click()
            acts = self.driver.find_elements_by_tag_name('label')
            acts[random.randint(0, len(acts)-1)].click()
            sleep(1)

            # 选择费用明细
            self.driver.find_element_by_id('expenses_ids').click()
            expenses = self.driver.find_elements_by_tag_name('label')
            expenses[random.randint(0, len(expenses)-1)].click()
            self.driver.find_element_by_xpath('//a[text()="确定"]').click()
            sleep(1)

            # 团购单位名称
            self.driver.find_element_by_id('companyName').send_keys(create_gbk(5))

            # 单位负责人
            self.driver.find_element_by_id('customerNames').send_keys(create_name())

            # 联系电话
            self.driver.find_element_by_id('customerMobile').send_keys(create_phone())

            # 赠送数量
            self.driver.find_element_by_id('apply_num').clear().send_keys(random.randint(1, 3))

            # 赠送金额
            if self.is_element_exist('apply_amount', 'id'):
                if self.driver.find_element_by_id('apply_amount').is_displayed():
                    amount_list = [0, 10, 20, 50, 100]
                    available_amount = self.driver.find_element_by_id('ableMoney').text[1:-1]  # 赠送金额剩余数字
                    while True:
                        amount = random.sample(amount_list, 1)[0]  # 从列表中随机选择一个元素
                        if amount <= int(available_amount):
                            self.driver.find_element_by_id('apply_amount').clear().send_keys(amount)
                            break

            # 随机拍1-5张照
            for i in range(random.randint(1, 5)):
                self.driver.find_element_by_class_name('picture1BtnId').click()
                # self.driver.find_element_by_xpath('//*[@id="form"]/div/section/div[2]/div/div/div/div/div').click()

                self.swich_webview(Setup.context)  # 切换到微信视图控制相机拍照
                self.driver.find_element_by_id('com.android.camera:id/shutter_button').click()  # Vivo x9 拍照
                self.driver.find_element_by_id('com.android.camera:id/done_button').click()  # Vivo x9 确定
                sleep(600)  # 等待图片上传完成

                self.driver.switch_to.context(Setup.h5_context)  # 切换到H5视图继续操作

            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_xpath('//button[contains(text(),"提交")]'))
            self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

            WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
            sleep(1)

        except Exception as e:
            format_print('拍照出现异常 ', e)
            self.take_screenshot('拍照异常')

    # 宴席推广活动
    def take_banquet(self):
        try:
            # 进入宴席推广活动
            act_kinds = self.driver.find_elements_by_tag_name('input')
            act_kinds[2].click()
            # sleep(5)

            # 选择宴席类型
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('banquet_type'))
            self.driver.find_element_by_id('banquet_type').click()
            banquets = self.driver.find_elements_by_tag_name('label')
            banquets[random.randint(0, len(banquets)-1)].click()
            # sleep(1)

            # 选择活动
            self.driver.find_element_by_id('activity_title').click()
            acts = self.driver.find_elements_by_tag_name('label')
            acts[random.randint(0, len(acts)-1)].click()
            sleep(1)

            # 选择费用明细
            self.driver.find_element_by_id('expenses_ids').click()
            expenses = self.driver.find_elements_by_tag_name('label')
            expenses[random.randint(0, len(expenses)-1)].click()
            self.driver.find_element_by_xpath('//a[text()="确定"]').click()
            sleep(1)

            # 联系人
            self.driver.find_element_by_id('customerNames').send_keys(create_name())

            # 电话
            self.driver.find_element_by_id('customerMobile').send_keys(create_phone())

            # 地址
            self.driver.find_element_by_id('customerAddress').send_keys(create_gbk(6))

            # 桌数
            self.driver.find_element_by_id('people').send_keys(random.randint(1, 3))

            # 赠送数量
            self.driver.find_element_by_id('apply_num').clear().send_keys(random.randint(1, 3))

            # 赠送金额
            if self.is_element_exist('apply_amount', 'id'):
                if self.driver.find_element_by_id('apply_amount').is_displayed():
                    amount_list = [0, 10, 20, 50, 100]
                    available_amount = self.driver.find_element_by_id('ableMoney').text[1:-1]  # 赠送金额剩余数字
                    while True:
                        amount = random.sample(amount_list, 1)[0]  # 从列表中随机选择一个元素
                        if amount <= int(available_amount):
                            self.driver.find_element_by_id('apply_amount').clear().send_keys(amount)
                            break

            # 随机拍1-5张照
            for i in range(random.randint(1, 5)):
                self.driver.find_element_by_class_name('picture1BtnId').click()
                # self.driver.find_element_by_xpath('//*[@id="form"]/div/section/div[2]/div/div/div/div/div').click()

                self.swich_webview(Setup.context)  # 切换到微信视图控制相机拍照
                self.driver.find_element_by_id('com.android.camera:id/shutter_button').click()  # Vivo x9 拍照
                self.driver.find_element_by_id('com.android.camera:id/done_button').click()  # Vivo x9 确定
                sleep(600)  # 等待图片上传完成

                self.driver.switch_to.context(Setup.h5_context)  # 切换到H5视图继续操作

            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_xpath('//button[contains(text(),"提交")]'))
            self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

            WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
            sleep(1)

        except Exception as e:
            format_print('拍照出现异常 ', e)
            self.take_screenshot('拍照异常')


if __name__ == '__main__':
    promotion = Promotion()
    for i in range(50):
        promotion.go_mycenter()
        promotion.enter_promotion()
        promotion.take_consume()
        promotion.take_group_purchase()
        promotion.take_banquet()
        promotion.go_home()
