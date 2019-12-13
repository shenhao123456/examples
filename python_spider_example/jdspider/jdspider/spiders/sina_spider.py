#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : sina_spider.py
@Author: sh
@Date  : 2019/5/22
@Desc  :
"""
import json
import re

import scrapy
from scrapy_redis.spiders import RedisSpider

from jdspider.items import NewsItem
import logging

logger = logging.getLogger(__name__)


"""
https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4&page=1&encode=utf-8&callback=feedCardJsonpCallback
"""

class SinaSpider(RedisSpider):
    name = 'sina_spider'
    redis_key = 'sina_spider:start_urls'
    allowed_domains = ['sina.com']


    def parse(self, response):
        # item=NewsItem()
        logger.warning(response.body)
        data=json.loads(response.body)
        # item.title=
        # for box in news_list:
        #     item.title=box.xpath('./h2/a/text()').extract_first()
        #     logger.warning(item.title)
        #     item.pre_title=box.xpath('./div[1]/div/a[1]/text()').extract_first()
        #     logger.warning(item.pre_title)
        #     url=box.xpath('./h2/a/@href').extract_first()
        #     logger.warning(url)
            # yield scrapy.Request(
            #     url=url,
            #     callback=self.parse_detail,
            #     meta={'data':item}
            # )

    def parse_detail(self,response):
        item=response.meta['data']





