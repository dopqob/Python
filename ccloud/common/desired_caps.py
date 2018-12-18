#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:32
# @Author  : Bilon
# @File    : desired_caps.py
from appium import webdriver


def appium_desired():
    url = 'http://localhost:4723/wd/hub'
    caps = {
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
    driver = webdriver.Remote(url, caps)
    driver.implicitly_wait(20)
    return driver


if __name__ == '__main__':
    appium_desired()