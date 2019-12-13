# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    content = scrapy.Field()
    image_url = scrapy.Field()
    detail_url = scrapy.Field()


class IpInfoItem(scrapy.Item):
    ip = scrapy.Field()


class WhoisItem(scrapy.Item):
    registrar_whois_server = scrapy.Field()
