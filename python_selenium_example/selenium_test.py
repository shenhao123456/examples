#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : selenium_test.py
@Author: sh
@Date  : 2019/5/24
@Desc  :
"""
from selenium import webdriver

# brochrome=webdriver.Chrome()

opt = webdriver.ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
# opt.add_argument('--headless')
opt.add_argument('--ignore-certificate-errors')
opt.add_argument('--disable-gpu')
# 创建chrome无界面对象
brochrome = webdriver.Chrome(options=opt)
brochrome.get('http://news.163.com/')


# brochrome.find_element_by_id('kw')
# brochrome.find_element_by_class_name('')
# a=brochrome.find_element_by_xpath('//*[@id="u1"]/a')

# input.send_keys("iPhone")
# button.click()
# browser.get_cookies()
# browser.add_cookie()
# print(a.get_property('name'))
# print(a.text)
# print(brochrome.page_source)
print((brochrome.page_source))

brochrome.quit() #关闭浏览器
# brochrome.close() #关闭最后一个页面
