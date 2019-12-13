# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WhoisItem(scrapy.Item):
    registrar_whois_server = scrapy.Field()
    registry_domain_id = scrapy.Field()
    domain_name = scrapy.Field()
    registrar_url = scrapy.Field()
    updated_date = scrapy.Field()
    creation_date = scrapy.Field()
    registry_expiry_date = scrapy.Field()
    registrar = scrapy.Field()
    registrar_iana_id = scrapy.Field()
    registrar_abuse_contact_email = scrapy.Field()
    registrar_abuse_contact_phone = scrapy.Field()
    domain_status = scrapy.Field()
    name_server = scrapy.Field()
    dnssec = scrapy.Field()
