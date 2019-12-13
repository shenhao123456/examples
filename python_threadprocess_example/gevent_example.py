#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 10:23
# @Author  : shenhao
# @File    : gevent_example.py
from gevent import monkey

monkey.patch_all()
import gevent
import requests
import time


def get_page(url):
    print('GET: %s' % url)
    response = requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' % (len(response.text), url))


start_time = time.time()
gevent.joinall([
    gevent.spawn(get_page, 'https://www.baidu.com/'),
    gevent.spawn(get_page, 'https://www.youdao.com/'),
    gevent.spawn(get_page, 'https://www.sina.com/'),
])
stop_time = time.time()
print('run time is %s' % (stop_time - start_time))
