# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class WYItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title_wy = scrapy.Field()
    newsDigest = scrapy.Field()


class WRJItem(scrapy.Item):
    title_wrj = scrapy.Field()
    content = scrapy.Field()


class FoodItem(scrapy.Item):
    title = scrapy.Field()
    eng_title = scrapy.Field()
    type = scrapy.Field()
    date = scrapy.Field()
    execute_date = scrapy.Field()
    lable = scrapy.Field()
    committee = scrapy.Field()


class HuanQiuItem(scrapy.Item):
    hq_title = scrapy.Field()
    hq_publish_date = scrapy.Field()
    hq_author = scrapy.Field()
    hq_content = scrapy.Field()
    hq_image_url = scrapy.Field()
    hq_category = scrapy.Field()
    hq_language = scrapy.Field()
    hq_module = scrapy.Field()
    hq_html_content = scrapy.Field()
    hq_copyright = scrapy.Field()
    hq_site_name = scrapy.Field()
    hq_meta_data = scrapy.Field()
    hq_hash_code = scrapy.Field()
    hq_url = scrapy.Field()


class OfWeekItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()


class PeopleItem(scrapy.Item):
    title = scrapy.Field()


class NeteasyItem(scrapy.Item):
    title_wy = scrapy.Field()
    newsDigest = scrapy.Field()


class DoubleCreateItem(scrapy.Item):
    title = scrapy.Field()


class BaiduNewsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()


class GongwkItem(scrapy.Item):
    newstitle = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    readnumber = scrapy.Field()
    content = scrapy.Field()
    keywords = scrapy.Field()
