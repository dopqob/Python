#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 19:00
# @Author  : Bilon
# @File    : audit.py
import random
import logging
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error
from common_tools import create_gbk, format_print


class Audit(Common):
    # 审核入口xpath
    order_audit_entrance = '//p[text()="订单审核"]'
    customer_audit_entrance = '//p[text()="客户审核"]'
    visit_audit_entrance = '//p[text()="拜访审核"]'
    activity_audit_entrance = '//p[text()="活动审核"]'

    # 同意/拒绝按钮xpath
    agree_button = '//div[contains(text(),"同意")]'
    refuse_button = '//div[contains(text(),"拒绝")]'

    # 二次确认/通过/取消按钮xpath
    confirm_button = '//span[text()="确认"]'
    pass_button = '//span[text()="通过"]'
    cancel_button = '//span[text()="取消"]'

    # 订单拒绝多选框name
    order_refuse = 'refuseReson'

    # 拜访审核拒绝下拉框xpath
    visit_refuse = '//*[@id="refuse-reason"]/select'

    # 备注信息id
    comment = 'comment'

    # 返回首页按钮class name
    return_home_page = 'return_index'

    # 审核通过
    def audit_pass(self):

        logging.info('========== audit_pass ==========')

        self.driver.find_element_by_xpath(self.agree_button).click()
        self.driver.find_element_by_xpath(self.pass_button).click()

    # 返回首页
    def return_index(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.return_home_page).click()

    @screenshot_error
    def order_audit(self, flag=True):
        """
        订单审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(self.order_audit_entrance))
        self.driver.find_element_by_xpath(self.order_audit_entrance).click()

        if not self.is_element_exist(self.refuse_button, 'xpath'):
            logging.warning('审核列表为空！')
        else:
            if flag:
                self.audit_pass()
            else:
                logging.info('========== audit_refuse ==========')

                self.driver.find_element_by_xpath(self.refuse_button).click()
                resons = self.driver.find_elements_by_name(self.order_refuse)
                resons[random.randint(0, len(resons) - 1)].click()
                self.driver.find_element_by_xpath(self.confirm_button).click()
        self.return_index()

    @screenshot_error
    def customer_audit(self, flag=True):
        """
        客户审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(self.customer_audit_entrance))
        self.driver.find_element_by_xpath(self.customer_audit_entrance).click()

        if not self.is_element_exist(self.refuse_button, 'xpath'):
            logging.warning('审核列表为空！')
        else:
            if flag:
                self.audit_pass()
            else:
                logging.info('========== audit_refuse ==========')

                self.driver.find_element_by_xpath(self.refuse_button).click()
                self.driver.find_element_by_id(self.comment).send_keys(create_gbk(10))
                self.driver.find_element_by_xpath(self.confirm_button).click()
        self.return_index()

    @screenshot_error
    def visit_audit(self, flag=True):
        """
        客户拜访审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        self.driver.find_element_by_xpath(self.visit_audit_entrance).click()

        if not self.is_element_exist(self.refuse_button, 'xpath'):
            logging.warning('审核列表为空！')
        else:
            if flag:
                self.audit_pass()
            else:
                logging.info('========== audit_refuse ==========')

                self.driver.find_element_by_xpath(self.refuse_button).click()

                sel = self.driver.find_element_by_xpath(self.visit_refuse)
                Select(sel).select_by_value(str(random.randint(1, 3)))

                self.driver.find_element_by_id(self.comment).send_keys(create_gbk(10))
                self.driver.find_element_by_xpath(self.confirm_button).click()
        self.return_index()

    @screenshot_error
    def activity_audit(self, flag=True):
        """
        活动审核
        :param flag: True代表审核通过，False代表审核拒绝
        """
        self.driver.find_element_by_xpath(self.activity_audit_entrance).click()

        if not self.is_element_exist(self.refuse_button, 'xpath'):
            logging.warning('审核列表为空！')
        else:
            if flag:
                self.audit_pass()
            else:
                logging.info('========== audit_refuse ==========')

                self.driver.find_element_by_xpath(self.refuse_button).click()
                self.driver.find_element_by_id(self.comment).send_keys(create_gbk(10))
                self.driver.find_element_by_xpath(self.confirm_button).click()
        self.return_index()


if __name__ == '__main__':
    driver = appium_desired()
    audit = Audit(driver)
    audit.enter_ccloud()
    audit.order_audit()
    audit.order_audit(flag=False)

    # audit.visit_audit()
    # audit.visit_audit(flag=False)
