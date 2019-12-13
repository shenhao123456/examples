#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : ip_spider.py
@Author: sh
@Date  : 2019/5/21
@Desc  :
"""
import logging

import scrapy

from myspider1.items import IpInfoItem

logger = logging.getLogger(__name__)


class IpSpider(scrapy.Spider):
    name = 'ip_spider'
    allowed_domains = ['xicidaili.com']
    # start_urls = ['http://www.xicidaili.com/wt/']
    start_urls = []
    # 爬取5页网站的IP
    for i in range(1, 6):
        start_urls.append('http://www.xicidaili.com/wt/' + str(i))

    def parse(self, response):
        item = IpInfoItem()
        for sel in response.xpath('//*[@id="ip_list"]//tr'):
            ip = sel.xpath('.//td[2]/text()').extract_first()
            port = sel.xpath('.//td[3]/text()').extract_first()
            if ip:
                item['ip'] = str(ip) + ":" + str(port)
                yield item
