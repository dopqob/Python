#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:32
# @Author  : Bilon
# @File    : desired_caps.py
import yaml
import logging.config
from appium import webdriver


CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired(flag=True):
    """设置一个flag，为True时启动微信，否则启动企业微信"""

    with open('../config/caps.yaml', 'r', encoding='utf-8') as f:
        data = yaml.load(f)

    desired_caps = {}
    if flag:
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']
        desired_caps['chromeOptions'] = data['chromeOptions']
    else:
        desired_caps['appPackage'] = data['appPackage_qywx']
        desired_caps['appActivity'] = data['appActivity_qywx']
        desired_caps['chromeOptions'] = data['chromeOptions_qywx']

    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']


    logging.info('start run test...')

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(20)
    return driver

    # url = 'http://localhost:4723/wd/hub'
    # caps = {
    #     'appPackage': 'com.tencent.mm',
    #     'appActivity': '.ui.LauncherUI',
    #     'platformName': 'android',
    #     # 'platformVersion': '7.1.2',
    #     'deviceName': 'Vivo x9',
    #     'noReset': 'true',
    #     # 'recreateChromeDriverSessions': 'true',
    #     'unicodeKeyboard': 'true',
    #     'resetKeyboard': 'true',
    #     'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    #     }
    # driver = webdriver.Remote(url, caps)
    # driver.implicitly_wait(20)
    # return driver


if __name__ == '__main__':
    appium_desired()
