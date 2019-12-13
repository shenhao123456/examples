#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : spider1.py
@Author: sh
@Date  : 2019/5/20
@Desc  :
"""
# import scrapy
# import logging
#
# from myspider1.items import TaobaoItem
#
# logger=logging.getLogger(__name__)
#
#
# class TaobaoSpiderSpider(scrapy.Spider):
#     name = 'taobao_spider'
#     allowed_domains = ['wz.sun0769.com']
#     start_urls = ['http://d.wz.sun0769.com/index.php/question/huiyin']
#
#     def parse(self, response):
#         item = TaobaoItem()
#         news = response.xpath('/html/body/div[10]/table[2]/tr')
#         for box in news:
#             item['title']=box.xpath('./td[3]/a/text()').extract_first()
#             item['detail_url']=box.xpath('./td[3]/a/@href').extract_first()
#             # logger.warning(item['detail_url'])
#
#             # url=item['detail_url']
#             # logger.warning(item['detail_url'])
#             yield  scrapy.Request(item['detail_url'],callback=self.parse_detail,meta={'data':item})
#
#         # next_url= response.xpath("//a[text()='>']/@href").extract_first()
#         # # logger.warning(next_url)
#         # if next_url is not None:
#         #     yield scrapy.Request(next_url, callback=self.parse)
#
#
#     def parse_detail(self, response):
#         item=response.meta['data']
#         item['content'] =response.xpath('/html/body/div[9]/table[2]/tr[1]/td[1]/text()').extract()
#         item['image_url'] =response.xpath('/html/body/div[9]/table[2]/tr[1]/td[1]//img/@src').extract()
#         item['image_url']=["wz.sun0769.com"+i for i in item['image_url']]
#         # logger.warning(item['image_url'])
#         yield item
