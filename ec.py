#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 15:30
# @Author  : Bilon
# @File    : ec.py

#封装元素方法
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
import time


class Base():
    def __init__(self, driver):
        self.driver=driver

#查找元素
    def find_element(self, locator): #locator参数是定位方式，如("id", "kw"),把两个参数合并为一个,*号是把两个参数分开传值
        element=WebDriverWait(self.driver, 20, 0.5).until(lambda x:x.find_element(*locator))
        self.driver.find_element()
        print(element)
        return element
#判断元素文本
    def is_text_in_element(self, locator,text):
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False
#判断元素的value属性
    def is_value_element(self, locator, text):
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.text_to_be_present_in_element_value(locator, text))
            return True
        except:
            return False

#判断元素是否被定位到
    def is_exists(self, locator):
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))#不需要*,这里跟*locator不是一个参数
            return True
        except:
            return False
#判断元素是否已经不存在,不存在了返回True,还存在就返回False
    def element_is_disappeared(self, locator, timeout=30):
        is_disappeared=WebDriverWait(self.driver, timeout, 1, (ElementNotVisibleException)).until_not(lambda x:x.find_element(*locator).is_displayed())
        print('is_disappeared')

#封装一个send_keys
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

#封装一个click
    def click(self,locator):
        self.find_element(locator).click()

#封装一个text
    def get_text(self, locator):
        return self.find_element(locator).text

#运行主函数
if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com")
    #实例化
    base=Base(driver)
    #定位输入框
    input_loc=("id","kw")
    #通过实例调用find_element来发送
    base.send_keys(input_loc,"selenium")
    #点击按钮
    button=("css selector","#su")
    base.click(button)
    print(base.is_text_in_element(("link text", "地图"), "地图"))
    time.sleep(3)
    driver.quit()
