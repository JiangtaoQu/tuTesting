# -*- coding: utf-8 -*-
# @Time : 2019/7/16 14:43
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : kaoyanbang.py
# @Software: PyCharm
# from appium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
#
# capabilities = {
#     "platformName": "Android",
#     "platformVersion": "5.1.1",
#     "deviceName": "127.0.0.1:62025",
#     "appPackage": "com.tal.kaoyan",
#     "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
#     "noReset": True
# }
# # Remote——连接远端
# driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
# try:
#     # 是否有跳过
#     if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath(
#             "//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/activity_splash_top']")):
#         driver.find_element_by_xpath(
#             "//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/activity_splash_top']").click()
# except:
#     pass
# driver.find_element_by_xpath(
#     "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys('ttt1757773661')
# driver.find_element_by_xpath(
#     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.LinearLayout[1]").send_keys(
#     'ttt1757773661')
# driver.find_element_by_xpath(
#     "//android.widget.Button[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()
# driver.get_window_size()
# driver.swipe()