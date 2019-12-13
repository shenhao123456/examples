# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()



class IpInfoItem(scrapy.Item):
    ip=scrapy.Field()


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    pre_title = scrapy.Field()
    article_text=scrapy.Field()
    article_images=scrapy.Field()
