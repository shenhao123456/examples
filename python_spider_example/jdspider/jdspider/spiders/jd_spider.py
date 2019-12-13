#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : jd_spider.py
@Author: sh
@Date  : 2019/5/21
@Desc  :
"""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider


class JDSpider(RedisCrawlSpider):
    name = 'jd_spider'
    allowed_domains = ['jd.com']
    redis_key = 'jingdong'
    # start_urls = ['https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10001-1']

    # 定义提取url规则
    rules = (
        Rule(LinkExtractor(allow=r'//book\.jd\.com/booktop/1713-0-0-0-10001-\d+\.html#comfort'), follow=True),
        # 还有其他参数，正则匹配当前页所有url  follow表示是否循环匹配
        Rule(LinkExtractor(allow=r'//item\.jd\.com/\d+\.html'), callback='parse_item'),  # 循环执行
    )

    def parse_item(self, response):
        item = {}
        item['name'] = response.xpath('//div[@id="name"]/div[1]/text()').extract_first()
        item['images_url'] = [i.xpath('./img/@src').extract_first()
                              for i in response.xpath('//*[@id="spec-list"]/div/ul/li')]
        # item['description'] = response.xpath('//div[@id="description"]').get()
        yield item
