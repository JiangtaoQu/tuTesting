# -*- coding: utf-8 -*-
# @Time : 2019/7/8 19:18
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : food.py
# @Software: PyCharm
import scrapy
from scrapy.loader import ItemLoader
from ..items import FoodItem


class FoodSpider(scrapy.Spider):
    name = 'food'
    collection = 'news'
    # allowed_domains = ['example.com']
    start_urls = ['http://bz.cfsa.net.cn/db']

    def start_requests(self):
        url = 'http://bz.cfsa.net.cn/db'
        form_data = {
            'task': 'listStandardGJ',
            'accessData': 'gj',
        }
        yield scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        # print(response.url)
        codes = response.xpath('//a[@href="javascript:void(0)"]/@onclick').re(r"\('(.*?)',")
        for code in codes:
            url = 'http://bz.cfsa.net.cn/staticPages/{}.html'.format(code)
            # print(url)
            yield scrapy.Request(url, self.parse1)

    def parse1(self, response):
        iii = response.xpath('//span[@class="list_zt_top"]/i/text()').getall()
        IL = ItemLoader(item=FoodItem(), response=response)
        IL.add_value(field_name='title', value=iii[0])
        IL.add_value(field_name='eng_title', value=iii[1])
        IL.add_value(field_name='type', value=iii[2])
        IL.add_value(field_name='date', value=iii[3])
        IL.add_value(field_name='execute_date', value=iii[4])
        IL.add_value(field_name='lable', value=iii[5])
        IL.add_value(field_name='committee', value=iii[6])
        return IL.load_item()
