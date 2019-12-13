#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 14:03
# @Author  : shenhao
# @File    : genhar_chrome2.py
import os
import time

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import ProxyServer, get_log, max_count_of_proxy, Page

cur_dir_path = os.path.abspath('.')
result_list = []
log = get_log()


def generate_har_from_url(dri_path, url, proxy):
    result_har = ''
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=dri_path, chrome_options=chrome_options)
    try:
        proxy.new_har(url)
        # selenium 访问目标地址
        driver.get(url)
        proxy.wait_for_traffic_to_stop(500, 5000)
        # 获得har对象内容
        result_har = proxy.har
        print(len(result_har['log']['entries']))
        result_list.append({"url": url, 'har': result_har})
    except Exception as e:
        log.error('访问%s异常:%s' % (url, repr(e)))
    finally:
        proxy.close()
        driver.quit()
    return {"url": url, 'har': result_har}


def main():
    path = cur_dir_path + "/browsermob-proxy-2.1.4/bin/browsermob-proxy"
    dri_path = cur_dir_path + "/chromedriver"
    # 待访问的地址列表
    urls_list = [
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.baidu.com', 'http://www.youdao.com',
    ]
    # url_list = ['http://news.163.com']
    # url数量如果超过最大代理数，分批执行
    max_proxy = max_count_of_proxy()
    page = Page(1, len(urls_list), max_proxy)
    for i in range(page.total_page):
        page = Page(i + 1, len(urls_list), max_proxy)
        url_list = urls_list[page.start:page.end]
        # 创建代理服务，监听9090
        port_browsermob = 9090
        server = ProxyServer(path, options={'port': port_browsermob})
        # 启动代理
        server.start()
        try:
            # 启用虚拟GUI
            display = Display(visible=0, size=(800, 600))
            display.start()
            for url in url_list:
                generate_har_from_url(dri_path, url, server.create_proxy())
            display.stop()
        finally:
            # 关闭代理服务
            server.stop()


if __name__ == '__main__':
    try:
        start_time = time.time()
        main()
        end_time = time.time()
        log.info("用时" + str(end_time - start_time) + "秒")
        for i in result_list:
            log.info(i['url'] + ":  " + str((len(i['har']['log']['entries']))))
    except Exception as e:
        log.error(repr(e))
