#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 16:07
# @Author  : Bilon
# @File    : ccloudinit.py
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import sys

URL = 'http://localhost:4723/wd/hub'
CAPS = {
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'platformName': 'android',
    'deviceName': 'aaa',
    'noReset': 'true',
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
}


def wrap_print(func):
    """ 装饰打印，给上下加上*分隔符 """
    def wrapper(*args):
        print('*' * 100)
        func(*args)
        print('*' * 100 + '\n')
    return wrapper


@wrap_print
def my_print(*args):
    log = ''
    for arg in args:
        log += str(arg)
    print(log)


class CcloudInit(object):
    """ 初始化 启动微信 """
    def __init__(self, *args):
        """
        如果有参数，就传入参数，没有参数时用默认参数
        :param args: 参数必须大于等于2个，第一个是url，第二个是caps
        """
        try:
            if len(args) >= 2:
                self.driver = webdriver.Remote(args[0], args[1])

            self.driver = webdriver.Remote(URL, CAPS)
            self.driver.implicitly_wait(20)     # 设置全局隐性等待20秒
        except Exception as e:
            my_print(e)
            sys.exit(0)

    def enter_wechat_official_account(self, account_id, account_name):
        """ 进入公众号 """
        try:
            elements = self.driver.find_elements_by_id(account_id)
            for e in elements:
                if e.text == account_name:
                    e.click()
                    break
        except Exception as e:
            my_print('进入公众号失败 ', e)
            sys.exit(0)     # 用例终止

    def swich_webview(self, webview):
        """ 切换视图 """
        sleep(5)
        try:
            if webview not in self.driver.contexts:
                sleep(5)    # 如果获取到的上下文里没有所需上下文，休眠5秒

            self.driver.switch_to.context(webview)  # 切换上下文
        except Exception as e:
            my_print('获取上下文失败 ', e)
            sys.exit(0)

    def enter_app(self, app_id, webview, *args):
        """
        进入订单云平台并选择账套
        :param app_id: 应用入口id
        :param webview: H5视图
        :param args: 账套名（可选）
        :return:
        """
        self.driver.find_element_by_id(app_id).click()  # 进入订单云平台
        self.swich_webview(webview)     # 切换到H5视图

        try:    # 如果出现多账套选择页面，选第一个账套
            title = self.driver.title  # 获取当前页面title
            my_print('当前页面的title： ', title)
            if title == '选择用户':
                # WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_tag_name('a'))
                sets = self.driver.find_elements_by_tag_name('a')   # 获取所有账套
                if args:    # 如果指定了账套，就进指定账套
                    for set in sets:
                        if set.text == args[0]:
                            set.click()
                            return  # 找到指定账套后进入后马上return
                sets[0].click()     # 没有指定账套时选择第一个账套进入
        except Exception as e:
            my_print(e)

    def exit(self, eid):
        """ 点击左上角X退出应用 """
        try:
            self.driver.switch_to.context('NATIVE_APP')
            self.driver.find_element_by_id(eid).click()
        except Exception as e:
            my_print('关闭应用失败 ', e)
            sys.exit(0)


# def ccloudinit(*args):
#     my_init = CcloudInit(my_caps, wechat_location)
#     my_init.enter_wechat_official_account(official_account_id, '武汉珈研')
#     my_init.enter_app(application_id)
#     my_init.swich_webview(h5_webview)
#     my_init.select_set()



if __name__ == '__main__':

    official_account_id = 'com.tencent.mm:id/azl'  # 消息列表联系人
    application_id = 'com.tencent.mm:id/po'  # 订单云平台入口ID
    h5_webview = 'WEBVIEW_com.tencent.mm:tools' # 应用H5视图
    exit_id = 'com.tencent.mm:id/jc'    # 应用左上角的X

    ccloud_test = CcloudInit()
    ccloud_test.enter_wechat_official_account(official_account_id, '武汉珈研')
    ccloud_test.enter_app(application_id, h5_webview)
    # ccloud_test.swich_webview(h5_webview)
    # ccloud_test.select_set()
    ccloud_test.exit(exit_id)
