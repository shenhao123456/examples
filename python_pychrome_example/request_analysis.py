#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 19:18
# @Author  : shenhao
# @File    : request_analysis.py
import time

import pychrome


class NetworkAPIImplemention(object):
    def __init__(self, browser, url):
        self.request_dict = {}
        self.response_dict = {}
        self.finish_dict = {}
        self.error_dict = {}
        self.browser = browser
        self.url = url
        # 创建tab对象并配置事件监听函数
        self.tab = self.browser.new_tab()
        self.tab.Network.requestWillBeSent = self.request_will_be_sent
        self.tab.Network.responseReceived = self.response_received
        self.tab.Network.loadingFinished = self.loading_finished
        self.tab.Network.loadingFailed = self.loading_failed
        self.tab.Page.loadEventFired = self.loaded

    # 请求开始回调
    def request_will_be_sent(self, **kwargs):
        self.request_dict[kwargs.get('requestId')] = kwargs

    # 响应加载结束回调
    def loading_finished(self, **kwargs):
        self.finish_dict[kwargs.get('requestId')] = kwargs

    # 开始接收响应
    def response_received(self, **kwargs):
        self.response_dict[kwargs.get('requestId')] = kwargs

    # 响应加载失败回调
    def loading_failed(self, **kwargs):
        self.error_dict[kwargs.get('requestId')] = kwargs

    # 页面加载完成回调
    def loaded(self, **kwargs):
        # print(kwargs)
        time.sleep(0.5)
        self.tab.stop()
        self.browser.close_tab(self.tab)

    # 请求资源
    def navigate_page(self):
        self.tab.start()
        self.tab.Network.enable()
        self.tab.Page.enable()
        # 是否禁用缓存
        self.tab.Network.setCacheDisabled(cacheDisabled=True)
        # 请求目标地址
        self.tab.Page.navigate(url=self.url)
        # 等待页面加载
        self.tab.wait()


def main():
    url_list = ['https://news.163.com/', 'https://www.baidu.com/']
    browser = pychrome.Browser(url="http://127.0.0.1:9222")
    for url in url_list:
        try:
            network_api = NetworkAPIImplemention(browser, url)
            network_api.navigate_page()
            # 获取的所有请求详细信息
            print(url + ":" + str(len(network_api.request_dict.keys())))
            for key in list(network_api.request_dict.keys()):
                print('请求url：' + network_api.request_dict[key]['request']['url'])
                if key in network_api.response_dict.keys():
                    print("返回内容：" + str(network_api.response_dict[key]['response']))
                else:
                    print("返回内容：无返回内容")

                if key in network_api.finish_dict.keys():
                    print("耗时：%f ms"
                          % (network_api.finish_dict[key]['timestamp'] - network_api.request_dict[key]['timestamp']))
                elif key in network_api.error_dict.keys():
                    print("该请求加载失败")
                else:
                    print('该请求没有得到响应')
                print("====================================================")
        except Exception as e:
            print(repr(e))


if __name__ == '__main__':
    main()
