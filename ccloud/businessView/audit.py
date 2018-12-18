#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 19:00
# @Author  : Bilon
# @File    : audit.py
import random
from time import sleep
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error
from common_tools import create_gbk


class Audit(Common):

    # 审核通过
    def audit_pass(self):
        p = '//div[contains(text(),"同意")]'
        if self.is_element_exist(p, 'xpath'):
            self.driver.find_element_by_xpath(p).click()
            self.driver.find_element_by_xpath('//span[text()="通过"]').click()
            sleep(2)

    # 返回首页
    def return_index(self):
        self.driver.find_element_by_class_name('return_index').click()

    @screenshot_error
    def order_audit(self, flag=True):
        """
        订单审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        self.driver.find_element_by_xpath('//p[text()="订单审核"]').click()

        if flag:
            self.audit_pass()
        else:
            r = '//div[contains(text(),"拒绝")]'
            if self.is_element_exist(r, 'xpath'):
                self.driver.find_element_by_xpath(r).click()
                resons = self.driver.find_elements_by_name('refuseReson')
                resons[random.randint(0, len(resons) - 1)].click()
                self.driver.find_element_by_xpath('//span[text()="确认"]').click()
                sleep(2)

        self.return_index()

    @screenshot_error
    def customer_audit(self, flag=True):
        """
        客户审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        self.driver.find_element_by_xpath('//p[text()="客户审核"]').click()

        if flag:
            self.audit_pass()
        else:
            r = '//div[contains(text(),"拒绝")]'
            if self.is_element_exist(r, 'xpath'):
                self.driver.find_element_by_xpath(r).click()
                self.driver.find_element_by_id('comment').send_keys(create_gbk(10))
                self.driver.find_element_by_xpath('//span[text()="确认"]').click()
                sleep(2)

        self.return_index()

    def visit_audit(self, flag=True):
        """
        客户拜访审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        self.driver.find_element_by_xpath('//p[text()="拜访审核"]').click()

        if flag:
            self.audit_pass()
        else:
            r = '//div[contains(text(),"拒绝")]'
            if self.is_element_exist(r, 'xpath'):
                self.driver.find_element_by_xpath(r).click()

                sel = self.driver.find_element_by_xpath('//*[@id="refuse-reason"]/select')
                Select(sel).select_by_value(str(random.randint(1, 3)))

                self.driver.find_element_by_id('comment').send_keys(create_gbk(10))
                self.driver.find_element_by_xpath('//span[text()="确认"]').click()
                sleep(2)

        self.return_index()


if __name__ == '__main__':
    driver = appium_desired()
    audit = Audit(driver)
    audit.enter_ccloud()
    # audit.order_audit()
    audit.visit_audit(flag=False)
