#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 11:23
# @Author  : Bilon
# @File    : wechat.py

"""
三种等待时间设置方法：
第一种 sleep()     设置固定时间休眠(python的time模块提供的方法)
第二种 implicitly_wait()   隐式等待
第三种 WebDriverWait()     显示等待
"""


from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import random


class wxTests:
    def setup(self):
        """初始化 启动微信"""
        caps = {
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'platformName': 'android',
            'deviceName': 'aaa',
            'noReset': 'true',
            'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
        }
        # caps["appPackage"] = "com.tencent.mm"
        # caps["appActivity"] = ".ui.LauncherUI"
        # caps["platformName"] = "android"
        # caps["deviceName"] = "aaa"
        # caps["noReset"] = "true"
        # caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        # sleep(15)

    # def open_ccloud(self):
        """打开'武汉珈研'微信公众号 进入'订单云平台' """
        jy_id = 'com.tencent.mm:id/azl'     # 武汉珈研公众号ID
        ent_id = 'com.tencent.mm:id/po'     # 订单云平台入口ID

        # 查找'武汉珈研'公众号是否存在，如果10秒内没有找到提示超时并退出
        # print(EC.presence_of_element_located(By.ID, jy_id))
        try:
            self.driver.find_element_by_id(jy_id).click()
        except Exception:
            sleep(5)
            self.driver.find_element_by_id(jy_id).click()
        except:
            print('没有找到武汉珈研公众号入口')
            self.driver.quit()

        # 查找'订单云平台'是否存在，如果10秒内没有找到提示超时并退出
        try:
            self.driver.find_elements_by_id(ent_id)[1].click()
        except TimeoutError:
            print('没有找到订单云平台入口')
            self.driver.quit()

        # 查找视图 如果视图不存在给予提示并退出
        try:
            webview = 'WEBVIEW_com.tencent.mm:tools'
            sleep(5)
            contexts = self.driver.contexts
            print('第1次获取到的上下文： {}'.format(contexts))
            if webview in contexts:
                # 切换到H5页面的webview
                self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
                handles = self.driver.window_handles  # 获取当前窗口句柄
                if len(handles) > 1:  # 如果有多个句柄，切换到最后一个
                    self.driver.switch_to.window(handles[-1])
            else:
                sleep(5)
                contexts = self.driver.contexts
                print('第2次获取到的上下文： {}'.format(contexts))
                self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
                handles = self.driver.window_handles  # 获取当前窗口句柄
                if len(handles) > 1:  # 如果有多个句柄，切换到最后一个
                    self.driver.switch_to.window(handles[-1])
        except Exception:
            print('视图切换失败，用例提前结束')
            self.driver.quit()

        # 进入聚合客户列表
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, "customerVisits"))
        # 等待 customerVisits 加载完毕，最多等10秒
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("customerVisits"))
        self.driver.find_element_by_id("customerVisits").click()
        sleep(3)
        # 获取客户数 随机选择一个客户
        customer = self.driver.find_elements_by_xpath('//*[@id="customerList"]/div')
        print('一共有 {} 个客户'.format(len(customer)))
        if len(customer) == 0:
            print('客户加载失败，用例提前结束')
            self.driver.quit()
        else:
            i = random.randint(0, len(customer)-1)
            customer[i].click()

        # 切换到弹窗iframe
        self.driver.switch_to.frame('layui-layer-iframe1')
        # print(driver.page_source)
        # 进入客户拜访
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, "photo"))
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("photo"))
        self.driver.find_element_by_id('photo').click()
        # sleep(3)

        # 循环三次 拍三张照片
        for i in range(3):
            shot_xpath = '//*[@id="form"]/section[2]/div[3]/div/div/div/div/div'
            # WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//div[contains(text(),"选择图片")]'))
            # self.driver.find_element_by_xpath('//div[contains(text(),"选择图片")]').click()

            # try:
            WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element_by_xpath(shot_xpath))
            self.driver.find_element_by_xpath(shot_xpath).click()
            # except Exception:
            #     print('没有找到添加图片按钮，3秒后再次查找')
            #     sleep(3)
            #     self.driver.find_element_by_xpath(shot_xpath).click()
            # except:
            #     print('找不到添加图片按钮，用例提前结束')
            #     self.driver.quit()

            self.driver.switch_to.context("NATIVE_APP")

            # self.driver.find_element_by_id('com.android.gallery3d:id/shutter_button').click()
            # self.driver.find_element_by_id('com.android.gallery3d:id/image_capture_done_img').click()
            self.driver.find_element_by_id('com.android.camera:id/shutter_button').click()  # Vivo x9
            self.driver.find_element_by_id('com.android.camera:id/done_button').click()  # Vivo x9
            sleep(3)

            self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//button[contains(text(),"提交")]'))
        self.driver.find_element_by_xpath('//button[contains(text(),"提交")]').click()

        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
            sleep(1)
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        except Exception:
            print('没有找到"确定按钮"，3秒后再次查找')
            sleep(3)
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        except:
            print('没有找到"确定"按钮,用例提前结束')
            self.driver.quit()

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("visitEnd"))
        self.driver.find_element_by_id('visitEnd').click()
        # sleep(3)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//a[contains(text(),"确定")]'))
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        sleep(3)
        print('用例正常执行完毕')

        self.driver.quit()


if __name__ == '__main__':
    meizu = wxTests()
    for i in range(1):
        print('{0} 第 {1} 次执行开始 {2}'.format('-'*20, i+1, '-'*20), end='\n')
        meizu.setup()
        print('{0} 第 {1} 次执行完毕 {2}'.format('-'*20, i+1, '-'*20), end='\n\n')
    # meizu.open_ccloud()
