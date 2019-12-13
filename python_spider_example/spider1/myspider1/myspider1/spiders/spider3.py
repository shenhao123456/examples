# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Spider3Spider(CrawlSpider):
    name = 'spider3'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/']


    #定义提取url规则
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item'), #还有其他参数，正则匹配当前页所有url  follow表示是否循环匹配
        Rule(LinkExtractor(allow=r'Items/'), follow=True),   #循环执行
        # Rule(LinkExtractor(restrict_xpaths=r'//div'), follow=True),   #查找符合区域的所有url
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
