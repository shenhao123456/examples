#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 13:25
# @Author  : shenhao
# @File    : whois_spider.py
import scrapy
import logging

from myspider1.items import WhoisItem

logger = logging.getLogger(__name__)


class TaobaoSpiderSpider(scrapy.Spider):
    name = 'whois_spider'
    allowed_domains = ['ip138.com']
    start_urls = ['https://site.ip138.com/youku.com/whois.htm']

    def parse(self, response):
        item = WhoisItem()
        news = response.xpath('//*[@id="whois"]/p')
        for box in news:
            item['registrar_whois_server'] = box.xpath('./text()').extract_first()
            # item['detail_url'] = box.xpath('./td[3]/a/@href').extract_first()
            # logger.warning(item['detail_url'])
            yield item
