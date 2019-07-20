# -*- coding: utf-8 -*-
# @Time : 2019/7/16 15:54
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : jinritoutiao.py
# @Software: PyCharm
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.loader import ItemLoader
from utils.server_post import postData_to_dict
import json


class WrjSpider(CrawlSpider):
    name = 'jinritoutiao'
    collection = 'news'
    # allowed_domains = ['www.test.com']
    category = 'news_tech'
    list_count = 1
    start_urls = [
        'https://is-hl.snssdk.com/api/news/feed/v88/?list_count={}&category={}&tdsourcetag=s_pctim_aiomsg'.format(
            list_count, category)]


def parse(self, response):
    data = json.loads(response.text)['data']
    for i in data:
        content = json.loads(i['content'])
        abstract = content['abstract']
        article_url = content['article_url']
        yield scrapy.Request(article_url, self.detail, meta={'abstract': abstract})


def detail(self, response):
    print(response.url)
    print(response.meta['abstract'])
    # article_title = response.xpath('//h1/text()').get('暂无')
    # print(article_title)
