#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 15:50
# @Author  : shenhao
# @File    : dnspython.py

import dns.resolver

# my_resolver=dns.resolver.Resolver()
# # 这里换成你指定的某一个域名服务器的ip
# my_resolver.nameservers=['8.8.8.8']

domain = 'www.baidu.com'  # 输入域名地址
A = dns.resolver.query(domain, 'A')  # 指定查询记录为A型
for i in A.response.answer:  # 通过response.answer方法获取查询回应信息
    print(i)
    for j in i.items:
        print(j)

domain = '694691295@qq.com'
MX = dns.resolver.query(domain, 'MX')  # 指定解析类型为MX记录
for i in MX:  # 遍历回应结果
    print('MX preference =', i.preference, 'mail exchanger =', i.exchange)

domain = 'baidu.com'
NS = dns.resolver.query(domain, 'NS')
for i in NS.response.answer:
    print(i)
    for j in i.items:
        print(j.to_text())

domain = 'www.baidu.com'
CNAME = dns.resolver.query(domain, 'CNAME')
for i in CNAME.response.answer:
    for j in i.items:
        print(j.to_text())
