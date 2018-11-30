#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 16:07
# @Author  : Bilon
# @File    : ccloudinit.py
import os
import time
import unittest
from appium import webdriver
from Appium.mytools import my_print
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
from time import sleep
import sys


class Setup(object):
    """ 初始化 """
    my_url = 'http://localhost:4723/wd/hub'
    my_caps = {
        'appPackage': 'com.tencent.mm',
        'appActivity': '.ui.LauncherUI',
        'platformName': 'android',
        # 'platformVersion': '7.1.2',
        'deviceName': 'Vivo x9',
        'noReset': 'true',
        # 'recreateChromeDriverSessions': 'true',
        'unicodeKeyboard': 'true',
        'resetKeyboard': 'true',
        'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    }
    official_account_id = 'com.tencent.mm:id/azl'  # 消息列表联系人
    application_id = 'com.tencent.mm:id/po'  # 订单云平台入口ID
    context = 'NATIVE_APP'  # 默认的应用context
    h5_context = 'WEBVIEW_com.tencent.mm:tools'  # 应用H5视图

    def __init__(self, url=my_url, caps=None):
        """
        初始化driver对象
        :param url:
        :param caps:
        """
        if caps is None:
            caps = Setup.my_caps
            self.driver = webdriver.Remote(url, caps)   # 创建driver对象
        self.driver.implicitly_wait(20)     # 设置全局隐性等待20秒
        self.enter_wechat_official_account(Setup.official_account_id, '武汉珈研')  # 进入指定微信公众号
        self.enter_app(Setup.application_id)   # 进入应用
        self.swich_webview(Setup.h5_context)   # 切换到h5视图
        self.select_accout('华中科技')    # 选择账套

    def enter_wechat_official_account(self, account_id, account_name):
        """ 进入公众号 """
        try:
            elements = self.driver.find_elements_by_id(account_id)
            if elements:
                for e in elements:
                    if e.text == account_name:
                        e.click()
                        break
            else:
                my_print('消息列表没有该公众号')
        except Exception as e:
            my_print('进入公众号失败 ', e)
            self.take_screenShot('进入公众号失败')
            sys.exit(0)

    def enter_app(self, app_id):
        """ 进入订单云平台 """
        try:
            # self.driver.find_element_by_id(app_id).click()      # Meizu MX3
            self.driver.find_elements_by_id(app_id)[1].click()  # Vivo x9
        except Exception as e:
            my_print('进入订单云平台失败 ', e)
            self.take_screenShot('进入订单云平台失败')
            sys.exit(0)

    def swich_webview(self, webview):
        """ 切换视图(上下文) """
        try:
            if webview == Setup.context:
                self.driver.switch_to.context(webview)
            else:
                if webview not in self.driver.contexts:
                    # sleep(10)    # 如果获取到的上下文里没有所需上下文，休眠10秒
                    self.driver.find_element_by_id('com.tencent.mm:id/jc')

                self.driver.switch_to.context(webview)  # 切换上下文
                # my_print(self.driver.current_context)

                if self.driver.title == '搜一搜':
                    handles = self.driver.window_handles    # 获取当前窗口句柄
                    # my_print(handles)
                    self.driver.switch_to.window(handles[-1])

        except Exception as e:
            my_print('切换视图失败 ', e)
            self.take_screenShot('切换视图失败')
            sys.exit(0)

    def select_accout(self, name=None):
        title = self.driver.title  # 获取当前页面title
        if title == '选择用户':     # 如果页面title是选择用户，说明是进入了选择账套页面
            sets = self.driver.find_elements_by_tag_name('a')  # 获取所有账套
            if name:
                for s in sets:
                    if s.text == name:
                        s.click()
                        return
            sets[0].click()  # 没有指定账套时选择第一个账套进入

    # 返回首页
    def go_home(self):
        if self.is_element_exist('/html/body/div[1]/div/a[1]', 'xpath'):
            self.driver.find_element_by_xpath('/html/body/div[1]/div/a[1]').click()
        elif self.is_element_exist('button', 'id'):
            self.driver.find_element_by_id('button').click()
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/ul/li[1]/a').click()
        else:
            self.take_screenShot('返回首页失败')
            raise Exception('无法返回首页')

    # 判断元素是否存在，如果存在返回flag=True,否则返回False
    def is_element_exist(self, element, type=None):
        flag = True
        try:
            if type == 'id':
                self.driver.find_element_by_id(element)
            elif type == 'xpath':
                self.driver.find_element_by_xpath(element)
            elif type == 'class':
                self.driver.find_element_by_class_name(element)
            elif type == 'name':
                self.driver.find_element_by_name(element)
            else:
                self.driver.find_element_by_css_selector(element)
            return flag
        except:
            flag = False
            return flag

    def exit(self, eid='com.tencent.mm:id/jc'):
        """ 点击左上角X退出应用 """
        try:
            self.driver.switch_to.context(Setup.context)
            self.driver.find_element_by_id(eid).click()
        except Exception as e:
            my_print('退出应用失败 ', e)
            self.take_screenShot('退出应用失败')
            sys.exit(0)

    def take_screenShot(self, name="screenshot"):
        """
        获取当前屏幕的截图
        :param name: 截图名称
        Usage:
             device.take_screenShot('个人主页')   #实际截图保存的结果为：2018-11-28_15_24_58_个人主页.png
        """
        if self.driver.current_context != Setup.context:
            self.swich_webview(Setup.context)
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        shot_path = ".\\screenShots\\" + day
        # fq =os.getcwd()[:-4] +'screenShots\\'+day    根据获取的路径，然后截取路径保存到自己想存放的目录下
        shot_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        type = '.png'
        filename = shot_path + "\\" + shot_time + "_" + name + type
        if not os.path.exists(shot_path):
            os.makedirs(shot_path)
        self.driver.get_screenshot_as_file(filename)

if __name__ == '__main__':
    for i in range(5):
        ccloud_test = Setup()
    # ccloud_test.exit()
