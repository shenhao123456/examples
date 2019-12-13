#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : ip_pool.py
@Author: sh
@Date  : 2019/5/21
@Desc  :
"""
import random

import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}


def get_ip():
    with open('ip_pool.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return random.choice(lines)

def checked_ip():
    proxies = {'HTTPS': 'HTTPS://' + get_ip().replace('\n', '')}
    try:
        # r = requests.get('http://httpbin.org/ip', headers=headers, proxies=proxies, timeout=10)
        r = requests.get('https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10001-1', headers=headers, proxies=proxies, timeout=10)
        if r.status_code == 200:
            return get_ip().replace('\n', '')
        else:
            checked_ip()
    except Exception as e:
        checked_ip()

if __name__ == '__main__':
    print(checked_ip())
