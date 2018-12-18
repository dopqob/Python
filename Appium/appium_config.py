#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 18:57
# @Author  : Bilon
# @File    : appium_config.py
from appium import webdriver


class Singleton(object):
    driver = None

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            config = {
                'platformName': 'Android',
                'platformVersion': '4.4',
                'deviceName': '11111',
                'newCommandTimeout': 30,
                'automationName': 'Appium',
                'appPackage': 'com.ibroker.iBerHK',
                'appActivity': '.SplashActivity'
                # 'autoLaunch':'false'   #appium是否要自动启动或安装APP，默认为ture
                # 'newCommandTimeout':'60'  #设置未接受到新命令的超时时间，默认60s，如果60s内没有接收到新命令，appium会自动断开，
                # 如果我需要很长时间做driver之外的操作，可设置延长接收新命令的超时时间
                # 'unicodeKeyboard':True,
                # 'resetKeyboard':True
                # 'noReset':'false'  #在会话前是否重置APP状态，默认是false
            }
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', config)
        return cls._instance


class DriverClient(Singleton):

    def getDriver(self):
        return self.driver