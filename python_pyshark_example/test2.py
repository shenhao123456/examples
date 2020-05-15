#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 14:47
# @Author  : shenhao
# @File    : test2.py
import pyshark

display_filter = "http.request.method == \"GET\""
# display_filter = "udp"

# 打开存储的捕获文件
# cap = pyshark.FileCapture('抖音.pcapng', only_summaries=True, keep_packets=False, display_filter=display_filter)
cap = pyshark.FileCapture('抖音.pcapng', keep_packets=False, display_filter=display_filter)

i = 1
for item in cap:
    # if i == 2:
    #     break
    # print(dir(item))
    # print(item.highest_layer)  #应用层协议
    # print(item.transport_layer)  #传输层协议

    # print(dir(item.frame_info))
    # print(item.frame_info.protocols)

    # print(dir(item.eth))
    # print(item.eth.src)
    # print(item.eth.dst)

    # print(dir(item.ip))
    # print(item.ip.dst)
    # print(item.ip.src)
    # print(item.ip.ttl)
    # print(item.ip.version)
    #
    # print(dir(item.tcp))
    # print(item.tcp.srcport)
    # print(item.tcp.dstport)

    # print(dir(item.http))
    print(item.http.field_names)
    print(item.http.request_full_uri)

    # print(dir(item.data))
    # print(item.data.field_names)
    # print(item.data.data)
    # print(item.data.len)
    i += 1
