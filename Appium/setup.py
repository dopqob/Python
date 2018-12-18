#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 16:07
# @Author  : Bilon
# @File    : ccloudinit.py
import os
import random
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from common_tools import format_print
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
import sys


class Setup(object):
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
        'newCommandTimeout': '1000',
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

    # 给异常加上装饰器，输出错误信息并截图
    # def wrap_error(func):
    #     def wrapper(*args):
    #         try:
    #             f = func(*args)
    #             return f
    #         except:
    #             take_screenShot()
    #             tearDown()
    #     return wrapper

    # 进入公众号
    def enter_wechat_official_account(self, account_id, account_name):
        try:
            elements = self.driver.find_elements_by_id(account_id)
            if elements:
                for e in elements:
                    if e.text == account_name:
                        e.click()
                        break
            else:
                format_print('消息列表没有该公众号')
        except Exception as e:
            format_print('进入公众号失败 ', e)
            self.take_screenshot('进入公众号失败')
            sys.exit(0)

    # 进入订单云平台
    def enter_app(self, app_id):
        try:
            # self.driver.find_element_by_id(app_id).click()      # Meizu MX3
            self.driver.find_elements_by_id(app_id)[1].click()  # Vivo x9
        except Exception as e:
            format_print('进入订单云平台失败 ', e)
            self.take_screenshot('进入订单云平台失败')
            sys.exit(0)

    # 切换视图（上下文）
    def swich_webview(self, webview):
        try:
            if webview == Setup.context:
                self.driver.switch_to.context(webview)
            else:
                if webview not in self.driver.contexts:
                    self.driver.find_element_by_id('com.tencent.mm:id/jc')

                self.driver.switch_to.context(webview)  # 切换上下文
                # format_print(self.driver.current_context)

                if self.driver.title == '搜一搜':
                    handles = self.driver.window_handles    # 获取当前窗口句柄
                    # format_print(handles)
                    self.driver.switch_to.window(handles[-1])

        except Exception as e:
            format_print('切换视图失败 ', e)
            self.take_screenshot('切换视图失败')
            sys.exit(0)

    # 选择账套
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
        time.sleep(1)
        if self.is_element_exist('.wy-foot-menu>a:first-child'):
            self.driver.find_element_by_css_selector('.wy-foot-menu a:first-child').click()
        elif self.is_element_exist('button', 'id'):
            self.driver.find_element_by_id('button').click()
            self.driver.find_elements_by_tag_name('li')[0].click()
        else:
            self.take_screenshot('返回首页失败')
            # raise Exception('无法返回首页')

    # 进入个人中心
    def go_mycenter(self):
        if self.is_element_exist('.wy-foot-menu>a:last-child'):
            self.driver.find_element_by_css_selector('.wy-foot-menu>a:last-child').click()
        else:
            self.take_screenshot('进入个人中心失败')
            format_print('进入个人中心失败')

    # 进入聚合客户列表并随机选择一个客户
    def go_func_group_page(self, delay=3):
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("customerVisits"))
        self.driver.find_element_by_id("customerVisits").click()  # 从首页的客户拜访进入客户列表
        time.sleep(1)

        customers = self.driver.find_elements_by_xpath('//*[@id="customerList"]/div')  # 获取当前页客户
        if customers:
            customers[random.randint(0, len(customers)-1)].click()  # 随机选一个用户
            # time.sleep(3)
        else:
            format_print('没有客户，请先添加客户')

        self.driver.switch_to.frame('layui-layer-iframe1')  # 切换到iframe弹层

        if self.is_element_exist('/html/body/div[6]/div[3]/a[2]', 'xpath'):  # 判断元素节点是否存在
            self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/a[2]').click()  # 如果出现定位失败弹窗，点击确定
            self.driver.find_element_by_id('refresh').click()  # 刷新定位
            time.sleep(delay)

    def is_element_exist(self, element, eimg_type=None):
        """
        判断元素是否存在
        :param element: 元素id名称,class名称,xpath路径,css等
        :param eimg_type: 对应的类型id,class,xpath,css等，如果没有默认为css
        :return: True表示元素存在，False表示不存在
        """
        flag = True
        try:
            if eimg_type == 'id':
                self.driver.find_element_by_id(element)
            elif eimg_type == 'xpath':
                self.driver.find_element_by_xpath(element)
            elif eimg_type == 'class':
                self.driver.find_element_by_class_name(element)
            elif eimg_type == 'name':
                self.driver.find_element_by_name(element)
            else:
                self.driver.find_element_by_css_selector(element)
            return flag
        except Exception:
            flag = False
            return flag

    # 退出应用
    def exit(self, eid='com.tencent.mm:id/jc'):
        try:
            self.driver.switch_to.context(Setup.context)
            self.driver.find_element_by_id(eid).click()
        except Exception as e:
            format_print('退出应用失败 ', e)
            self.take_screenshot('退出应用失败')
            sys.exit(0)

    def take_screenshot(self, img_name="screenshot"):
        """
        获取当前屏幕的截图
        :param img_name: 截图名称
        Usage:
             device.take_screenshot('个人主页')   #实际截图保存的结果为：2018-11-28_15_24_58_个人主页.png
        """
        if self.driver.current_context != Setup.context:
            self.swich_webview(Setup.context)
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        shot_path = ".\\screenShots\\" + day
        shot_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        img_type = '.png'
        filename = shot_path + "\\" + shot_time + "_" + img_name + img_type
        if not os.path.exists(shot_path):
            os.makedirs(shot_path)
        self.driver.get_screenshot_as_file(filename)


if __name__ == '__main__':

    ccloud_test = Setup()
