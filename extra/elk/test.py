import datetime
import time

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

es = Elasticsearch([{"host": "30.207.39.18", "port": "9200"}], timeout=36000, )

index = 'dnslog_2020-06-08'
body = {
    "size": 0,
    "aggs": {
        "aggregation_name": {
            "terms": {
                "field": "domain.keyword",
                "size": 5
            }
        }
    }
}

queryData = es.search(index=index, body=body)

date_list = queryData['aggregations']['aggregation_name']['buckets']
print(len(date_list))
for item in date_list:
    print(item)
    # print(item.get('doc_count'))

# print((datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'))