# -*- coding: utf-8 -*-
# @Time : 2019/6/12 9:12
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : envi.py
# @Software: PyCharm
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.baidu.com')
browser.find_element_by_id('kw').send_keys('大地瓜')
browser.find_element_by_id('su').click()
