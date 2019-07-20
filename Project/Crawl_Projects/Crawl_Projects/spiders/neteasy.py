# -*- coding: utf-8 -*-
# @Time : 2019/7/6 9:26
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : neteasy.py
# @Software: PyCharm
from scrapy.spiders import CrawlSpider, Rule
# LinkExtractor——连接提取器
from scrapy.linkextractors import LinkExtractor
import re
# ItemLoader——数据加载器
from scrapy.loader import ItemLoader
from ..items import WYItem


class Neteasy(CrawlSpider):
    name = 'neteasy'
    collection = 'news'
    start_urls = ['http://tech.163.com/special/gd2016/']
    rules = (
        Rule(LinkExtractor(allow=r'http://tech.163.com/special/gd2016_\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'https://tech.163.com/\d{2}/\d{4}/\d{2}/[\w\d]{16}.html'),
             callback='parse_item'),
    )

    def parse_item(self, response):
        # print(response.url)
        title = response.xpath('//h1/text()').get().strip()
        # print(title)
        content = response.xpath('string(//div[@id="endText"])').getall()
        ret = ''.join(list(map(lambda x: re.sub(r'\s{2,}', '', x.strip()), content)))
        # 实例化
        IL = ItemLoader(item=WYItem(), response=response)
        # value 自动转成 list
        IL.add_value(field_name='title_wy', value=title)
        IL.add_value(field_name='newsDigest', value=ret)
        # 将提取好的数据一并 load 出来
        return IL.load_item()
