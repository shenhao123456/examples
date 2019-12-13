#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 13:25
# @Author  : shenhao
# @File    : whois_spider.py
import re

import scrapy
import logging

logger = logging.getLogger(__name__)

filename = '省网-联通混合CDN 20190906.txt'


def get_domain_list(filename):
    with open(filename, 'r') as file:
        data = file.read()
        domain_list = re.findall(r'"(.*?)"', data)
        new_domain_list = []
        for domain in domain_list:
            while domain.split('.')[-1] == '':
                domain = '.'.join(domain.split('.')[:len(domain.split('.')) - 1])
            top_domain = domain.split('.')[-2] + '.' + domain.split('.')[-1]
            new_domain_list.append(top_domain)
        domain_list = list(set(new_domain_list))
        return domain_list


class TaobaoSpiderSpider(scrapy.Spider):
    name = 'whois_spider'
    allowed_domains = ['chinaz.com']
    domain_list = get_domain_list(filename)
    start_urls = ['https://whois.chinaz.com/' + domain for domain in domain_list]

    # start_urls = ['https://whois.chinaz.com/qq.com']

    def parse(self, response):
        item = {}
        item['domain'] = response.url
        item['domain_status'] = []
        item['name_server'] = []
        box = response.xpath('//*[@id="detail_info"]').extract_first().split('<br>')
        for text in box:
            text = text.strip()
            # print(text.split(':'))
            if text.split(':')[0] == 'Registry Domain ID':
                item['registry_domain_id'] = ':'.join(text.split(':')[1:]).strip()
            elif text.split(':')[0] == 'Registrar WHOIS Server':
                item['registrar_whois_server'] = ':'.join(text.split(':')[1:]).strip()
            elif text.split(':')[0] == 'Registrar URL':
                item['registrar_url'] = ":".join(text.split(':')[1:])
            elif text.split(':')[0] == 'Updated Date':
                item['updated_date'] = ':'.join(text.split(':')[1:]).strip()
            elif text.split(':')[0] == 'Creation Date':
                item['creation_date'] = ':'.join(text.split(':')[1:]).strip()
            elif text.split(':')[0] == 'Registry Expiry Date':
                item['registry_expiry_date'] = ':'.join(text.split(':')[1:]).strip()
            elif text.split(':')[0] == 'Registrar':
                item['registrar'] = ':'.join(text.split(':')[1:]).strip()
            elif text.split(':')[0] == 'Registrar IANA ID':
                item['egistrar_iana_id'] = ':'.join(text.split(':')[1:]).strip()
            elif text.split(':')[0] == 'Registrar Abuse Contact Email':
                item['registrar_abuse_contact_email'] = ':'.join(text.split(':')[1:]).strip()
            elif text.split(':')[0] == 'Registrar Abuse Contact Phone':
                item['registrar_abuse_contact_phone'] = ':'.join(text.split(':')[1:]).strip()
            elif text.split(':')[0] == 'Domain Status':
                item['domain_status'].append(':'.join(text.split(':')[1:]).strip())
            elif text.split(':')[0] == 'Name Server':
                item['name_server'].append(':'.join(text.split(':')[1:]).strip())
            elif text.split(':')[0] == 'DNSSEC':
                item['dnssec'] = ':'.join(text.split(':')[1:]).strip()

        # item['domain'] = str(response.xpath('//*[@id="sh_info"]/li[1]/div[2]/p[1]/a[1]/text()').extract_first()).strip()
        # item['registrar'] = str(
        #     response.xpath('//*[@id="sh_info"]/li[2]/div[2]/div/span/text()').extract_first()).strip()
        # item['email'] = str(response.xpath('//*[@id="sh_info"]/li[3]/div[2]/span/text()').extract_first()).strip()
        # item['phone'] = str(response.xpath('//*[@id="sh_info"]/li[4]/div[2]/span/text()').extract_first()).strip()
        # item['create_time'] = str(response.xpath('//*[@id="sh_info"]/li[5]/div[2]/span/text()').extract_first()).strip()
        # item['expire_time'] = str(response.xpath('//*[@id="sh_info"]/li[6]/div[2]/span/text()').extract_first()).strip()
        # item['dns'] = str(response.xpath('//*[@id="sh_info"]/li[7]/div[2]/span/text()').extract_first()).strip()
        # # item['dns_server'] = [box.extract().strip() for box in response.xpath('//*[@id="sh_info"]/li[8]/div[2]/text()')]
        yield item
