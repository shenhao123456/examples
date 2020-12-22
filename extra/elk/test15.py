#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 15:36
# @Author  : shenhao
# @File    : test
import time

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

es = Elasticsearch([{"host": "30.207.39.18", "port": "9200"}], timeout=36000, )


def scan_query(index, body, size=10000):
    return scan(es, query=body, size=size, index=index)


def query(index, body, return_fields, size=1):
    st = time.time()
    queryData = es.search(index=index, body=body, size=size, scroll='5m')
    scroll_id = queryData['_scroll_id']  # 获取scrollID
    total = queryData['hits']['total']['value']
    print(total)
    # mdata = queryData['hits']['hits']
    # print(time.time() - st)
    # st = time.time()
    # print(len(mdata))
    # for i in range(divmod(total, size)[0] + 1):
    #     res = es.scroll(scroll_id=scroll_id, scroll='5m')
    #     if res and 'hits' in res["hits"]:
    #         mdata += res["hits"]["hits"]  # 扩展列表
    #         print(time.time() - st)
    #         print(len(mdata))
    #         st = time.time()
    # return mdata


if __name__ == '__main__':
    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "term": {
                            "domain.keyword": "www.jd.com",
                        },
                    },
                ],
            }
        },
        "aggs": {
            "group_by_covered": {
                "terms": {
                    "field": "covered",
                    "size": 10000
                },
            }
        }
    }
    return_fields = [
        '_scroll_id',
        'hits.total',
        'hits.hits._source.message'
    ]
    index = "dnslog_2020-07-15"
    stt = time.time()
    # data = query(index, body, return_fields)
    res = es.search(body=body, size=0, index=index)
    print(res['aggregations'])
    print(time.time() - stt)
    # print(list(set(data)))
    # print(time.time() - stt)
