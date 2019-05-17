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

    # 微信
    official_account_id = 'com.tencent.mm:id/b4o'  # 消息列表联系人ID 微信7.0版本及以后
    # official_account_id = 'com.tencent.mm:id/azl'  # 消息列表联系人ID 微信7.0版本及以前
    application_id = 'com.tencent.mm:id/am1'  # 订单云平台入口ID 微信7.0版本及以后
    # application_id = 'com.tencent.mm:id/po'   # 订单云平台入口ID 微信7.0版本及以前
    context = 'NATIVE_APP'  # 默认的应用context
    h5_context = 'WEBVIEW_com.tencent.mm:tools'  # 应用H5视图
    close = 'com.tencent.mm:id/k5'  # 左上角X

    # 企业微信
    menu_id = 'com.tencent.wework:id/aqa'  # 底部菜单ID
    app_id = 'com.tencent.wework:id/avx'    # 应用ID

    def enter_ccloud(self, flag=True):
        """执行用例的前提条件，先进入应用"""
        if flag:
            self.enter_wechat_official_account('武汉珈研')  # 进入指定微信公众号
            self.enter_applet()     # 进入应用

        else:
            self.enter_qywx_applet('慧订货')   # 进入企业微信的慧订货应用

        time.sleep(1)

    @screenshot_error
    def enter_wechat_official_account(self, account_name):
        """进入公众号"""

        logging.info('========== enter_wechat_official_account ==========')

        elements = self.driver.find_elements_by_id(self.official_account_id)
        if elements:
            for e in elements:
                if e.text == account_name:
                    e.click()
                    time.sleep(0.5)
                    break
            else:
                logging.warning('消息列表没有该公众号')
                raise Exception('消息列表没有该公众号')

    @screenshot_error
    def enter_applet(self):
        """进入订单云平台"""

        logging.info('========== enter_applet ==========')

        self.driver.find_element_by_id(self.application_id).click()     # Meizu MX3
        # self.driver.find_elements_by_id(app_id)[0].click()   # Vivo x9
        self.swich_webview(self.h5_context)  # 切换到h5视图
        # self.select_accout('华中科技')  # 选择账套
        time.sleep(3)

    @screenshot_error
    def enter_qywx_applet(self, app_name):
        """企业微信进入应用"""
        logging.info('========== enter_qywx_applet ==========')
        menus = self.driver.find_elements_by_id(self.menu_id)
        if menus:
            for m in menus:
                if m.text == '工作台':
                    m.click()
                    break
            apps = self.driver.find_elements_by_id(self.app_id)
            for app in apps:
                if app.text == app_name:
                    app.click()
                    break
        self.swich_webview(self.h5_context)  # 切换到h5视图
        time.sleep(1)

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

        time.sleep(2)
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
        time.sleep(1)

    @screenshot_error
    def go_func_group_page(self):
        """
        进入(聚合)客户列表并随机选择一个客户
        """
        logging.info('========== go_func_group_page ==========')

        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("customerVisits"))
        self.driver.find_element_by_id("customerVisits").click()  # 从首页的客户拜访进入客户列表
        time.sleep(1)

        customers = self.driver.find_elements_by_xpath('//*[@id="customerList"]/div')  # 获取当前页客户
        if customers:
            # customers[random.randint(0, len(customers)-1)].click()  # 随机选一个用户
            random.choice(customers).click()  # 随机选一个用户
            time.sleep(3)
        else:
            logging.warning('没有客户，请先添加客户')

        self.driver.switch_to.frame('layui-layer-iframe1')  # 切换到iframe弹层

        if self.is_element_exist('//a[text()="确定"]', 'xpath'):  # 如果出现上个拜访未完成的提示，点击确定
            self.driver.find_element_by_xpath('//a[text()="确定"]').click()

        # 定位失败时刷新定位
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("location-span"))
        location = self.driver.find_element_by_id('location-span')
        if location.text == '请手动刷新定位':
            self.driver.find_element_by_id('refresh').click()  # 刷新定位
            time.sleep(2)

        time.sleep(1)
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

    def clear_drafts(self):
        """清空草稿箱"""
        badge = self.driver.find_element_by_xpath('//*[@id="home"]/div[4]/div[2]/a[5]/span')
        if badge.is_displayed() and int(badge.text) == 4:
            # if self.is_element_exist('//*[@id="home"]/div[4]/div[2]/a[5]/span', 'xpath'):
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath('//p[text()="拜访草稿箱"]'))
            self.driver.find_element_by_xpath('//p[text()="拜访草稿箱"]').click()
            self.driver.find_element_by_tag_name('img').click()
            self.driver.find_element_by_xpath('//a[text()="确定"]').click()
            self.driver.find_element_by_xpath('//button[text()="首页"]').click()

    def take_photo(self,flag=True):
        """拜访、活动拍照"""

        logging.info('========== take_photo ==========')

        for i in range(random.randint(1, 5)):
        # for i in range(5):
            self.driver.find_element_by_class_name('picture1BtnId').click()
            time.sleep(1)

            self.swich_webview(self.context)  # 切换到微信视图控制相机拍照
            # self.driver.find_element_by_id('com.android.gallery3d:id/shutter_button').click() # Meizu MX3
            # self.driver.find_element_by_id('com.android.gallery3d:id/image_capture_done_img').click() # Meizu MX3
            self.driver.find_element_by_id('com.android.camera:id/shutter_button').click()  # Vivo x9 拍照
            time.sleep(1)
            self.driver.find_element_by_id('com.android.camera:id/done_button').click()  # Vivo x9 确定
            if not flag:    # 企业微信上传图片二次确认按钮
                self.driver.find_element_by_id('com.tencent.wework:id/e2v').click()
            time.sleep(3)  # 等待图片上传完成

            self.driver.switch_to.context(self.h5_context)  # 切换到H5视图继续操作

    def upload_photo(self, flag=True):
        """补录上传照片"""
        logging.info('========== upload_photo ==========')

        for i in range(random.randint(1, 4)):
            # for i in range(4):
            self.driver.find_element_by_class_name('picture1BtnId').click()
            time.sleep(0.5)
            self.swich_webview(self.context)  # 切换到NATIVE_APP视图控制照片选择

            # 企业微信多两个步骤
            if not flag:
                sources = self.driver.find_elements_by_id('com.tencent.wework:id/aqa')
                sources[1].click()
                self.driver.find_element_by_xpath(
                    '//android.widget.ImageButton[@content-desc="显示根目录"]').click()

            self.driver.find_elements_by_id('vivo:id/text1')[-1].click()
            time.sleep(1)
            # width = self.driver.get_window_size().get('width')  # 获取屏幕宽度
            # height = self.driver.get_window_size().get('height')  # 获取屏幕高度
            # self.driver.tap([(width * 0.9, height * 0.4), ])
            photos = self.driver.find_elements_by_id('com.android.documentsui:id/thumbnail')
            # photos[random.randint(0, len(photos)-1)].click()
            random.choice(photos).click()
            time.sleep(3)  # 等待图片上传完成

            self.driver.switch_to.context(self.h5_context)  # 切换到H5视图继续操作
            time.sleep(0.5)
            if self.is_element_exist('//h3[text()="照片没有定位信息"]', 'xpath'):
                self.driver.find_element_by_xpath('//span[text()="关闭"]').click()
            if self.is_element_exist('//h3[text()="照片定位不一致"]', 'xpath'):
                self.driver.find_element_by_xpath('//span[text()="关闭"]').click()

            # self.driver.find_elements_by_id('android:id/title')[-1].click()     # 选择系统相册
            # num = self.driver.find_elements_by_id('com.vivo.gallery:id/dreamway_folder_count')[0].text  # 获取照片数量
            # self.driver.find_elements_by_id(
            #     'com.vivo.gallery:id/dreamway_folder_info')[0].click()  # 选择相机相册

            # time.sleep(0.5)
            # if int(num) == i+1:
            #     self.driver.tap([(width * 0.2 * (i+1), height * 0.2), ])
            #     time.sleep(3)  # 等待图片上传完成
            #
            #     self.driver.switch_to.context(self.h5_context)  # 切换到H5视图继续操作
            #     time.sleep(0.5)
            #     if self.is_element_exist('//h3[text()="照片没有定位信息"]', 'xpath'):
            #         self.driver.find_element_by_xpath('//span[text()="关闭"]').click()
            #     if self.is_element_exist('//h3[text()="照片定位不一致"]', 'xpath'):
            #         self.driver.find_element_by_xpath('//span[text()="关闭"]').click()
            #     break
            # else:
            #     self.driver.tap([(width * 0.2 * (i + 1), height * 0.2), ])
            #     time.sleep(3)  # 等待图片上传完成
            #
            #     self.driver.switch_to.context(self.h5_context)  # 切换到H5视图继续操作
            #     time.sleep(0.5)
            #     if self.is_element_exist('//h3[text()="照片没有定位信息"]', 'xpath'):
            #         self.driver.find_element_by_xpath('//span[text()="关闭"]').click()
            #     if self.is_element_exist('//h3[text()="照片定位不一致"]', 'xpath'):
            #         self.driver.find_element_by_xpath('//span[text()="关闭"]').click()

    @screenshot_error
    def exit(self):
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.find_element_by_id(self.close).click()

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


if __name__ == '__main__':
    driver = appium_desired(flag=False)
    common = Common(driver)
    common.enter_ccloud(flag=False)
    time.sleep(5)
