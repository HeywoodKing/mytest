# -*- encoding: utf-8 -*-
"""
@File           : helper.py
@Time           : 2019/11/7 14:03
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mofang_data_cleaning
@description    : 描述
"""
import hashlib
import logging
import time
import pymysql
import pymongo
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from es_category_cleaning.setting import *

logger = logging.getLogger('es_electron_kwargs_helper_log')


# 获取哈希列表
def get_hash_256():
    """
    得到256个两位数字符串
    :return:
    """
    results_set = set()
    for i in range(0, 256):
        k = hex(i)[-2:]
        if k[0] == 'x':
            k = k.replace('x', '0')
        results_set.add('{}'.format(k))

    results_set = sorted(results_set)
    # print('数量：', len(results_set))
    return results_set


def get_hash_id(address, max_num):
    """
    根据 address 确定唯一 hash 值（确定分表）
    """
    hash_str = hashlib.md5(address.encode(encoding='UTF-8')).hexdigest()  # 16进制 -- 900150983cd24fb0d6963f7d28e17f72
    num = int(hash_str[:2] + hash_str[-2:], 16)  # 16进制 --> 10进制
    print(hash_str, hash_str[:2], hash_str[-2:], num)
    hash_id = num % max_num  # 8
    print('HashID:', hash_id)
    return hash_id


# 打开MySQL数据库并返回连接和游标
def mysql_context(is_dict_cursor=True, is_sscursor=False):
    """
    打开MySQL数据库并返回连接和游标
    :param is_dict_cursor:
    :param is_sscursor:
    :return:
    """
    try:
        config = {
            'host': MYSQL_HOST,
            'port': MYSQL_PORT,
            'user': MYSQL_USER,
            'password': MYSQL_PASSWORD,
            'database': MYSQL_DATABASE,
            'charset': MYSQL_CHARSET,
        }

        conn = pymysql.connect(**config)
        """
        类型	            描述
        Cursor	        普通的游标对象，默认创建的游标对象                   
        游标结果作为元祖的元祖返回
        说明：
            这是您用于与数据库交互的对象。
            不要自己创建Cursor实例。调用connections.Connection.cursor()

        SSCursor	    不缓存游标，主要用于当操作需要返回大量数据的时候       
        无缓冲游标结果作为元祖的元祖返回
        用途：
            用于返回大量数据查询，或慢速网络连接到远程服务器             
            不将每行数据复制到缓冲区，根据需要获取行。客户端内存使用少
            在慢速网络上或结果集非常大时行返回速度快

        限制：
            MySQL协议不支持返回总行数，判断有多少行唯一方法是迭代返回的每一行。
            目前无法向后滚动，因为只有当前行保存在内存中。

        DictCursor	    以字典的形式返回操作结果
        将结果作为字典返回游标

        SSDictCursor	不缓存游标，将结果以字典的形式进行返回
        无缓冲游标结果作为字典返回
        """
        if is_dict_cursor:
            # 返回结果是字典类型
            if is_sscursor:
                cursor = conn.cursor(cursor=pymysql.cursors.SSDictCursor)
            else:
                cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            # 返回结果是元组类型
            if is_sscursor:
                cursor = conn.cursor(cursor=pymysql.cursors.SSCursor)
            else:
                cursor = conn.cursor()
        return conn, cursor
    except Exception as ex:
        logger.error("connect database failed, {},{}".format(200, ex))
        print("connect database failed, {},{}".format(200, ex))
        raise Exception({'code': 200, 'msg': ex})


# 连接mongodb并返回连接
def mongo_context():
    """
    连接mongodb并返回连接
    :return:
    """
    try:
        # config = {
        #     'host': MYSQL_HOST,
        #     'port': MYSQL_PORT,
        #     'user': MYSQL_USER,
        #     'password': MYSQL_PASSWORD,
        #     'database': MYSQL_DATABASE,
        #     'charset': MYSQL_CHARSET,
        # }

        conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        # db_session = conn[MONGO_NAME][MONGO_TABLE]
        return conn
    except Exception as ex:
        logger.error("connect database failed, {},{}".format(200, ex))
        print("connect database failed, {},{}".format(200, ex))
        raise Exception({'code': 200, 'msg': ex})


# 创建MySQL数据库表
def create_table(sql=None):
    """
    创建表
    :param sql:
    :return:
    """
    if sql is None:
        print('创建表sql语句不能为空！')
        return

    try:
        mysql_conn, mysql_cursor = mysql_context()
        mysql_cursor.execute(sql)
        print('表创建完成')
        mysql_cursor.close()
        mysql_conn.close()
    except Exception as ex:
        print('创建表失败：{}'.format(ex))


# 创建hash 表
def create_hash_table(db_name=None, table_name_prefix=None, sql=None):
    """
    创建hash表
    :param db_name:数据库名
    :param table_name_prefix:hash表前缀
    :param create_sql: 创建表sql
    :return:
    """
    hash_suffix_tables = get_hash_256()
    mysql_conn, mysql_cursor = mysql_context()

    # print('即将删除存在的hash表')
    # mysql_conn.begin()
    # for item in hash_suffix_tables:
    #     table_name = table_name_prefix + item
    #     delete_sql = 'drop table if exists {}.`{}`'.format(db_name, table_name)
    #     mysql_cursor.execute(delete_sql)
    #     print('{}删除完成：{}'.format(item, delete_sql))
    #
    # mysql_conn.commit()
    # print('hash表删除完成')

    # 创建哈希表语句
    # create_sql = """
    # create table if not exists {}.`{}` (
    #     id int(11) not null AUTO_INCREMENT,
    #     model_id int(11),
    #     model_name varchar(256) DEFAULT null,
    #     price decimal(10,2) default '0.00',
    #     factory_id int(11),
    #     factory_zh_name varchar(256) DEFAULT null,
    #     factory_en_name varchar(512) DEFAULT null,
    #     kwargs_id int(11),
    #     kwargs_zh_name varchar(256),
    #     kwargs_en_name varchar(512),
    #     kwargs_value_id int(11),
    #     kwargs_zh_value varchar(256),
    #     kwargs_en_value varchar(512),
    #     cid int(11),
    #     category_id varchar(10),
    #     category_zh_name varchar(256),
    #     category_en_name varchar(512),
    #     primary key(id),
    #     key tb_extra_electron_params_model_name (model_name) USING BTREE,
    #     key tb_extra_electron_params_cid (cid) USING BTREE,
    #     key tb_extra_electron_params_category_id (category_id) USING BTREE
    # ) ENGINE=innodb AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
    # """.format(table_name_prefix + item)

    print('创建hash表')
    mysql_conn.begin()
    for item in hash_suffix_tables:
        table_name = table_name_prefix + item
        delete_sql = 'drop table if exists {}.`{}`'.format(db_name, table_name)
        mysql_cursor.execute(delete_sql)
        print('{} 表删除完成 {}'.format(table_name, delete_sql))

        create_sql = sql.format(db_name, table_name)
        mysql_cursor.execute(create_sql)
        print('{} 表创建完成 {}'.format(table_name, create_sql))

    mysql_conn.commit()
    print('所有hash表创建完成')
    mysql_cursor.close()
    mysql_conn.close()


# 修改哈希表字段等
def alter_hash_table(db_name=None, table_name_prefix=None, sql=None):
    """
    修改hash表字段
    :param db_name:数据库名
    :param table_name_prefix:hash表前缀
    :param create_sql: 修改表sql
    :return:
    """
    hash_suffix_tables = get_hash_256()
    mysql_conn, mysql_cursor = mysql_context()

    mysql_conn.begin()
    for item in hash_suffix_tables:
        table_name = table_name_prefix + item
        create_sql = sql.format(db_name, table_name)
        mysql_cursor.execute(create_sql)
        print('{} 表修改完成 {}'.format(table_name, create_sql))

    mysql_conn.commit()
    print('所有hash表修改完成')
    mysql_cursor.close()
    mysql_conn.close()


# 删除哈希表
def drop_hash_table(db_name=None, table_name_prefix=None):
    """
    删除哈希表
    :param db_name:数据库名
    :param table_name_prefix:hash表前缀
    :return:
    """
    sql = 'drop table if exists {}.`{}`'
    _execute_hash_sql(db_name, table_name_prefix, sql)
    print('所有hash表删除完成')


# 清空哈希表记录
def truncate_hash_table(db_name=None, table_name_prefix=None, is_delete_sql=False):
    """
    清空哈希表记录
    :param db_name:数据库名
    :param table_name_prefix:hash表前缀
    :param is_delete_sql:delete sql or truncate sql?
    :return:
    """
    if is_delete_sql:
        sql = 'delete from table {}.`{}`'
    else:
        sql = 'truncate table {}.`{}`'

    _execute_hash_sql(db_name, table_name_prefix, sql)
    print('所有hash表记录已清空')


# 统计哈希表中满足条件的记录数量
def stat_hash_count(db_name=None, table_name_prefix=None, sql=None):
    """
    统计哈希表中满足条件的记录数量
    :param db_name:
    :param table_name_prefix:
    :param sql:
    :return:
    """
    if sql is None:
        print('统计sql语句不能为空！')
        return

    total_record = 0
    try:
        mysql_conn, mysql_cursor = mysql_context()
        table_suffix_list = get_hash_256()
        for suffix in table_suffix_list:
            table_name = "{}.{}{}".format(db_name, table_name_prefix, suffix)
            new_sql = sql.format(table_name)
            mysql_cursor.execute(new_sql)
            result = mysql_cursor.fetchone()
            total_record += int(result['total'])
            print("表名：{}\n数量：{}\n总量：{}".format(table_name, result['total'], total_record))
            print("+" * 100)

        mysql_cursor.close()
        mysql_conn.close()
    except Exception as ex:
        print(ex)

    print("total_record: {}".format(total_record))

    return total_record


def _execute_hash_sql(db_name=None, table_name_prefix=None, sql=None):
    """
    执行具体的 hash sql 语句
    :param db_name:
    :param table_name_prefix:
    :param sql:
    :return:
    """
    if db_name is None:
        print("数据库名不能为空")
        return

    if table_name_prefix is None:
        print("哈希表前缀不能为空")
        return

    if sql is None:
        print("执行sql不能为空")
        return

    hash_suffix_tables = get_hash_256()
    mysql_conn, mysql_cursor = mysql_context()

    mysql_conn.begin()
    for item in hash_suffix_tables:
        table_name = table_name_prefix + item
        exec_sql = sql.format(db_name, table_name)
        mysql_cursor.execute(exec_sql)
        print('{} 执行完成 {}'.format(table_name, exec_sql))

    mysql_conn.commit()
    print('执行完成')
    mysql_cursor.close()
    mysql_conn.close()


# ============================================================================================

def es_context(host=ES_ADDRESS, http_auth=ES_HTTP_AUTH):
    try:
        if http_auth is None:
            es = Elasticsearch(hosts=host)
        else:
            es = Elasticsearch(
                hosts=host,
                http_auth=http_auth,
                # # 在做任何操作之前，先进行嗅探
                # sniff_on_start=True,
                # # 节点没有响应时，进行刷新，重新连接
                # sniff_on_connection_fail=True,
                # # 每 60 秒刷新一次
                # sniffer_timeout=60,
                # # 打开SSL
                # use_ssl=True,
                # # 确保我们验证了SSL证书（默认关闭）
                # verify_certs=True,
                # # 提供CA证书的路径
                # ca_certs='/path/to/CA_certs',
                # # PEM格式的SSL客户端证书
                # client_cert='/path/to/clientcert.pem',
                # # PEM格式的SSL客户端密钥
                # client_key='/path/to/clientkey.pem'
            )
        # 测试集群是否启动
        # es.ping()
        # 获取集群基本信息
        # es.info()
        # 获取集群的健康状态信息
        # es.cluster.health()
        # 获取当前连接的集群节点信息
        # es.cluster.client.info()
        # 获取集群目前所有的索引
        # es.cat.indices()
        # 获取集群的更多信息
        # es.cluster.stats()
        return es
    except Exception as ex:
        logger.error("connect es failed, {},{}".format(200, ex))
        print("connect es failed, {},{}".format(200, ex))
        raise Exception({'code': 200, 'msg': ex})


# 创建es索引
def es_create_index(index_name=None, index_type="_doc"):
    """
    创建索引, 创建索引名字
    :param index_name: Elasticsearch对象
    :param index_type: Elasticsearch document
    :return:
    """
    es = es_context()
    # 索引 相当于数据库中的 库名
    # _index_mappings = {
    #     "mappings": {
    #         index_type: {  # 相当于数据库中的表名
    #             "properties": {
    #                 "title": {
    #                     "type": "text",
    #                     "index": True,
    #                 },
    #                 "date": {
    #                     "type": "date",
    #                     "store": True,
    #                     "format": "yyyy/MM/dd HH:mm:ss||yyyy/MM/dd||epoch_millis"
    #                 },
    #                 "keyword": {
    #                     "type": "keyword",
    #                     "index": "not_analyzed"
    #                 },
    #                 "source": {
    #                     "type": "string",  # 字符串
    #                     "index": "not_analyzed"
    #                 },
    #                 "link": {
    #                     "type": "string",
    #                     "index": "not_analyzed"
    #                 },
    #                     "zh_parameter": {  # zh_parameter可以存json格式，访问tags.content
    #                         "type": "object",
    #                         "properties": {
    #                             "content": {"type": "keyword", "index": True},
    #                             "dominant_color_name": {"type": "keyword", "index": True},
    #                             "skill": {"type": "keyword", "index": True},
    #                         }
    #                     },
    #                     "en_parameter": {  # en_parameter可以存json格式，访问tags.content
    #                         "type": "object",
    #                         "properties": {
    #                             "content": {"type": "keyword", "index": True},
    #                             "dominant_color_name": {"type": "keyword", "index": True},
    #                             "skill": {"type": "keyword", "index": True},
    #                         }
    #                     }
    #             }
    #         }
    #     }
    # }

    # index = 'category_with_kwargs'
    # _index_mappings = {
    #     "mappings": {
    #         index_type: {  # doc_type=_doc
    #             "properties": {
    #                 "id": {
    #                     "type": "long",
    #                     "index": True
    #                 },
    #                 "category_id": {
    #                     "type": "keyword",  # keyword不会进行分词,text会分词
    #                     "index": True  # 不建索引
    #                 },
    #                 "category_zh_name": {
    #                     "type": "keyword",  # keyword不会进行分词,text会分词
    #                     "index": True  # 不建索引
    #                 },
    #                 "category_en_name": {
    #                     "type": "text",  # keyword不会进行分词,text会分词
    #                     "index": True  # 不建索引
    #                 },
    #                 "zh_parameter": {  # zh_parameter可以存json格式，访问tags.content
    #                     "type": "object",
    #                     "index": True  # 不建索引
    #                 },
    #                 "en_parameter": {  # en_parameter可以存json格式，访问tags.content
    #                     "type": "object",
    #                     "index": True  # 不建索引
    #                 }
    #             }
    #         }
    #     }
    # }

    try:
        if es.indices.exists(index=index_name) is not True:
            # res = es.indices.create(index=index_name, body=_index_mappings, ignore=400)
            res = es.indices.create(index=index_name, ignore=400)
            print('es index {} 创建成功，{}'.format(index_name, res))
        else:
            print('es index 已存在')
    except Exception as ex:
        print('es_create_index:', ex)


# 批量创建es索引
def es_create_index_batch(index_names: list, es_index_prefix: str):
    for item in index_names:
        index_name = '{}{}'.format(es_index_prefix, item)
        es_create_index(index_name)
    print('es index 哈希表创建完成')


# 删除es索引
def es_delete_index(index_name=None):
    # ignore 404 and 400
    es = es_context()
    es.indices.delete(index=index_name, ignore=[400, 404])
    # es.cluster.health(wait_for_status='yellow', request_timeout=1)
    print('es index {} 删除成功'.format(index_name))


# 批量删除es索引
def es_delete_index_batch(index_names: list, es_index_prefix: str):
    for item in index_names:
        index_name = '{}{}'.format(es_index_prefix, item)
        es_delete_index(index_name=index_name)
    print('es index 哈希表删除完成')


# 重建es索引
def es_rebuild_index(index_name_suffix_list: list, es_index_prefix: str):
    """
    重建es index
    :param index_name_suffix_list: index名称后缀
    :param es_index_prefix: index名称后缀
    :return:
    """
    for item in index_name_suffix_list:
        index_name = '{}{}'.format(es_index_prefix, item)
        es_delete_index(index_name)
        es_create_index(index_name)

    print('es index 哈希重建完成')


# 记录操作
# 单条插入
def es_put(index_name=None, doc_type='_doc', _id=None, body=None):
    es = es_context()
    try:
        start_time = time.time()
        # body = {"name": 'lucy', 'sex': 'female', 'age': 10}
        es.index(index=index_name, doc_type=doc_type, id=_id, body=body,)
        end_time = time.time()
        t = end_time - start_time
        print('本次共写入1条数据，用时{}s'.format(t))
    except Exception as ex:
        print(ex)


# 批量插入
def es_put_bulk(actions: list = None, request_timeout=ES_BULK_REQUEST_TIMEOUT):
    es = es_context()
    try:
        start_time = time.time()
        if actions:
            helpers.bulk(es, actions, request_timeout=request_timeout)
            end_time = time.time()
            t = end_time - start_time
            print('本次共写入{}条数据，用时{}s'.format(len(actions), t))
    except Exception as ex:
        print(ex)


# 根据指定host，批量插入
def es_put_bulk_by_host(host, actions: list = None):
    es = es_context(host)
    try:
        start_time = time.time()
        # print(actions)
        if actions:
            helpers.bulk(es, actions)
            end_time = time.time()
            t = end_time - start_time
            print('本次共写入{}条数据，用时{}s'.format(len(actions), t))
    except Exception as ex:
        print(ex)


# 单条删除
def es_delete(index_name=None, doc_type='_doc', _id=None):
    # ignore 404 and 400
    es = es_context()
    try:
        es.delete(index=index_name, doc_type=doc_type, id=_id)
        print('{}删除成功！'.format(_id))
    except Exception as ex:
        print(ex)


# 批量删除
def es_delete_batch(index_name=None, doc_type='_doc', body=None):
    es = es_context()
    try:
        es.delete_by_query(index=index_name, doc_type=doc_type, body=body)
        print('{}删除成功！'.format(_id))
    except Exception as ex:
        print(ex)


# 批量删除
def es_delete_bulk(index_name=None, doc_type='_doc', _id=None):
    # ignore 404 and 400
    es = es_context()
    try:
        es.delete(index=index_name, doc_type=doc_type, id=_id)
        print('{}删除成功！'.format(_id))
    except Exception as ex:
        print(ex)


# 单条更新
def es_update(index_name, doc_type='_doc', _id: int = 0, body: dict = None):
    if body is None:
        print('body is not None')
        return

    start_time = time.time()
    es = es_context()
    try:
        # # 或者:ignore=409忽略文档已存在异常
        # es.create(index=index_name, doc_type=doc_type, id=_id, ignore=409, body=body)
        # 添加或更新数据,index，doc_type名称可以自定义，id可以根据需求赋值,body为内容    如果不写id值的话会生成一个随机数的id
        # es.index(index=index_name, doc_type=doc_type, id=0, body={"name": "python", "addr": "深圳"})
        # es.index(index=index_name, doc_type=doc_type, id=_id, body=body)
        es.update(index=index_name, doc_type=doc_type, id=_id, body=body)

        end_time = time.time()
        t = end_time - start_time
        print('本次共更新数据，用时{}s'.format(t))
    except Exception as ex:
        print(ex)


# 批量更新
def es_update_batch(index_name, doc_type='_doc', body: dict = None):
    """
    批量更新
    :param index_name:
    :param doc_type:
    :param body:
    body = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"_id": "11"}}
                ],
            }
        },
        "script": {
            "inline": "ctx._source.tags = params.tags",
            "params": {
                "tags": tags
            },
            "lang":"painless"

        }
    }
    body = {
        "script": {
        "lang": "painless",
        # "inline": "if (ctx._source.test_code == null) {ctx._source.test_code= '02'}"
        "inline": "ctx._source.kw_sourceType= 'trueTime'"   #新增字段kw_sourceType值为trueTime
    }
    :return:
    """
    if body is None:
        print('body is not None')
        return

    start_time = time.time()
    es = es_context()
    try:
        es.update_by_query(index=index_name, doc_type=doc_type, body=body)

        end_time = time.time()
        t = end_time - start_time
        print('本次共更新数据，用时{}s'.format(t))
    except Exception as ex:
        print(ex)


# 批量更新
def es_update_bulk(index_name, doc_type='_doc', _id: int = 0, body: dict = None):
    start_time = time.time()
    es = es_context()
    try:
        # 添加或更新数据,index，doc_type名称可以自定义，id可以根据需求赋值,body为内容    如果不写id值的话会生成一个随机数的id
        # es.index(index=index_name, doc_type=doc_type, id=0, body={"name": "python", "addr": "深圳"})
        es.index(index=index_name, doc_type=doc_type, id=_id, body=body)

        # # 或者:ignore=409忽略文档已存在异常
        # es.create(index=index_name, doc_type=doc_type, id=_id, ignore=409, body=body)

        end_time = time.time()
        t = end_time - start_time
        print('本次共更新数据，用时{}s'.format(t))
    except Exception as ex:
        print(ex)


# 单条查询
def es_search(index_name=None, doc_type='_doc', _id=None):
    es = es_context()
    try:
        return es.get(index=index_name, doc_type=doc_type, id=_id)
    except Exception as ex:
        print(ex)

    return None


# 条件批量查询
def es_search_batch(index_name=None, doc_type='_doc', query=None):
    es = es_context()
    try:
        result = es.search(index=index_name, doc_type=doc_type, body=query)
        if result['hits']['total']:
            return result['hits']['hits']
    except Exception as ex:
        print(ex)

    return None


# def es_search_bulk(index_name=None, doc_type='_doc', query=None):
#     # data_query = {
#     #     "index": index_name,
#     #     "type": doc_type,
#     #     "body": {
#     #         "query": {
#     #             "match_all": {}
#     #         }
#     #     },
#     # }
#
#     # query = {
#     #     "query": {
#     #         "bool": {
#     #             "must": [
#     #                 {
#     #                     # "match": {
#     #                     #     "zh_parameter": "BE-A"
#     #                     # }
#     #                     "match_all": {}
#     #                 }
#     #             ],
#     #             "must_not": [],
#     #             "should": []
#     #         }
#     #     },
#     #     "from": 0,
#     #     "size": 10,
#     #     "sort": [],
#     #     "aggs": {}
#     # }
#
#     es = es_context()
#     try:
#         res = es.search(index=index_name, doc_type=doc_type, body=query)
#         if res['hits']['total']:
#             data = res['hits']['hits']
#             return data
#     except Exception as ex:
#         print(ex)
#
#     return None


