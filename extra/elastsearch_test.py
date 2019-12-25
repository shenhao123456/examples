#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 15:36
# @Author  : shenhao
# @File    : test
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

es = Elasticsearch([{'host': '30.207.39.18', 'port': 9200}], timeout=3600,)


def scan_query(index, body, size=10000):
    return scan(es, query=body, size=size, index=index)


def query(index, body, return_fields, size=10000):
    queryData = es.search(index=index, body=body, size=size, scroll='5m', filter_path=return_fields)
    scroll_id = queryData['_scroll_id']  # 获取scrollID
    total = queryData['hits']['total']
    mdata = queryData['hits']['hits']
    for i in range(divmod(total, size)[0] + 1):
        res = es.scroll(scroll_id=scroll_id, scroll='5m', filter_path=return_fields)
        if res and 'hits' in res["hits"]:
            mdata += res["hits"]["hits"]  # 扩展列表
    return mdata


if __name__ == '__main__':
    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "regexp": {
                            "host": "promethues_nod[a-z]+[0-9]*"
                        },
                        # "terms": {
                        #     "tags": [
                        #         'dnslog23013',
                        #         # "beats_input_codec_plain_applied"
                        #     ]
                        # }
                    },
                    {
                        "match": {
                            "_index": "113.215.230.13--2019.12.05"
                        }
                    },
                    {
                        "range": {
                            '@timestamp': {
                                "gt": "2019-12-05T05:16:00",  # 查询时间-8
                                "lt": "2019-12-05T05:16:10",
                            }
                        }
                    }
                ]
            }
        }
    }
    return_fields = [
        '_scroll_id',
        'hits.total',
        'hits.hits._source.message'
    ]
    index = "113.215.230.13--2019*"
    data = query(index, body, return_fields)
