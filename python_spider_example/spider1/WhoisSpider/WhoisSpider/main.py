#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : main.py
@Author: sh
@Date  : 2019/3/29
@Desc  :
"""
from scrapy import cmdline

cmdline.execute('scrapy crawl whois_spider'.split())
