#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:36
# @Author  : Bilon
# @File    : baseView.py


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver
        self.official_account_id = 'com.tencent.mm:id/b4o'    # 消息列表联系人ID 微信7.0版本及以后
        # self.official_account_id = 'com.tencent.mm:id/azl'  # 消息列表联系人ID 微信7.0版本及以前
        self.application_id = 'com.tencent.mm:id/am1'  # 订单云平台入口ID 微信7.0版本及以后
        # self.application_id = 'com.tencent.mm:id/po'   # 订单云平台入口ID 微信7.0版本及以前
        self.context = 'NATIVE_APP'     # 默认的应用context
        self.h5_context = 'WEBVIEW_com.tencent.mm:tools'    # 应用H5视图
        self.close = 'com.tencent.mm:id/k5'     # 左上角X

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
