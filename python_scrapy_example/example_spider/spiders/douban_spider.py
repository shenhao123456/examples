# -*- coding: utf-8 -*-
import scrapy
from python_scrapy_example.example_spider.items import ExampleSpiderItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = ExampleSpiderItem()
        # print(response.text)
        movie_list=response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for box in movie_list:

            item['serial_number']=box.xpath('.//em/text()').extract()[0]
            item['movie_name']=box.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            # print(item['serial_number'])
            # print(item['movie_name'])
            yield item

        url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract()

        if url:
            page = 'https://movie.douban.com/top250' + url[0]
            yield scrapy.Request(page, callback=self.parse)
            # 返回url

