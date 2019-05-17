#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:36
# @Author  : Bilon
# @File    : baseView.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    # 获取设备尺寸
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动屏幕
    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # 查找元素
    def find_element(self, locator):  # locator参数是定位方式，如("id", "kw"),把两个参数合并为一个,*号是把两个参数分开传值
        element = WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
        return element

    # 查找一组元素
    def find_elements(self, locator):  # locator参数是定位方式，如("id", "kw"),把两个参数合并为一个,*号是把两个参数分开传值
        elements = self.driver.find_elements(*locator)
        return elements

    # 判断元素文本
    def is_text_in_element(self, locator, text):
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False

    # 判断元素的value属性
    def is_value_element(self, locator, text):
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.text_to_be_present_in_element_value(locator, text))
            return True
        except:
            return False

    # 判断元素是否被定位到
    def is_exists(self, locator):
        try:
            WebDriverWait(self.driver, 20, 0.5).until(
                EC.presence_of_element_located(locator))  # 不需要*,这里跟*locator不是一个参数
            return True
        except:
            return False

    # 判断元素是否已经不存在,不存在了返回True,还存在就返回False
    def element_is_disappeared(self, locator, timeout=30):
        is_disappeared = WebDriverWait(self.driver, timeout, 1, (ElementNotVisibleException)).until_not(
            lambda x: x.find_element(*locator).is_displayed())
        return is_disappeared

    # 判断元素是否可见
    def element_is_dispalyed(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout, 1, (ElementNotVisibleException)).until(
            lambda x: x.find_element(*locator)).is_displayed()

    # 封装一个send_keys
    def send_keys(self, locator, text):
        self.find_element(locator).clear().send_keys(text)

    # 封装一个click
    def click(self, locator):
        self.find_element(locator).click()

    # 封装一个text
    def get_text(self, locator):
        return self.find_element(locator).text