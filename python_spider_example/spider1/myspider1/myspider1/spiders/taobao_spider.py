#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : taobao_spider.py
@Author: sh
@Date  : 2019/5/29
@Desc  :
"""
import re
import json

import scrapy
from scrapy_redis.spiders import RedisSpider


class TaoBaoSpider(RedisSpider):
    name = 'taobao_spider'
    redis_key = 'taobao_spider:start_urls'  # 先重redis中找到这个建  然后获取url    读取是pop操作实现一次操作
    allowed_domains = ['ju.taobao.com']
    """
    http://ju.taobao.com/?page=1
    """

    def parse(self, response):
        # nodes=response.xpath('//*[@id="juList"]/text()').extract()
        # print(response.text)
        a = re.findall('juListData = .*;', response.text)
        data = json.loads(a[0][13:len(a[0]) - 1])
        if data != {}:
            item = {}
            for box in data['itemList']:
                item['tqgDetailUrl'] = box['extend']['tqgDetailUrl']
                item['info'] = box['extend']['thirdSellPointInfos'][0]
                item['title'] = box['name']['title']
                item['price'] = box['price']['actPrice']
                # print(item)
                yield scrapy.Request(
                    url='https:' + item['tqgDetailUrl'],
                    callback=self.detail_parse,
                    meta={'data': item}
                )
            # num = re.findall('page=\d+', response.url)[0]
            # num = int(num[5:]) + 1
            # next_url = 'http://ju.taobao.com/?page=' + str(num)
            # yield scrapy.Request(
            #     url=next_url,
            #     callback=self.parse,
            #     dont_filter=True
            # )

    def detail_parse(self, response):
        item = response.meta['data']
        img_urls = response.xpath('//*[@id="page"]/div[3]/div/div[2]/div[1]/div/ul/li')
        item['img_urls'] = [i.xpath('//img/@src').extract_first() for i in img_urls]
        yield item
