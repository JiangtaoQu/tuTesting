# -*- coding: utf-8 -*-
# @Time : 2019/7/15 9:11
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : xinhuawang.py
# @Software: PyCharm
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.loader import ItemLoader
from utils.server_post import postData_to_dict
import json


class WrjSpider(CrawlSpider):
    name = 'xinhuawang'
    collection = 'news'
    # allowed_domains = ['www.test.com']
    start_urls = ['http://api.app.xinhuanet.com/1.0/touTiao/list%20HTTP/1.1']

    def start_requests(self):
        url = 'http://api.app.xinhuanet.com/1.0/touTiao/list'
        str1 = 'udid=1b6ae2bcf7ef5283&openudid=1b6ae2bcf7ef5283&device_model=OPPO%20R11&os=Android&os_version=5.1.1&resolution=1440000&device_brand=OPPO%20&offset=0'
        form_data = postData_to_dict(str1)
        # print(form_data)
        headers = {
            'device-token': '64cda4c9370025ee25ee6707577c51e3',
        }
        # print(form_data)
        yield scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse, headers=headers)

    def parse(self, response):
        # response.text 是 str 转 dict 用 json.loads
        ret = json.loads(response.text)['data']
        for i in ret:
            title = i.get('title', '无')
            source = i.get('source', '无')
            user_info = i.get('user_info', '无')
            article_url = i.get('article_url', '无')
            # home_page = i.get('user_info', '无').get('home_page', '无')
            # print(article_url)
            yield scrapy.Request(article_url, callback=self.parse1)

    def parse1(self, response):
        print(response.url)
