#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 9:51
# @Author  : Bilon
# @File    : activity.py
import random
import logging
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error
from common_tools import create_phone, create_name, create_gbk


class ActivityCommon(Common):
    """活动基类，封装一些公共方法"""

    # id
    act_enter_id = 'activity_quick'     # 活动快捷执行入口
    act_choose_id = 'activity_title'    # 选择活动
    expense_id = 'expenses_ids'         # 选择费用明细
    able_num_id = 'ableNum'            # 可用赠送数量
    apply_num_id = 'apply_num1'         # 赠送数量输入框
    able_money_id = 'ableMoney'        # 可用赠送金额
    apply_amount_id = 'apply_amount1'   # 赠送金额输入框

    banquet_type_id = 'banquet_type'   # 宴席类型选择
    company_name_id = 'companyName'    # 单位名称
    contact_id = 'customerNames'       # 联系人/培育对象
    mobile_id = 'customerMobile'       # 电话
    address_id = 'customerAddress'     # 地址
    people_id = 'people'               # 人数/桌数

    # class
    check_label_class = 'weui-check_label'    # 活动列表和费用明细列表
    submit_class = 'weui-footer'              # 活动提交按钮
    act_choose_class = 'weui-input'           # 营销推广活动选择

    # xpath
    confirm_xpath = '//a[text()="确定"]'       # 二次确认按钮
    re_unload_xpath = '//a[contains(text(),"继续上传")]'    # 继续上传
    close_layer_xpath = '/html/body/div[2]'     # 关闭弹层
    marketing_enter_xpath = '//p[text()="营销推广"]'  # 营销推广入口
    marketing_supplement_xpath = '//p[text()="营销补录"]'   # 营销补录入口
    drafts_box_cancel_xpath = '/html/body/div[6]/div[3]/a[1]'    # 取消进入拜访草稿箱

    def choose_act(self):
        """选择活动"""

        logging.info('========== choose_act ==========')

        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(self.act_choose_id))
        self.driver.find_element_by_id(self.act_choose_id).click()
        sleep(1)

        acts = self.driver.find_elements_by_class_name(self.check_label_class)
        # acts[random.randint(0, len(acts) - 1)].click()
        random.choice(acts).click()
        sleep(1)

    def choose_expense(self):
        """选择费用明细"""

        logging.info('========== choose_expense ==========')

        self.driver.find_element_by_id(self.expense_id).click()
        sleep(0.5)

        costs = self.driver.find_elements_by_class_name(self.check_label_class)
        # costs[random.randint(0, len(costs) - 1)].click()
        random.choice(costs).click()
        sleep(0.5)
        self.driver.find_element_by_xpath(self.confirm_xpath).click()
        sleep(0.5)

    def apply_num(self):
        """赠送数量"""

        logging.info('========== apply_num ==========')
        if self.is_element_exist(self.apply_num_id, 'id'):  # 非补录时数量输入框的id是apply_num1
            if self.driver.find_element_by_id(self.apply_num_id).is_displayed():  # is_displayed 如果元素可见
                available_num = self.driver.find_element_by_id(self.able_num_id).text[1:-1]  # 可用赠送数量
                if int(available_num) <= 0:
                    self.driver.find_element_by_id(self.apply_num_id).clear().send_keys(0)
                else:
                    self.driver.find_element_by_id(self.apply_num_id).clear().send_keys(random.randint(1, 5))
                sleep(0.5)

        if self.is_element_exist(self.apply_num_id[:-1], 'id'):     # 补录时数量输入框的id是apply_num
            if self.driver.find_element_by_id(self.apply_num_id[:-1]).is_displayed():
                available_num = self.driver.find_element_by_id(self.able_num_id).text[1:-1]  # 可用赠送数量
                if int(available_num) <= 0:
                    self.driver.find_element_by_id(self.apply_num_id[:-1]).clear().send_keys(0)
                else:
                    self.driver.find_element_by_id(self.apply_num_id[:-1]).clear().send_keys(random.randint(1, 5))
                sleep(0.5)

    def apply_amount(self):
        """赠送金额"""

        logging.info('========== apply_amount ==========')
        if self.is_element_exist(self.apply_amount_id, 'id'):   # 非补录时金额输入框的id是apply_amount1
            if self.driver.find_element_by_id(self.apply_amount_id).is_displayed():
                amount_list = [10, 20, 30, 50, 80, 100]
                available_amount = self.driver.find_element_by_id(self.able_money_id).text[1:-1]  # 可用赠送金额
                while True:
                    amount = random.choice(amount_list)  # 从列表中随机选择一个元素
                    if amount <= int(available_amount):
                        self.driver.find_element_by_id(self.apply_amount_id).clear().send_keys(amount)
                        break

        if self.is_element_exist(self.apply_amount_id[:-1], 'id'):  # 补录时金额输入框的id是apply_amount
            if self.driver.find_element_by_id(self.apply_amount_id[:-1]).is_displayed():
                amount_list = [10, 20, 30, 50, 80, 100]
                available_amount = self.driver.find_element_by_id(self.able_money_id).text[1:-1]  # 可用赠送金额
                while True:
                    amount = random.choice(amount_list)  # 从列表中随机选择一个元素
                    if amount <= int(available_amount):
                        self.driver.find_element_by_id(self.apply_amount_id[:-1]).clear().send_keys(amount)
                        break

    def submit(self):
        """提交活动"""

        logging.info('========== submit ==========')
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name(self.submit_class))
        submits = self.driver.find_elements_by_class_name(self.submit_class)
        for submit in submits:
            if submit.text == '提交':
                submit.click()
                break
        sleep(0.5)

    def reconfirm(self):
        """再次确认"""

        logging.info('========== reconfirm ==========')
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(self.confirm_xpath))
        self.driver.find_element_by_xpath(self.confirm_xpath).click()
        sleep(1)

    # def drafts_box(self):
    #     """取消进入拜访草稿箱"""
    #     if self.is_element_exist(self.drafts_box_cancel_xpath, 'xpath'):
    #         # if self.driver.find_element_by_xpath(self.drafts_box_cancel_xpath).is_displayed():
    #         logging.info('-------- cancel entry to draft box --------')
    #         self.driver.find_element_by_xpath(self.drafts_box_cancel_xpath).click()


class NormalActivity(ActivityCommon):
    """普通活动"""
    @screenshot_error
    def normal_activity(self, flag=True):
        """活动快捷执行"""

        # 进入"活动快捷执行"
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(self.act_enter_id))
        self.driver.find_element_by_id(self.act_enter_id).click()
        sleep(1)

        # 如果出现草稿箱已满的提示，点取消
        # self.drafts_box()

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 输入赠送数量
        self.apply_num()

        # 输入赠送金额
        # if self.is_element_exist('apply_amount', 'id'):
        self.apply_amount()

        # 随机拍1-5张照
        self.take_photo(flag)

        # 提交
        self.submit()

        # 如果出现继续上传的提示，点击继续上传
        if self.is_element_exist(self.re_unload_xpath, 'xpath'):
            self.driver.find_element_by_xpath(self.re_unload_xpath).click()
            sleep(5)
            self.submit()

        # 二次确认
        self.reconfirm()

        # 关闭弹层
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(self.close_layer_xpath))
        self.driver.find_element_by_xpath(self.close_layer_xpath).click()


class MarketingCampaign(ActivityCommon):
    """营销推广活动"""

    def choose_activity_type(self, num):
        """进入营销推广并选择活动类型"""

        logging.info('========== choose_activity_type ==========')

        # 进入营销推广
        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_xpath(self.marketing_enter_xpath))
        self.driver.find_element_by_xpath(self.marketing_enter_xpath).click()
        sleep(0.5)

        act_kinds = self.driver.find_elements_by_class_name(self.act_choose_class)
        act_kinds[num].click()
        sleep(3)

    def choose_activity_supplement_type(self, num):
        """进入营销补录并选择活动类型"""

        logging.info('========== choose_activity_supplement_type ==========')

        # 进入营销推广
        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_xpath(self.marketing_supplement_xpath))
        self.driver.find_element_by_xpath(self.marketing_supplement_xpath).click()
        sleep(0.5)

        act_kinds = self.driver.find_elements_by_class_name(self.act_choose_class)
        act_kinds[num].click()
        sleep(1)

    @screenshot_error
    def cultivate_activity(self, flag=True):
        """消费培育活动"""

        # 选择消费培育活动
        self.choose_activity_type(0)
        logging.info('========== cultivate_activity ==========')

        # 如果出现草稿箱已满的提示，点取消
        # self.drafts_box()

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 培育对象名称
        self.driver.find_element_by_id(self.contact_id).send_keys(create_name())

        # 培育对象电话
        self.driver.find_element_by_id(self.mobile_id).send_keys(create_phone())

        # 培育地点
        self.driver.find_element_by_id(self.address_id).send_keys(create_gbk(6))

        # 品鉴人数
        self.driver.find_element_by_id(self.people_id).send_keys(random.randint(1, 3))

        # 赠送数量
        self.apply_num()

        # 赠送金额
        self.apply_amount()

        # 随机拍1-5张照
        self.take_photo(flag)

        # 提交
        self.submit()

        # 再次确认
        self.reconfirm()

    @screenshot_error
    def groupon_activity(self, flag=True):
        """团购直销活动"""

        # 进入团购直销活动
        self.choose_activity_type(1)
        logging.info('========== groupon_activity ==========')

        # 如果出现草稿箱已满的提示，点取消
        # self.drafts_box()

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 团购单位名称
        self.driver.find_element_by_id(self.company_name_id).send_keys(create_gbk(5))

        # 单位负责人
        self.driver.find_element_by_id(self.contact_id).send_keys(create_name())

        # 联系电话
        self.driver.find_element_by_id(self.mobile_id).send_keys(create_phone())

        # 赠送数量
        self.apply_num()

        # 赠送金额
        self.apply_amount()

        # 随机拍1-5张照
        self.take_photo(flag)

        # 提交
        self.submit()

        # 再次确认
        self.reconfirm()

    @screenshot_error
    def feast_activity(self, flag=True):
        """宴席推广活动"""

        # 进入宴席推广活动
        self.choose_activity_type(2)
        logging.info('========== feast_activity ==========')

        # 如果出现草稿箱已满的提示，点取消
        # self.drafts_box()

        # 选择宴席类型
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.banquet_type_id))
        self.driver.find_element_by_id(self.banquet_type_id).click()
        sleep(0.5)
        banquets = self.driver.find_elements_by_class_name(self.check_label_class)
        # banquets[random.randint(0, len(banquets) - 1)].click()
        random.choice(banquets).click()
        sleep(1)

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 联系人
        self.driver.find_element_by_id(self.contact_id).send_keys(create_name())

        # 电话
        self.driver.find_element_by_id(self.mobile_id).send_keys(create_phone())

        # 地址
        self.driver.find_element_by_id(self.address_id).send_keys(create_gbk(6))

        # 桌数
        self.driver.find_element_by_id(self.people_id).send_keys(random.randint(1, 3))

        # 赠送数量
        self.apply_num()

        # 赠送金额
        self.apply_amount()

        # 随机拍1-5张照
        self.take_photo(flag)

        # 提交
        self.submit()

        # 再次确认
        self.reconfirm()

    @screenshot_error
    def cultivate_activity_supplement(self, flag=True):
        """消费培育活动-补录"""

        # 选择消费培育活动
        self.choose_activity_supplement_type(0)
        logging.info('========== cultivate_activity_supplement ==========')

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 培育对象名称
        self.driver.find_element_by_id(self.contact_id).send_keys(create_name())

        # 培育对象电话
        self.driver.find_element_by_id(self.mobile_id).send_keys(create_phone())

        # 培育地点
        self.driver.find_element_by_id(self.address_id).send_keys(create_gbk(6))

        # 品鉴人数
        self.driver.find_element_by_id(self.people_id).send_keys(random.randint(1, 3))

        # 赠送数量
        self.apply_num()

        # 赠送金额
        self.apply_amount()

        # 上传照片
        self.upload_photo(flag)

        # 提交
        self.submit()

        # 再次确认
        self.reconfirm()
        sleep(2)

    @screenshot_error
    def groupon_activity_supplement(self, flag=True):
        """团购直销活动-补录"""

        # 进入团购直销活动
        self.choose_activity_supplement_type(1)
        logging.info('========== groupon_activity_supplement ==========')

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 团购单位名称
        self.driver.find_element_by_id(self.company_name_id).send_keys(create_gbk(5))

        # 单位负责人
        self.driver.find_element_by_id(self.contact_id).send_keys(create_name())

        # 联系电话
        self.driver.find_element_by_id(self.mobile_id).send_keys(create_phone())

        # 赠送数量
        self.apply_num()

        # 赠送金额
        self.apply_amount()

        # 上传照片
        self.upload_photo(flag)

        # 提交
        self.submit()

        # 再次确认
        self.reconfirm()
        sleep(2)

    @screenshot_error
    def feast_activity_supplement(self, flag=True):
        """宴席推广活动-补录"""

        # 进入宴席推广活动
        self.choose_activity_supplement_type(2)
        logging.info('========== feast_activity_supplement ==========')

        # 选择宴席类型
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.banquet_type_id))
        self.driver.find_element_by_id(self.banquet_type_id).click()
        banquets = self.driver.find_elements_by_class_name(self.check_label_class)
        banquets[random.randint(0, len(banquets) - 1)].click()
        # sleep(1)

        # 选择活动
        self.choose_act()

        # 选择费用明细
        self.choose_expense()

        # 联系人
        self.driver.find_element_by_id(self.contact_id).send_keys(create_name())

        # 电话
        self.driver.find_element_by_id(self.mobile_id).send_keys(create_phone())

        # 地址
        self.driver.find_element_by_id(self.address_id).send_keys(create_gbk(6))

        # 桌数
        self.driver.find_element_by_id(self.people_id).send_keys(random.randint(1, 3))

        # 赠送数量
        self.apply_num()

        # 赠送金额
        self.apply_amount()

        # 上传照片
        self.upload_photo(flag)

        # 提交
        self.submit()

        # 再次确认
        self.reconfirm()
        sleep(2)


if __name__ == '__main__':
    driver = appium_desired()
    act = NormalActivity(driver)
    act.enter_ccloud()
    for _ in range(1):
        act.go_func_group_page()
        act.normal_activity()
        act.return_home_page()
    # market = MarketingCampaign(driver)
    # market.enter_ccloud()
    # for _ in range(2):
        # market.go_mycenter()
        # market.cultivate_activity()
        # market.return_home_page()
        # market.go_mycenter()
        # market.groupon_activity()
        # market.return_home_page()
        # market.go_mycenter()
        # market.feast_activity()
        # market.return_home_page()
        # market.go_mycenter()
        # market.cultivate_activity_supplement()
        # market.return_home_page()
        # market.go_mycenter()
        # market.groupon_activity_supplement()
        # market.return_home_page()
        # market.go_mycenter()
        # market.feast_activity_supplement()
        # market.return_home_page()
        # logging.info('************* 第 {} 次执行完毕 *************'.format(_+1))
