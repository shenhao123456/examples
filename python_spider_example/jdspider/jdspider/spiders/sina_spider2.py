#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : sina_spider2.py
@Author: sh
@Date  : 2019/5/22
@Desc  :
"""
import json
import re

import scrapy
import logging

from jdspider.items import NewsItem

logger = logging.getLogger(__name__)

class SinaSpider2(scrapy.Spider):
    name = 'sina_spider2'
    allowed_domains = ['feed.sina.com.cn']
    start_urls = ['https://feed.sina.com.cn/api/roll/get?'
                  'pageid=121&lid=1356&num=20&versionNumber=1.2.4&page=1&encode=utf-8&'
                  'callback=feedCardJsonpCallback']


    def parse(self, response):
        item=NewsItem()
        data=response.body.decode()
        n=len(data)
        data=data[26:n-14]
        data=json.loads(data)
        if len(data['result']['data'])>0:
            for new in data['result']['data']:
                # logger.warning(new)
                item['title']=new['title']
                item['pre_title']=new['intro']
                yield item

            url=response.url
            page_num = re.search('page=\d+', url).group()[5:]
            next_num=int(page_num)+1
            url2=re.sub(r'page=\d+','page=%d'%next_num,url)
            # logger.warning(url)
            yield scrapy.Request(
                url=url2,
                callback=self.parse
            )
