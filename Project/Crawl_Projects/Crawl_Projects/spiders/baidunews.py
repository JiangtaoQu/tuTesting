# -*- coding: utf-8 -*-
# @Time : 2019/7/11 19:40
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : baidunews.py
# @Software: PyCharm
import scrapy
from ..items import BaiduNewsItem
from scrapy.loader import ItemLoader


class BaiduNewsSpider(scrapy.Spider):
    name = 'baidunews'
    collection = 'news'
    # allowed_domains = ['www.test.com']
    keyword = '%E6%97%A0%E4%BA%BA%E6%9C%BA'
    start_urls = [
        'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=' + keyword + '&x_bfe_rqs=03E80&x_bfe_tjscore=0.016743&tngroupname=organic_news&pn=0']

    # print(start_urls)

    def parse(self, response):
        # print(response.url)
        # print(response.text)
        domains = 'https://www.baidu.com/s?'
        next_page = domains + response.xpath('//p[@id="page"]//a[contains(text(),"下一页")]/@href').get('无')
        # print(next_page)
        hrefs = response.xpath('//h3[@class="c-title"]/a/@href').getall()
        # for href in hrefs:
            # print(href)
        h3 = response.xpath('//h3[@class="c-title"]')
        title_list = []
        for h in h3:
            title = h.xpath('string(.//a)').get('暂无').strip()
            title_list.append(title)
        # print(title_list)
        IL = ItemLoader(item=BaiduNewsItem(), response=response)
        # for title, url in zip(hrefs, h3):
        #     url = url.xpath('string(.//a)').get().strip()
        #     print(title, url, sep='\n')
        IL.add_value(field_name='title', value=title_list)
        IL.add_value(field_name='url', value=hrefs)
        IL.load_item()
        yield scrapy.Request(next_page, callback=self.parse, dont_filter=True, )
