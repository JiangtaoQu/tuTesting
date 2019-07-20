# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from utils.server_mongodb import format_insert_many


class CrawlProjectsPipeline(object):
    def __init__(self):
        self.db = pymongo.MongoClient()['Crawl_Projects']

    def process_item(self, item, spider):
        # print(item._values)
        self.db[spider.collection].insert_many(format_insert_many(item._values))
        return item
