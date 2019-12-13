#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : spider2.py
@Author: sh
@Date  : 2019/5/20
@Desc  :
"""
import scrapy
import logging

logger=logging.getLogger(__name__)

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['hao.360.com']
    start_urls = ['https://hao.360.com/?wd_xp1']

    #重定义start_url
    def start_requests(self):
        cookies='id=222; name=zhangsan'
        cookies={i.split('=')[0]:i.split('=')[1] for i in cookies.split('; ')}
        logger.warning(cookies)
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

        # yield scrapy.FormRequest(
        #     url='',
        #     formdata={
        #
        #     },
        #     callback=''
        # )



    def parse(self, response):
        # yield scrapy.FormRequest.from_response(
        #     response,
        #     # formid=
        #     # formname=
        #     formdata={
        #
        #     },
        #     callback=''
        # )
        item = {}
        yield item
