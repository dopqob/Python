#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 10:08
# @Author  : Bilon
# @File    : common_func.py
import os
import random
import time
import logging
from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.baseView import BaseView
# from selenium.webdriver.common.by import By


def screenshot_error(func):
    """错误截图装饰器"""
    name = func.__name__

    def _screenshot_error(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            self.take_screenshot(name)  # 封装的截图方法
            logging.error(e)
            raise e

    return _screenshot_error


class Common(BaseView):
    """封装公共方法类"""

    def enter_ccloud(self):
        """执行用例的前提条件，先进入应用"""
        self.enter_wechat_official_account(self.official_account_id, '武汉珈研')  # 进入指定微信公众号
        self.enter_applet(self.application_id)     # 进入应用
        self.swich_webview(self.h5_context)     # 切换到h5视图
        self.select_accout('华中科技')          # 选择账套

    @screenshot_error
    def enter_wechat_official_account(self, account_id, account_name):
        """进入公众号"""

        logging.info('========== enter_wechat_official_account ==========')

        elements = self.driver.find_elements_by_id(account_id)
        if elements:
            for e in elements:
                if e.text == account_name:
                    e.click()
                    break
            else:
                logging.warning('消息列表没有该公众号')
                raise Exception('消息列表没有该公众号')

    def take_screenshot(self, img_name):
        """
        获取当前屏幕的截图
        :param img_name: 截图名称
        Usage:
             device.take_screenshot('个人主页')   #实际截图保存的结果为：2018-11-28_15_24_58_个人主页.png
        """
        logging.info('========== take_screenshot ==========')

        try:
            if self.driver.current_context != 'NATIVE_APP':
                self.driver.switch_to.context('NATIVE_APP')
            day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
            shot_path = "..\\Screenshots\\" + day
            shot_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
            img_type = '.png'
            filename = shot_path + "\\" + shot_time + "_" + img_name + img_type
            if not os.path.exists(shot_path):
                os.makedirs(shot_path)
            self.driver.get_screenshot_as_file(filename)
        except Exception as e:
            logging.warning('尝试截图失败', e)

    @screenshot_error
    def enter_applet(self, app_id):
        """进入订单云平台"""

        logging.info('========== enter_applet ==========')

        self.driver.find_element_by_id(app_id).click()     # Meizu MX3
        # self.driver.find_elements_by_id(app_id)[0].click()   # Vivo x9

    @screenshot_error
    def swich_webview(self, webview):
        """
        切换视图
        :param webview: 视图名称
        """
        if webview == self.context:
            self.driver.switch_to.context(webview)
        else:
            if webview not in self.driver.contexts:
                self.driver.find_element_by_id('com.tencent.mm:id/jc')

            self.driver.switch_to.context(webview)  # 切换上下文

            if self.driver.title == '搜一搜':
                handles = self.driver.window_handles    # 获取当前窗口句柄
                self.driver.switch_to.window(handles[-1])

    @screenshot_error
    def select_accout(self, name=None):
        """
        如果出现选账套页面，进入name账套，如果没指定name，默认选第一个
        :param name: 账套名称
        """
        title = self.driver.title  # 获取当前页面title
        if title == '选择用户':     # 如果页面title是选择用户，说明是进入了选择账套页面
            sets = self.driver.find_elements_by_tag_name('a')  # 获取所有账套
            if name:
                for s in sets:
                    if s.text == name:
                        s.click()
                        return
            sets[0].click()

    @screenshot_error
    def return_home_page(self):
        """返回首页"""

        logging.info('========== return_home_page ==========')

        time.sleep(1)
        if self.is_element_exist('.wy-foot-menu>a:first-child'):
            self.driver.find_element_by_css_selector('.wy-foot-menu a:first-child').click()
        elif self.is_element_exist('button', 'id'):
            self.driver.find_element_by_id('button').click()
            self.driver.find_elements_by_tag_name('li')[0].click()

    @screenshot_error
    def go_mycenter(self):
        """进入个人中心"""

        logging.info('========== go_mycenter ==========')

        css = '.wy-foot-menu>a:last-child'
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_css_selector(css))
        self.driver.find_element_by_css_selector(css).click()

    @screenshot_error
    def go_func_group_page(self):
        """
        进入(聚合)客户列表并随机选择一个客户
        """
        logging.info('========== go_func_group_page ==========')

        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("customerVisits"))
        self.driver.find_element_by_id("customerVisits").click()  # 从首页的客户拜访进入客户列表
        time.sleep(2)

        customers = self.driver.find_elements_by_xpath('//*[@id="customerList"]/div')  # 获取当前页客户
        if customers:
            customers[random.randint(0, len(customers)-1)].click()  # 随机选一个用户
        else:
            logging.warning('没有客户，请先添加客户')

        self.driver.switch_to.frame('layui-layer-iframe1')  # 切换到iframe弹层

        # 定位失败时刷新定位
        location = self.driver.find_element_by_id('location-span')
        if location.text == '请手动刷新定位':
            self.driver.find_element_by_id('refresh').click()  # 刷新定位
            time.sleep(3)

        # 如果出现定位失败弹窗，点击确定，并刷新定位
        # if self.is_element_exist('weui-dialog', 'class'):  # 判断元素节点是否存在
        #     self.driver.find_element_by_class_name('primary').click()
        #     self.driver.find_element_by_id('refresh').click()  # 刷新定位
        #     time.sleep(3)

    def is_element_exist(self, element, eimg_type=None):
        """
        判断元素是否存在
        :param element: 元素id class xpath css
        :param eimg_type: 对应的类型，如果没有默认为css
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

    def take_photo(self):
        """拜访、活动拍照"""

        logging.info('========== take_photo ==========')

        for i in range(random.randint(1, 5)):
        # for i in range(5):
            self.driver.find_element_by_class_name('picture1BtnId').click()

            self.swich_webview(self.context)  # 切换到微信视图控制相机拍照
            # self.driver.find_element_by_id('com.android.gallery3d:id/shutter_button').click() # Meizu MX3
            # self.driver.find_element_by_id('com.android.gallery3d:id/image_capture_done_img').click() # Meizu MX3
            self.driver.find_element_by_id('com.android.camera:id/shutter_button').click()  # Vivo x9 拍照
            self.driver.find_element_by_id('com.android.camera:id/done_button').click()  # Vivo x9 确定
            time.sleep(3)  # 等待图片上传完成

            self.driver.switch_to.context(self.h5_context)  # 切换到H5视图继续操作

    @screenshot_error
    def exit(self, close_id):
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.find_element_by_id(close_id).click()


if __name__ == '__main__':
    driver = appium_desired()
    common = Common(driver)
    common.enter_ccloud()
