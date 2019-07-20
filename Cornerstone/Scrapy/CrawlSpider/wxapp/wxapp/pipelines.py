# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter, JsonItemExporter


class WxappPipeline(object):
    def __init__(self):
        self.fp = open('wxjc.json', 'wb')
        # 创建一个 JsonLinesItemExporter 对象，确保 ensure_ascii=False
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf8')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
