# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import re
import requests

logger = logging.getLogger(__name__)

header = {
    'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    # 'Cookie': 'b963ef2d97e050aaf90fd5fab8e78633',
    # 需要查看图片的cookie信息，否则下载的图片无法查看
}


class Myspider1Pipeline(object):
    # def __init__(self):
    # self.connection = pymongo.MongoClient(settings.MONHOST, settings.MONPORT)
    # db = self.connection[settings.MONDB]
    # self.collection = db[settings.COLLECTION]
    def process_item(self, item, spider):
        print(item)
        # if spider.name == 'taobao_spider':
        #     logger.warning(item)
        #     # self.connection.insert(dict(item))
        #     # self.collection.insert_one(dict(item))
        #     for url in item['img_urls']:
        #         res = requests.get("https:" + url)
        #         with open('images/' + url.split('/')[-1], 'wb') as f:
        #             f.write(res.content)
        return item

    def open_spider(self, spider):  # 只执行一次
        pass

    def close_spider(self, spider):
        pass


class IpSpiserPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'ip_spider':
            with open('ip_pool.txt', 'a', encoding='utf-8') as f:
                f.writelines(item['ip'] + '\n')
            # logger.warning(item)
        return item
