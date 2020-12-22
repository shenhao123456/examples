import json
import time

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

es = Elasticsearch([{"host": "30.207.39.18", "port": "9200"}], timeout=36000, )


def scan_query(index, body, size=10000):
    return scan(es, query=body, size=size, index=index, scroll='5m')


query_index = "dnslog_2020-07-26"

body = {
    "query": {
        "bool": {
            "must": [
                {
                    "term": {
                        "cname.keyword": "s.autoimg.cn.w.kunlunca.com"
                    }
                },
                {
                    "term": {
                        "covered": "2"
                    }
                }
            ],
        }
    }
}

body2 = {
    "query": {
        "match_all": {}
    }
}

if __name__ == '__main__':
    st1 = time.time()
    data_list = []
    # data = es.search(index=query_index, body=body, size=0)
    # print(data)
    # print(data['aggregations']['group_by_clientip']['buckets'])
    # print(time.time() - st1)
    # print(len(data['aggregations']['group_by_clientip']['buckets']))
    data = scan_query(body=body, index=query_index)
    # data = scan_query(body=body, index=query_index)
    # data_list = [(item['_source']['clientip'], item['_source']['ip_list']) for item in data]
    count = 0
    with open('域名解析失败数据.txt', 'w+') as f:
        for item in data:
            count += 1
            # print(count, item['_source'])
            obj = item['_source']
            print('源地址:%s ,cname:%s,a记录:%s' % (obj['clientip'], obj['cname'], obj['ip_list']))
            f.write('源地址:%s ,cname:%s,a记录:%s\n' % (obj['clientip'], obj['cname'], obj['ip_list']))

    #     ip_list = sorted(json.loads(item['_source']['ip_list'].replace("'", "\"")))
    #     print(count, ip_list)
    #     data_list.append((item['_source']['clientip'], tuple(ip_list)))
    #     # if count == 40000:
    #     #     break
    # print(len(list(set((data_list)))))
