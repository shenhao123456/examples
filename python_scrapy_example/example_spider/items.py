# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    serial_number = scrapy.Field()
    movie_name = scrapy.Field()

