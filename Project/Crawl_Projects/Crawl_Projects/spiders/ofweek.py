# -*- coding: utf-8 -*-
# @Time : 2019/7/10 10:50
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : ofweek.py
# @Software: PyCharm
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from ..items import OfWeekItem
from scrapy.loader import ItemLoader


class OfWeekSpider(CrawlSpider):
    name = 'ofweek'
    collection = 'news'
    # allowed_domains = ['www.test.com']
    start_urls = ['https://www.ofweek.com/']
    rules = (
        Rule(LinkExtractor(allow=(r'//[\w]+\.ofweek\.com/[\w]*/*',), restrict_xpaths=('//link',)), follow=True),
        Rule(
            LinkExtractor(
                allow=(r'https://[\w]+\.ofweek\.com/[\w]*/*[\d]{4}-[\d]{2}/ART-[\d]{6}-[\d]{4}-[\d]{8}\.html',)),
            callback='parse_item')
    )

    def parse_item(self, response):
        # print(response.url)
        title = response.xpath('//p[@class="title"]/text()').get()
        # print(title)
        date = response.xpath('//div[@class="time fl"]/text()').get().strip()
        # print(date)
        IL = ItemLoader(item=OfWeekItem(), response=response)
        IL.add_value(field_name='title', value=title)
        IL.add_value(field_name='date', value=date)
        return IL.load_item()
