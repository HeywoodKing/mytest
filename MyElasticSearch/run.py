from setting import *
from elasticsearch import Elasticsearch
from elasticsearch import helpers


class ElasticSearchDb(object):
    def __init__(self):
        self.es = None

    def connect(self):
        self.es = Elasticsearch(ES_ADDRESS)

    def count(self, data=None):
        return self.es.count(index='new_electron', q=data)

    def insert(self, data=None):
        pass

    def delete(self, data=None):
        try:
            res = self.es.delete(index=data['index'], body=data['body'])
            return res
        except Exception as ex:
            raise ex

    def update(self, data=None):
        try:
            res = self.es.update(index=data['index'], body=data['body'])
            return res
        except Exception as ex:
            raise ex

    """
    常用参数:
    index - 索引名
    q - 查询指定匹配 使用Lucene查询语法
    from_ - 查询起始点  默认0
    doc_type - 文档类型
    size - 指定查询条数 默认10
    field - 指定字段 逗号分隔
    sort - 排序  字段：asc/desc
    body - 使用Query DSL
    scroll - 滚动查询
    """
    def find(self, data=None):
        """
        :param data:
        data = {
            "index": "new_electron",
            "type": "_doc",
            "body": {
                "query": {
                    "match": {
                        "_id": "232169"
                    }
                }
            },
        }
        :return:
        """
        try:
            res = self.es.search(index=data['index'], body=data['body'])
            return res
        except Exception as ex:
            raise ex


if __name__ == "__main__":
    es = ElasticSearchDb()
    es.connect()
    # num = es.count(data='http_status_code:500')
    # print(num)

    # data_query = {
    #     "index": "new_electron",
    #     "type": "_doc",
    #     "body": {
    #         "query": {
    #             "bool": {
    #                 "must": [
    #                     {
    #                         "query_string": {
    #                             "default_field": "id",
    #                             "query": "232169"
    #                         }
    #                     }
    #                 ],
    #                 "must_not": [],
    #                 "should": []
    #             }
    #         },
    #         "from": 0,
    #         "size": 10,
    #         "sort": [],
    #         "aggs": {}
    #     },
    # }

    # data_query = {
    #     "index": "new_electron",
    #     "type": "_doc",
    #     "body": {
    #         "query": {
    #             "bool": {
    #                 "must": {
    #                     "match": {
    #                         "content": "123"
    #                     }
    #                 }
    #             }
    #         },
    #         # "highlight": {
    #         #     "fields": {
    #         #         "content": {}
    #         #     }
    #         # },
    #         "from": 0,
    #         "size": 10,
    #         "sort": [],
    #         "aggs": {}
    #     },
    # }

    # data_query = {
    #     "index": "new_electron",
    #     "type": "_doc",
    #     "body": {
    #         "query": {
    #             "match": {
    #                 "content": "MLX92231"
    #             }
    #         },
    #         "highlight": {
    #             "fields": {
    #                 "content": {}
    #             }
    #         },
    #         "from": 0,
    #         "size": 10,
    #         "sort": [],
    #         "aggs": {}
    #     },
    # }

    # data_query = {
    #     "index": "new_electron",
    #     "type": "_doc",
    #     "body": {
    #         "query": {
    #             "bool": {
    #                 "must": [
    #                     # {
    #                     #     "match_all": {}
    #                     # },
    #
    #                     {
    #                         "match": {
    #                             "content": "123"
    #                         }
    #                     },
    #
    #                     # {
    #                     #     "term": {
    #                     #         "content": "aaa"
    #                     #     }
    #                     # }
    #                 ],
    #                 "must_not": [],
    #                 "should": [],
    #             }
    #         },
    #         "highlight": {
    #             "fields": {
    #                 "content": {}
    #             }
    #         },
    #         "from": 0,
    #         "size": 10,
    #         "sort": [],
    #         "aggs": {}
    #     },
    # }

    data_query = {
        "index": "new_electron",
        "type": "_doc",
        "body": {
            "query": {
                # "match": {
                #     "content": "123"
                # }
                "match_all": {}
            }
        },
    }

    # data_query = {
    #     "index": "new_electron",
    #     "type": "_doc",
    #     "body": {
    #         "query": {
    #             "bool": {
    #                 "must": {
    #                     "match": {
    #                         "content": "123"
    #                     }
    #
    #                     # "match": {
    #                     #     "content": {
    #                     #         "query": "aaa",
    #                     #         "operator": "or",
    #                     #         "minimum_should_match": "50%"
    #                     #     }
    #                     # }
    #                 }
    #
    #                 # "must": [
    #                 #     # {
    #                 #     #     "match_all": {}
    #                 #     # }
    #                 #     {
    #                 #         "match": {
    #                 #             "content": "123"
    #                 #         }
    #                 #     }
    #                 #     # {
    #                 #     #     "term": {
    #                 #     #         "content": "aaa"
    #                 #     #     }
    #                 #     # }
    #                 # ],
    #                 # "must_not": [],
    #                 # "should": [],
    #
    #                 # "filter": {
    #                 #     "range": {
    #                 #         "price": {
    #                 #             "gt": 400,
    #                 #             "lt": 700
    #                 #         }
    #                 #     }
    #                 # }
    #             }
    #         },
    #         "highlight": {
    #             "fields": {
    #                 "content": {}
    #             }
    #         },
    #         "from": 0,
    #         "size": 10,
    #         "sort": [],
    #         "aggs": {}
    #     },
    # }

    # data_query = {
    #     "index": "new_electron",
    #     "type": "_doc",
    #     "body": {
    #         "query": {
    #             "multi_match": {
    #                 "query": "EPCOS",  # 查询关键字，多个关键字之间是或的关系
    #                 "fields": ['content', 'supplier']  # title或address字段中有老人或起火字段
    #             }
    #         },
    #         "highlight": {
    #             "fields": {
    #                 "content": {}
    #             }
    #         },
    #         "from": 0,
    #         "size": 10,
    #         "sort": [],
    #         "aggs": {}
    #     },
    # }

    res = es.find(data_query)
    print(res)
    if res['hits']['total']:
        print('获取到数据')
        # print(res['hits']['hits'])
        for item in res['hits']['hits']:
            # print(item)
            print(item['_source'])
    else:
        print('未获取到数据')

    # res = es.find(query='http_status_code:5* AND server_name:"web1"')
    # {'took': 21, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'failed': 0}, 'hits': {'total': 0, 'max_score': None, 'hits': []}}
    # print(res['hits']['hits'])

    # if res['hits']['hits']:
    #     print('获取到数据')
    # else:
    #     print('未获取到数据')




