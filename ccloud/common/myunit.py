#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 11:32
# @Author  : Bilon
# @File    : myunit.py
import os
import time
import unittest
from time import sleep
from ccloud.common.desired_caps import appium_desired


class StartEnd(unittest.TestCase):

    def setUp(self):
        self.driver = appium_desired()

    def tearDown(self):
        sleep(1)
        self.driver.quit()

    @classmethod
    def create_report_file(cls):
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        path = "..\\Report\\" + day
        create_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        file = path + "\\" + create_time + "_" + 'Report.html'
        if not os.path.exists(path):
            os.makedirs(path)
        return file
