#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : redis_spider.py
@Author: sh
@Date  : 2019/5/21
@Desc  :
"""
# from scrapy_redis.spiders import RedisSpider


# class IpSpider(RedisSpider):
#     name = 'redis_spider'
#     redis_key = 'redis_spider:start_urls'  #先重redis中找到这个建  然后获取url    读取是pop操作实现一次操作
#     allowed_domains = ['xicidaili.com']
#     # start_urls = ['http://www.xicidaili.com/wt/']
#     #lpush redis_spider:start_urls url   redis_spider:start_urls 是一个列表
#
#     # def __init__(self,*args,**kwargs):
#
#
#
#     def parse(self, response):
#         pass
