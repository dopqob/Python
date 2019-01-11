#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 11:21
# @Author  : Bilon
# @File    : test_activity.py
import logging
import unittest
from HTMLTestRunner import HTMLTestRunner
from ccloud.common.myunit import StartEnd
from ccloud.businessView.activity import NormalActivity, MarketingCampaign


class ActivityTest(StartEnd):
    """活动测试"""

    def test_normal_activity(self):
        """活动快捷执行"""
        logging.info('******************** test_normal_activity ********************')
        act = NormalActivity(self.driver)
        act.enter_ccloud()
        act.go_func_group_page()
        act.normal_activity()

    # @unittest.skip('消费培育活动')
    def test_cultivate_activity(self):
        """消费培育活动"""
        logging.info('******************** test_cultivate_activity ********************')
        act = MarketingCampaign(self.driver)
        act.enter_ccloud()
        act.go_mycenter()
        act.cultivate_activity()
        self.assertEqual(self.driver.title, '营销推广')

    # @unittest.skip('团购直销活动')
    def test_groupon_activity(self):
        """团购直销活动"""
        logging.info('******************** test_groupon_activity ********************')
        act = MarketingCampaign(self.driver)
        act.enter_ccloud()
        act.go_mycenter()
        act.groupon_activity()
        self.assertEqual(self.driver.title, '营销推广')

    # @unittest.skip('宴席推广活动')
    def test_feast_activity(self):
        """宴席推广活动"""
        logging.info('******************** test_feast_activity ********************')
        act = MarketingCampaign(self.driver)
        act.enter_ccloud()
        act.go_mycenter()
        act.feast_activity()
        self.assertEqual(self.driver.title, '营销推广')


if __name__ == '__main__':
    file_path = StartEnd.create_report_file()
    with open(file_path, 'wb') as f:
        unittest.main(testRunner=HTMLTestRunner(stream=f, title=u'Ccloud测试报告', description=u'测试结果:'))