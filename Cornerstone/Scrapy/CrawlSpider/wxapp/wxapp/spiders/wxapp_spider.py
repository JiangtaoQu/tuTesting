# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['www.wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    # 规则
    rules = (
        Rule(LinkExtractor(allow=r'http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=\d+'),
             follow=True),
        # callback——回调函数
        # follow——是否需要跟进
        Rule(LinkExtractor(allow=r'http://www.wxapp-union.com/article-\d+-\d\.html'),
             callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title = response.xpath('//h1[@class="ph"]/text()').get()
        author_p = response.xpath('//p[@class="authors"]')
        author = author_p.xpath('.//a/text()').get()
        pub_time = author_p.xpath('.//span/text()').get()
        article_content = ''.join(response.xpath('//td[@id="article_content"]//text()').getall()).split()
        item = WxappItem()
        item['title'] = title
        item['author'] = author
        item['pub_time'] = pub_time
        item['article_content'] = article_content
        return item
