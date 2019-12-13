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
    proxies = {'HTTP': 'HTTP://' + get_ip().replace('\n', '')}
    try:
        r = requests.get('http://ju.taobao.com', headers=headers, proxies=proxies, timeout=10)
        print(r)
        if r.status_code == 200:
            return get_ip().replace('\n', '')
        else:
            checked_ip()
    except Exception as e:
        checked_ip()

if __name__ == '__main__':
    print(checked_ip())
