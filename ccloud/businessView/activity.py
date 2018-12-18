#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 9:51
# @Author  : Bilon
# @File    : activity.py
import random
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error
from common_tools import create_phone, create_name, create_gbk


class Activity(Common):
    """活动基类，封装一些公共方法"""

    def choose_act(self):
        """选择活动"""
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("activity_title"))
        self.driver.find_element_by_id('activity_title').click()
        sleep(0.5)
        acts = self.driver.find_elements_by_tag_name('label')
        acts[random.randint(0, len(acts) - 1)].click()
        sleep(1)

    def choose_expense(self):
        """选择费用明细"""
        self.driver.find_element_by_id('expenses_ids').click()
        sleep(0.5)
        costs = self.driver.find_elements_by_tag_name('label')
        costs[random.randint(0, len(costs) - 1)].click()
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()
        sleep(1)

    def apply_num(self):
        """赠送数量"""
        if self.driver.find_element_by_id('apply_num').is_displayed():  # is_displayed 如果元素可见
            available_num = self.driver.find_element_by_id('ableNum').text[1:-1]  # 可用赠送数量
            if int(available_num) <= 0:
                self.driver.find_element_by_id('apply_num').clear().send_keys(0)
            else:
                self.driver.find_element_by_id('apply_num').clear().send_keys(random.randint(1, 5))
            sleep(0.5)

    def apply_amount(self):
        """赠送金额"""
        if self.driver.find_element_by_id('apply_amount').is_displayed():
            amount_list = [0, 10, 200, 50, 100]
            available_amount = self.driver.find_element_by_id('ableMoney').text[1:-1]  # 可用赠送金额
            while True:
                amount = random.choice(amount_list)  # 从列表中随机选择一个元素
                if amount <= int(available_amount):
                    self.driver.find_element_by_id('apply_amount').clear().send_keys(amount)
                    break

    def choose_campaign(self, num):
        """选择营销推广活动类型"""
        act_kinds = self.driver.find_elements_by_tag_name('input')
        act_kinds[num].click()
        sleep(3)


class NormalActivity(Activity):
    """普通活动"""
    @screenshot_error
    def normal_activity(self, delay=1):
        """
        活动快捷执行
        :param delay: 等待时间（秒）
        """
        # 进入应用
        # self.enter_ccloud()

        # 进入功能聚合页面
        # self.go_func_group_page()

        # 进入"活动快捷执行"
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("activity_quick"))
        self.driver.find_element_by_id('activity_quick').click()

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 输入赠送数量
        self.apply_num()

        # 输入赠送金额
        # if self.is_element_exist('apply_amount', 'id'):
        self.apply_amount()

        # 随机拍1-5张照
        self.take_photo()

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


class MarketingCampaign(Activity):
    """营销推广活动"""

    @screenshot_error
    def enter_marketing(self):
        """进入营销推广"""
        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_xpath('//p[text()="营销推广"]'))
        self.driver.find_element_by_xpath('//p[text()="营销推广"]').click()

    @screenshot_error
    def cultivate_activity(self):
        """消费培育活动"""

        # 选择消费培育活动
        self.choose_campaign(0)

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 培育对象名称
        self.driver.find_element_by_id('customerNames').send_keys(create_name())

        # 培育对象电话
        self.driver.find_element_by_id('customerMobile').send_keys(create_phone())

        # 培育地点
        self.driver.find_element_by_id('customerAddress').send_keys(create_gbk(6))

        # 品鉴人数
        self.driver.find_element_by_id('people').send_keys(random.randint(1, 3))

        # 赠送数量
        self.apply_num()

        # 赠送金额
        self.apply_amount()

        # 随机拍1-5张照
        self.take_photo()

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('//button[contains(text(),"提交")]'))
        self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        sleep(1)

    @screenshot_error
    def groupon_activity(self):
        """团购直销活动"""

        # 进入团购直销活动
        self.choose_campaign(1)

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 团购单位名称
        self.driver.find_element_by_id('companyName').send_keys(create_gbk(5))

        # 单位负责人
        self.driver.find_element_by_id('customerNames').send_keys(create_name())

        # 联系电话
        self.driver.find_element_by_id('customerMobile').send_keys(create_phone())

        # 赠送数量
        self.apply_num()

        # 赠送金额
        self.apply_amount()

        # 随机拍1-5张照
        self.take_photo()

        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_xpath('//button[contains(text(),"提交")]'))
        self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        sleep(1)

    @screenshot_error
    def feast_activity(self):
        """宴席推广活动"""

        # 进入宴席推广活动
        self.choose_campaign(2)

        # 选择宴席类型
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('banquet_type'))
        self.driver.find_element_by_id('banquet_type').click()
        banquets = self.driver.find_elements_by_tag_name('label')
        banquets[random.randint(0, len(banquets) - 1)].click()
        # sleep(1)

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 联系人
        self.driver.find_element_by_id('customerNames').send_keys(create_name())

        # 电话
        self.driver.find_element_by_id('customerMobile').send_keys(create_phone())

        # 地址
        self.driver.find_element_by_id('customerAddress').send_keys(create_gbk(6))

        # 桌数
        self.driver.find_element_by_id('people').send_keys(random.randint(1, 3))

        # 赠送数量
        self.apply_num()

        # 赠送金额
        self.apply_amount()

        # 随机拍1-5张照
        self.take_photo()

        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_xpath('//button[contains(text(),"提交")]'))
        self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        sleep(1)


if __name__ == '__main__':
    driver = appium_desired()
    act = NormalActivity(driver)
    act.enter_ccloud()
    act.go_func_group_page()
    act.normal_activity()
    # market = MarketingCampaign(driver)
    # market.cultivate_activity()
    # market.groupon_activity()
    # market.feast_activity()
