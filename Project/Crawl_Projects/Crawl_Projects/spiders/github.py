# -*- coding: utf-8 -*-
# @Time : 2019/7/18 17:05
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : github.py
# @Software: PyCharm
# import scrapy
# import re
# from utils.server_post import postCookies_to_dict
# from scrapy.http.cookies import CookieJar
#
#
# class GitHubSpider(scrapy.Spider):
#     name = 'github'
#     # allowed_domains = ['example.com']
#     start_urls = ['https://github.com/login']
#     Cookie = {
#         'Cookie': 'has_recent_activity=1; logged_in=no; _ga=GA1.2.1654949503.1563519428; _gat=1; tz=Asia%2FShanghai; _octo=GH1.1.466675443.1563519432; _gh_sess=TEdSRFVvUWc1NGF5MC9yd2NvTXQ5NTl3YVpwREVkeUdaNE0wQk0zeDA3Qi81UFUwSG1LVjFyY0J4Y3k5VUhqa1VaVnVtUlYwMTQ0SEJYZURkMldjZHEwendCM1k5aTZEc2JUN1lUNjdKaFBZTUZPUVRhYnFsV1krQmlBcjFOZFdYTk5paTFGVDVTRnpjWW1QWFZuWVhmUENRcTJlSE5OL09TQnhWWnNsdDFtZkxQa2w0L1VZVGowbkJnQ3g3R1I5eExFR2FIVXF1Q3c1YnRvV041YVovL1JhdFZBWTlCVTNYTUgwL0sxU3UwWXY1K0x6bko4ZHZhQklwVnBmNmVIWXBieG9VeDFIbmxvZFRSMzdZUFd0UU5McldjMDlCT0tHRDBqSVJac0Y2dlBNZXl2cVR0UDQwWWFYSjNGT2J2L2VNSldEWUJsWUxkYlg0WjFPRjgyb3QyM2FhMEV3NWhpTFJWTFBtdVpwTXJaclNYSlBxWFMzZjdIMk13eFBSWXhOTi9NdlJSUXN3aEJYelY4R3FFUDVDOHVGSWhoMEV0WnpOV2tUWXBieDdVZUlVRGxUS1JnVytmRzIzY0VKWGk3S0ZXQTVqSk9GMmRPMTBhOVY1TE03M1Q3ZENaRW5GNDN5NUQxSkVxUEdmRXc9LS10M0FKMGQ1U3lnVFhEYXJEKzAxdFd3PT0%3D--875b43965b0a9dc144beabaf3d71a51a5f5d5450'}
#
#     # 在 start_requests 获取 cookies
#     # def start_requests(self):
#     #     url = 'https://github.com/session'
#     #     # 通过meta传入 cookiejar 特殊 key ，爬取url作为参数传给回调函数
#     #     # meta：字典格式的元数据
#     #     # cookiejar：是meta的一个特殊的key，通过cookiejar参数可以支持多个会话对某网站进行爬取
#     #     # 可以对cookie做标记1, 2, 3, 4......这样scrapy就维持了多个会话
#     #     yield scrapy.Request(url, meta={'cookiejar': 1}, callback=self.github_login)
#
#     def parse(self, response):
#         # cookiejar = CookieJar()
#         # cookiejar.extract_cookies(response, response.request)
#         url = 'https://github.com/session'
#         authenticity_token = response.xpath('//*[@id="login"]/form/input[2]/@value').extract_first()
#         # print(authenticity_token)
#         formdata = {
#             'commit': 'Sign in',
#             'utf8': '✓',
#             'authenticity_token': authenticity_token,
#             'login': 'ai.ei.ui@live.cn',
#             'password': '892635566665c5db6254ffd29534b9a8',
#             # 'login': '',
#             # 'password': '',
#             'webauthn-support': 'supported',
#         }
#         yield scrapy.FormRequest(
#             url=url,
#             callback=self.after_login,
#             cookies=self.Cookie,
#             formdata=formdata,
#         )
#
#     def after_login(self, response):
#         home_page = response.xpath(".//*[@id='dashboard']/div[2]/div[1]/nav/a[1]/text()").extract()
#         # 获取登录成功后页面中的文本“Browse activity”
#         with open('a.html', 'w')as f:
#             f.write(response.body.decode())
#
#         if 'Browse activity' in home_page:
#             self.logger.info('登录成功！')
#             # 如果含有“Browse activity”，则打印登录成功
#         else:
#             self.logger.error('登录失败！')

import random


class IPProxyDownloadMiddleware:
    PROXIES = [
        '178.44.170.152:48182',
        '60.167.20.253:20701',
        '111.177.164.37:37485',
    ]

    def process_request(self, request, spider):
        proxy = random.choice(self.PROXIES)
        if request.url.startswith('http://'):
            request.meta['proxy'] = 'http://' + proxy
        elif request.url.startswith('https://'):
            request.meta['proxy'] = 'https://' + proxy
C:\Users\Quantum\Documents\GitHub\Project\Crawl_Projects