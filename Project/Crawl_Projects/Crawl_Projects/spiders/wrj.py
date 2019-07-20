# -*- coding: utf-8 -*-
# @Time : 2019/7/6 9:28
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : wrj.py
# @Software: PyCharm
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from ..items import WRJItem
from scrapy.loader import ItemLoader
import re


class WrjSpider(CrawlSpider):
    name = 'wrj'
    collection = 'news'
    # allowed_domains = ['www.test.com']
    start_urls = ['https://www.81uav.cn/uav-news/']

    rules = (
        # 翻页链接，从 start_urls 的 response 里所有的 LINK
        # 找匹配的 正则 页面
        # follow=True——更加深入页面
        Rule(LinkExtractor(allow=r'/uav-news/index-htm-page-\d+\.html'), follow=True),
        # 详情页链接
        # 只要匹配到了就 callback 函数，后面的函数写函数名
        Rule(LinkExtractor(allow=r'/uav-news/\d{6}/\d{2}/\d+\.html'), callback='parse_item', follow=False)
    )

    # rules 和 parse 不能同时使用，如果有 parse 就不走 rules 了。
    def parse_item(self, response):
        # print(response.url)
        title = response.xpath('//h1/text()').get()
        # print(title)
        content = response.xpath('string(//div[@id="content"])').getall()
        content = ''.join(list(map(lambda x: re.sub(r'\s{2,}', '', x.strip()), content)))
        # print(content)
        IL = ItemLoader(item=WRJItem(), response=response)
        IL.add_value(field_name='title_wrj', value=title)
        IL.add_value(field_name='content', value=content)
        return IL.load_item()
