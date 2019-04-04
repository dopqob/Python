#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 15:05
# @Author  : Bilon
# @File    : customer.py
import random
import logging
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from ccloud.common.desired_caps import appium_desired
from ccloud.common.common_func import Common, screenshot_error
from common_tools import create_gbk, create_name, create_phone


class Customer(Common):
    # 新增客户
    # id
    customer_name_id = 'customer_name'      # 店名
    contact_id = 'contact'      # 联系人
    mobile_id = 'mobile'        # 电话
    customer_type_id = 'default_customer_type'  # 选择客户类型
    sub_type_id = 'subType'     # 客户等级
    province_id = 'delivery-address'    # 省市区
    address_id = 'address'      # 详细地址
    upload_id = 'uploaderInput'  # 上传图片
    shutter_button_id = 'com.android.camera:id/shutter_button'  # 相机拍照按钮 X9
    done_button_id = 'com.android.camera:id/done_button'        # 相片确认按钮 X9
    # shutter_button_id = 'com.android.gallery3d:id/shutter_button'  # 相机拍照按钮 MX3
    # done_button_id = 'com.android.gallery3d:id/image_capture_done_img'  # 相片确认按钮 MX3
    add_id = 'add'  # 新增按钮

    # xpath
    addcustomer_entrance = '//*[@id="home"]/div[3]/div[2]/a[2]'  # 新增客户功能入口
    province_confirm = '//a[text()="完成"]'   # 省市区确定按钮
    addcustomer_confirm = '//a[text()="确定"]'    # 新增客户二次确认

    # class
    check_label = 'weui-check_label'    # 客户类型和客户等级选择

    # 常规拜访
    # id
    visit_entrance_id = 'photo'  # 常规拜访入口
    visit_complete_id = 'visitEnd'  # 拜访完成按钮

    # xpath
    cannel_enter_drafts = '//a[text()="取消"]'    # 取消进入草稿箱按钮
    visit_submit = '//button[contains(text(),"提交")]'  # 提交拜访
    visit_confirm = '//a[contains(text(),"确定")]'    # 提交拜访二次确认
    visit_complete_confirm = '//a[contains(text(),"确定")]'   # 拜访完成二次确认

    # 常规拜访补录
    visit_supplement_id = 'photoBL'   # 常规拜访补录入口
    add_photo_id = 'uploaderInput'  # 添加照片
    remark_id = 'question_desc'     # 添加备注信息

    @screenshot_error
    def add_customer(self, photo=True):
        """新增客户"""

        logging.info('========== add_customer ==========')

        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(self.addcustomer_entrance))
        self.driver.find_element_by_xpath(self.addcustomer_entrance).click()  # 进入新增客户页面

        # 填写客户名、联系人、手机号
        kinds = ['小店', '副食', '酒楼', '批发', '烟酒', '便利店', '小卖部', '超市', '百货']
        customer_name = create_name() + random.choice(kinds)
        self.driver.find_element_by_id(self.customer_name_id).send_keys(customer_name)
        self.driver.find_element_by_id(self.contact_id).send_keys(create_name())
        self.driver.find_element_by_id(self.mobile_id).send_keys(create_phone())

        # 选择客户类型
        self.driver.find_element_by_id(self.customer_type_id).click()
        typelist = ['零售终端', '批发', '餐饮', '其他', '商超']
        types = self.driver.find_elements_by_class_name(self.check_label)
        while True:
            t = int(random.randint(0, len(types)-1))
            if types[t].text in typelist:
                types[t].click()
                break

        # 选择客户等级
        self.driver.find_element_by_id(self.sub_type_id).click()
        sub_types = self.driver.find_elements_by_class_name(self.check_label)
        sub_types[random.randint(0, len(sub_types)-1)].click()

        # 选择配送地址
        self.driver.find_element_by_id(self.province_id).click()
        self.swich_webview(self.context)  # 切换到APP视图做swipe操作，滑动选择省市区
        width = self.driver.get_window_size().get('width')  # 获取屏幕宽度
        height = self.driver.get_window_size().get('height')  # 获取屏幕高度
        self.driver.swipe(width * 0.25, height * 0.9, width * 0.25, height * 0.1)  # 滑动
        self.driver.swipe(width * 0.9, height * 0.9, width * 0.9, height * 0.7)

        self.swich_webview(self.h5_context)  # 切换到H5视图继续后面的操作
        self.driver.find_element_by_xpath(self.province_confirm).click()
        self.driver.find_element_by_id(self.address_id).send_keys(create_gbk(8))

        if photo:
            for _ in range(random.randint(1, 3)):
                self.driver.find_element_by_id(self.upload_id).click()

                self.swich_webview(self.context)  # 切换到微信视图控制相机拍照
                # self.driver.find_element_by_id(self.shutter_button_id).click() # Meizu MX3
                # self.driver.find_element_by_id(self.done_button_id).click() # Meizu MX3
                self.driver.find_element_by_id(self.shutter_button_id).click()  # Vivo x9 拍照
                self.driver.find_element_by_id(self.done_button_id).click()  # Vivo x9 确定
                sleep(3)  # 等待图片上传完成

                self.driver.switch_to.context(self.h5_context)  # 切换到H5视图继续操作

        # 如果键盘弹出就关闭键盘
        # if self.driver.is_keyboard_shown():
        #     self.driver.hide_keyboard()

        self.driver.find_element_by_id(self.add_id).click()
        self.driver.find_element_by_xpath(self.addcustomer_confirm).click()
        sleep(1)

    @screenshot_error
    def customer_visit(self):
        """常规拜访"""

        logging.info('========== customer_visit ==========')

        # 进入"常规拜访"
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.visit_entrance_id))
        self.driver.find_element_by_id(self.visit_entrance_id).click()
        sleep(1)

        # 如果出现草稿箱已满的提示
        if self.is_element_exist(self.cannel_enter_drafts, 'xpath'):
            self.driver.find_element_by_xpath(self.cannel_enter_drafts).click()

        self.driver.find_element_by_id(self.remark_id).send_keys(create_gbk(30))  # 添加备注信息

        self.take_photo()   # 随机拍1-5张照片

        self.driver.find_element_by_xpath(self.visit_submit).click()
        sleep(1)

        self.driver.find_element_by_xpath(self.visit_confirm).click()
        sleep(1)

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.visit_complete_id))
        self.driver.find_element_by_id(self.visit_complete_id).click()  # 点击拜访完成按钮

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath(self.visit_complete_confirm))
        self.driver.find_element_by_xpath(self.visit_complete_confirm).click()  # 拜访完成二次确认
        sleep(1)

    @screenshot_error
    def customer_visit_supplement(self):
        """常规拜访-补录"""

        logging.info('========== customer_visit_supplement ==========')
        # 进入"常规拜访(补录）"
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.visit_supplement_id))
        self.driver.find_element_by_id(self.visit_supplement_id).click()
        sleep(1)

        self.driver.find_element_by_id(self.remark_id).send_keys(create_gbk(30))   # 添加备注信息

        self.upload_photo()     # 添加照片

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath(self.visit_submit))
        self.driver.find_element_by_xpath(self.visit_submit).click()    # 提交

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath(self.visit_confirm))
        self.driver.find_element_by_xpath(self.visit_confirm).click()   # 二次确认

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(self.visit_complete_id))
        self.driver.find_element_by_id(self.visit_complete_id).click()  # 点击拜访完成按钮
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath(self.visit_complete_confirm))
        self.driver.find_element_by_xpath(self.visit_complete_confirm).click()
        sleep(1)


if __name__ == '__main__':


    driver = appium_desired()
    customer = Customer(driver)
    # customer.enter_ccloud()

    # 新增客户
    # customer.add_customer()
    # customer.return_home_page()

    customer.enter_wechat_official_account('武汉珈研')
    for _ in range(50):
        customer.enter_applet()


        # 常规拜访
        customer.go_func_group_page()
        customer.customer_visit()

        customer.exit()

        print('第 {} 次执行完毕'.format(_+1))

    # 常规拜访补录
    # for _ in range(100):
    #     print('Start run loop {} '.format(_+1))
    #     customer.go_func_group_page()
    #     sleep(1)
    #     customer.customer_visit_supplement()
    #     customer.return_home_page()
    #     sleep(1)
