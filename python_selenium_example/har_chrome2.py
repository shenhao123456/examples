#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 14:29
# @Author  : shenhao
# @File    : har_chrome2.py
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from har_firefox import ProxyServer, log

cur_dir_path = os.path.abspath('.')
result_list = []


def generate_har_from_url(dri_path, url, proxy):
    result_har = ''
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=dri_path, chrome_options=chrome_options)
    try:
        proxy.new_har(url)
        # 访问目标地址
        driver.get(url)
        # 等待网页资源访问结束
        proxy.wait_for_traffic_to_stop(500, 5000)
        # 生成har文件
        result_har = proxy.har
        # print({"url": url, 'har': result_har})
        result_list.append({"url": url, 'har': result_har})
    except Exception as e:
        log.error('访问%s异常:%s' % (url, e))
    finally:
        proxy.close()
        driver.quit()
    return {"url": url, 'har': result_har}


def main():
    path = cur_dir_path + "/browsermob-proxy-2.1.4/bin/browsermob-proxy.bat"
    dri_path = cur_dir_path + "/chromedriver.exe"
    # 待访问的地址列表
    url_list = [
        'http://news.163.com', 'http://www.youdao.com',
        'http://news.163.com', 'http://www.youdao.com',
    ]
    # base_url = 'http://news.163.com'
    # 创建代理服务，监听9090
    port_browsermob = 9090
    server = ProxyServer(path, options={'port': port_browsermob})
    # 启动代理
    server.start()
    try:
        for url in url_list:
            generate_har_from_url(dri_path, url, server.create_proxy())
    finally:
        # 关闭代理服务
        server.stop()


if __name__ == '__main__':
    main()
    for res in result_list:
        print(res['url'] + " --- " + str(len(res['har']['log']['entries'])))
        for entry in res['har']['log']['entries']:
            print(entry['request']['url'] + ' === ' + str(entry['time']) + "ms")
