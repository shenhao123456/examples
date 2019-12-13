#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 15:36
# @Author  : shenhao
# @File    : ipy_test.py
from IPy import IP

print(IP('10.0.0.0/8').version())
print(IP('::1').version())

ip = IP("192.168.2.0/28")
print(ip.len())
# for i in ip:
#     print(i)

ip = IP("192.168.2.0")
print(ip.iptype())

IP("8.8.8.8").int()  # 转换成整型格式
IP('8.8.8.8').strHex()  # 转换成十六进制格式
IP('8.8.8.8').strBin()  # 转换成二进制格式
print(IP(0x8080808))  # 十六进制转成IP格式

print(IP('192.168.1.20').make_net('255.255.255.0'))  # 格式转换
print(IP('192.168.1.20/255.255.255.0', make_net=True))

IP('192.168.1.0/24').strNormal(0)  # 格式不同
IP('192.168.1.0/24').strNormal(1)
IP('192.168.1.0/24').strNormal(2)
IP('192.168.1.0/24').strNormal(3)

print(IP('10.0.0.0/24') < IP('12.0.0.0/24'))
print('192.168.1.100' in IP('192.168.1.0/24'))
print(IP('192.168.1.0/24') in IP('192.168.0.0/16'))

print(IP('192.168.0.0/23').overlaps('192.168.1.0/24'))  # 判断是否有重复网段1重叠，0不重叠

ip = IP("192.168.1.0/24")
##输出网络地址
print(ip.net())
# 输出网络掩码地址
print(ip.netmask())
##输出网络广播地址
print(ip.broadcast())
# 输出地址反向解析
print(ip.reverseNames()[0])
