import json
import time

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

es = Elasticsearch([{"host": "30.207.39.18", "port": "9200"}], timeout=36000, )


def scan_query(index, body, size=10000):
    return scan(es, query=body, size=size, index=index, scroll='5m')


def query(index, body, size=10000):
    queryData = es.search(index=index, body=body, size=size, scroll='5m')
    # scroll_id = queryData['_scroll_id']  # 获取scrollID
    total = queryData['hits']['total']['value']
    print(total)


query_index = "dnslog_2020-08-03"

body = {
    "query": {
        "bool": {
            "must": [
                {
                    "term": {
                        "domain.keyword": 'www.jd.com'
                    }
                }
            ],
            "must_not": [
                {
                    "term": {
                        'covered': 2
                    }
                }
            ]
        }
    },
}


body2 = {
    "query": {
        "bool": {
            "must": [
                {
                    "term": {
                        "view.keyword": 'LJWL'
                    }
                },
                {
                    "term": {
                        "ip_list": '113.215.12.3'
                    }
                }
            ],
        }
    },
}

body3 = {
    "query": {
        "bool": {
            "must": [
                # {
                #     "prefix": {
                #         "clientip.keyword": '103.30.97'
                #     }
                # },
                {
                    "term": {
                        "view.keyword": 'LJWL'
                    }
                },
                {
                    "term": {
                        "ip_list": '113.215.12.5'
                    }
                }
            ],
        }
    },
}

if __name__ == '__main__':
    st1 = time.time()
    # data_list = []
    # data = es.search(index=query_index, body=body, size=0)
    # print(data)
    # print(data['aggregations']['group_by_clientip']['buckets'])
    # print(len(data['aggregations']['group_by_clientip']['buckets']))
    data = scan_query(body=body2, index=query_index)
    domain_list = []
    cname_list = []
    count = 0
    for item in data:
        count += 1
        domain_list.append(item['_source']['domain'])
        cname_list.append(item['_source']['cname'])
        # data_list1.append(item)
        print(count, item)
        # if count == 10000:
        #     break
    count = 0
    data = scan_query(body=body3, index=query_index)
    for item in data:
        count += 1
        domain_list.append(item['_source']['domain'])
        cname_list.append(item['_source']['cname'])
        # data_list1.append(item)
        print(count, item)
    domain_list = list(set(domain_list))  # 去重
    cname_list = list(set(cname_list))  # 去重
    with open('result2.txt', 'w+') as f:
        f.write('域名：\n')
        for domain in domain_list:
            f.write(domain + '\n')
        f.write('cname：\n')
        for cname in cname_list:
            f.write(cname + '\n')

    # print(data_list[0])
    #     ip_list = sorted(json.loads(item['_source']['ip_list'].replace("'", "\"")))
    #     print(count, ip_list)
    #     data_list.append((item['_source']['clientip'], tuple(ip_list)))
    #     # if count == 40000:
    #     #     break
    # print(len(list(set((data_list)))))
