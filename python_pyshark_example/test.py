#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 13:55
# @Author  : shenhao
# @File    : test.py
import pyshark

# display_filter = "http.response.code==200"
display_filter = "udp"
# cap = pyshark.LiveCapture(interface='WLAN')
# 打开存储的捕获文件
cap = pyshark.FileCapture('抖音.pcapng', only_summaries=True, keep_packets=False, display_filter=display_filter)

# cap.load_packets(timeout=5)


details = {
    'stats': {
        'breakdown': {},
        'length_buckets': {'0-200': 0, '201-450': 0, '451-800': 0, '801-1200': 0, '1201-1500': 0}
    },
    'packets': [],
    # 'linechart': []
}

avg_length = []


def decode_packet(packet):
    pkt_details = {
        'number': packet.no,
        'length': packet.length,
        'time': packet.time
    }
    pkt_details['src_ip'] = packet.source
    pkt_details['dst_ip'] = packet.destination
    pkt_details['protocol'] = packet.protocol
    pkt_details['desc'] = packet.info

    # delta and stream aren't supported by earlier versions (1.99.1) of tshark
    try:
        pkt_details['delta'] = packet.delta
        pkt_details['stream'] = packet.stream
    except AttributeError:
        pass

    details['packets'].append(pkt_details)
    avg_length.append(int(packet.length))

    if 0 <= int(packet.length) <= 200:
        details['stats']['length_buckets']['0-200'] += 1
    elif 201 <= int(packet.length) <= 450:
        details['stats']['length_buckets']['201-450'] += 1
    elif 451 <= int(packet.length) <= 800:
        details['stats']['length_buckets']['451-800'] += 1
    elif 801 <= int(packet.length) <= 1200:
        details['stats']['length_buckets']['801-1200'] += 1
    elif 1201 <= int(packet.length):
        details['stats']['length_buckets']['1201-1500'] += 1

    try:
        details['stats']['breakdown'][packet.protocol] += 1
    except KeyError:
        details['stats']['breakdown'][packet.protocol] = 1


try:
    cap.apply_on_packets(decode_packet, timeout=600)
except:
    print('Capture File is too large, please try downloading and analyzing locally.')

details['stats']['avg_length'] = sum(avg_length) / len(avg_length)

print(details)
