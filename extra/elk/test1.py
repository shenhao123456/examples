import json
import time

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

es = Elasticsearch([{"host": "30.207.39.18", "port": "9200"}], timeout=36000, )


query_index = "dnslog_2020-07-15"

body = {
    "query": {
        "bool": {
            "must": [
                {
                    "term": {
                        "domain.keyword": "ips.ifeng.com"
                    }
                }
            ],
            "must_not": [
                {
                    "term": {
                        "covered.keyword": ""
                    }
                }
            ]
        }
    }
}