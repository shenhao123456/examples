# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JdspiderPipeline(object):
    def process_item(self, item, spider):
        # if len(item['name'].split()) > 0:
        #     item['name'] = item['name'].split()[0]
        # print(item)
        return item


class SinaPipeline(object):
    def process_item(self, item, spider):
        if spider.name=='sina_spider2':
            print(item)
            return item
