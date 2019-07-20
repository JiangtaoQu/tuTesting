# -*- coding: utf-8 -*-
# @Time : 2019/7/8 20:47
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : huanqiu.py
# @Software: PyCharm
import scrapy
from scrapy.loader import ItemLoader
from ..items import HuanQiuItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class HuanQiuSpider(CrawlSpider):
    name = 'huanqiu'
    collection = 'news'
    # allowed_domains = ['example.com']
    start_urls = ['http://tech.huanqiu.com/']

    rules = {
        # 取出每个分类链接
        Rule(LinkExtractor(allow=r'http://tech.huanqiu.com/\w+/'), follow=True),
        # 分页链接(取前十页)
        # Rule(LinkExtractor(allow=r'http://tech.huanqiu.com/\w+/{page}\.html'.format(page=[i for i in range(1, 11)])),
        Rule(LinkExtractor(allow=r'http://tech.huanqiu.com/\w+/([1,2,3,4,5,6,7,8,9]{1}|10)\.html'),
             follow=True),
        # 详情页
        Rule(LinkExtractor(allow=r'http://tech.huanqiu.com/\w+/\d{4}-\d{2}/\d{8}\.html'), callback='parse_item')
    }

    def parse_item(self, response):
        hq_title = response.xpath('//h1/text()').get('无')
        print(hq_title)
        hq_publish_date = response.xpath('//span[@class="la_t_a"]/text()').get('无')
        hq_author = response.xpath('//span[@class="author"]/text()').get('无')
        # hq_content =
        hq_image_url = response.xpath('//img/@src').getall()
        # hq_category =
        # hq_language =
        hq_module = response.xpath('/html/body/div[5]/div[2]/div[1]/a[3]/text()').get('无')
        # hq_html_content = scrapy.Field()
        # hq_copyright = scrapy.Field()
        # hq_site_name = scrapy.Field()
        # hq_meta_data = scrapy.Field()
        # hq_hash_code = scrapy.Field()
        # hq_url = scrapy.Field()
        IL = ItemLoader(item=HuanQiuItem(), response=response)
        IL.add_value(field_name='hq_publish_date', value=hq_publish_date)
        IL.add_value(field_name='hq_author', value=hq_author)
        IL.add_value(field_name='hq_image_url', value=hq_image_url)
        IL.add_value(field_name='hq_module', value=hq_module)
        return IL.load_item()
