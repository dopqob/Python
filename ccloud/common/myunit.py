#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 11:32
# @Author  : Bilon
# @File    : myunit.py
import os
import time
import logging
import unittest
from time import sleep
from ccloud.common.desired_caps import appium_desired


class StartEnd(unittest.TestCase):

    def setUp(self):
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('******************** tearDown ********************\n')
        sleep(1)
        self.driver.quit()

    @classmethod
    def create_report_file(cls):
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        path = "..\\TestReport\\" + day
        create_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        file = path + "\\" + create_time + "_" + 'report.html'
        if not os.path.exists(path):
            os.makedirs(path)
        return file
