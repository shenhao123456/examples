#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 16:49
# @Author  : shenhao
# @File    : har_info.py
import logging
import os
import time

from browsermobproxy import Server
from selenium import webdriver
from threadpool import ThreadPool, makeRequests

cur_dir_path = os.path.abspath('.')
result_list = []

# 配置简单日志
log = logging.getLogger('genhar')
log.setLevel(logging.INFO)
LOG_FORMAT = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
file_handler = logging.FileHandler(os.path.join(cur_dir_path + '/genhar.log'))
# console_handler = logging.StreamHandler()
file_handler.setFormatter(LOG_FORMAT)
# console_handler.setFormatter(LOG_FORMAT)
log.addHandler(file_handler)


# 重写server 解决程序关闭后server关闭问题
class ProxyServer(Server):

    def __init__(self, path='browsermob-proxy', options=None):
        options = options if options is not None else {}

        self.path = path
        self.host = 'localhost'
        self.port = options.get('port', 8080)
        self.process = None
        self.command = []
        self.command += ["java", "-Dapp.name=browsermob-proxy",
                         "-Dbasedir=%s/browsermob-proxy-2.1.4" % cur_dir_path, "-jar",
                         "%s/browsermob-proxy-2.1.4/lib/browsermob-dist-2.1.4.jar" % cur_dir_path,
                         '--port=%s' % self.port]

    def get_process_pid(self):
        return self.process.pid


def generate_har_from_url(dri_path, url, proxy):
    result_har = ''
    profile = webdriver.FirefoxProfile()
    # 设置浏览器代理
    profile.set_proxy(proxy.selenium_proxy())
    options = webdriver.FirefoxOptions()
    # 设置无头模式
    # options.add_argument('-headless')
    driver = webdriver.Firefox(firefox_profile=profile,
                               executable_path=dri_path,
                               options=options)
    try:
        # 创建har对象
        proxy.new_har("generated_har")
        # selenium 访问目标地址
        driver.get(url)
        # 等待网络请求稳定,等待1s
        proxy.wait_for_traffic_to_stop(1000, 5000)
        # 获得har对象内容
        result_har = proxy.har
        # proxy.close()
        # driver.quit()
        result_list.append({"url": url, 'har': result_har})
    except Exception as e:
        log.error('访问%s异常:%s' % (url, e))
    finally:
        proxy.close()
        driver.quit()
    return {"url": url, 'har': result_har}


def main():
    path = cur_dir_path + "/browsermob-proxy-2.1.4/bin/browsermob-proxy.bat"
    dri_path = cur_dir_path + "/geckodriver.exe"
    # 待访问的地址列表
    url_list = ['https://news.163.com', 'https://www.baidu.com', 'https://www.sina.com',
                'https://news.163.com', 'https://www.baidu.com', 'https://www.sina.com',
                ]
    # url_list = ['http://www.baidu.com']
    # 创建代理服务，监听9090
    port_browsermob = 9090
    server = ProxyServer(path, options={'port': port_browsermob})
    # 启动代理
    server.start()
    try:
        # 采用多线程访问地址
        thread_count = 3
        args = [([dri_path, url, server.create_proxy()], None) for url in url_list]
        thread_pool = ThreadPool(thread_count)
        requests = makeRequests(generate_har_from_url, args)
        [thread_pool.putRequest(req) for req in requests]
        thread_pool.wait()
        # 防止内存泄漏
        thread_pool.dismissWorkers(thread_count, do_join=True)
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
        log.error(e)
