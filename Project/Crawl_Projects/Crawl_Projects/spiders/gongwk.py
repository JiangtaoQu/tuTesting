# -*- coding: utf-8 -*-
# @Time : 2019/7/17 14:54
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : gongwk.py
# @Software: PyCharm
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from newspaper import Article
from ..items import GongwkItem
from scrapy.loader import ItemLoader


class GongwkSpider(CrawlSpider):
    name = 'gongwk'
    collection = 'news'
    # allowed_domains = ['www.test.com']
    kw = '经济'
    start_urls = ['https://www.gongwk.com/article.jhtml?tdsourcetag=s_pctim_aiomsg']

    rules = (
        Rule(LinkExtractor(allow=(r'https://www\.gongwk\.com/articles/c-[\d]{2}\.jhtml',),
                           restrict_xpaths='//h4/a[contains(text(),"{}")]'.format(kw)), follow=True),
        Rule(LinkExtractor(allow=(r'https://www\.gongwk\.com/article/[\d]{6}\.jhtml',)), follow=True,
             callback='parse_detail')
    )

    def parse_detail(self, response):
        # print(response.url)
        # 新闻标题
        newstitle = response.xpath('//h2/text()').get('暂无')
        # 日期
        date = response.xpath('//p[@class="artinfo"]/text()').re(
            r'[\d]{4}-[\d]{1,2}-[\d]{1,2} [\d]{1,2}:[\d]{1,2}:[\d]{1,2}')
        date = date[0] if date != [] else '暂无'
        # 作者
        author = response.xpath('//span[@class="author"]/a/@title').get('暂无')
        # 阅读量
        readnumber = response.xpath('//p[@class="artinfo"]/text()').re(
            r'阅读: ([\d]*)')
        readnumber = readnumber[0] if readnumber != [] else '暂无'
        # 正文
        language = 'zh'
        news = Article(url=response.url, language=language)
        news.download()
        news.parse()
        content = news.text
        # 关键词
        keywords = response.xpath('//div[contains(@class, "keywords")]/a/text()').getall()
        # 存库
        IL = ItemLoader(item=GongwkItem(), response=response)
        IL.add_value(field_name='newstitle', value=newstitle, )
        IL.add_value(field_name='date', value=date, )
        IL.add_value(field_name='author', value=author, )
        IL.add_value(field_name='readnumber', value=readnumber, )
        IL.add_value(field_name='content', value=content, )
        IL.add_value(field_name='keywords', value=keywords, )
        yield IL.load_item()

















