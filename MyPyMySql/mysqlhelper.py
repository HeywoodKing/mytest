from setting import *
import pymysql


class MySqlHelper(object):
    def __init__(self):
        pass

    def context(self, is_dict_cursor=True):
        try:
            config = {
                'host': HOST,
                'port': PORT,
                'user': USER,
                'password': PASSWORD,
                'database': DATABASE,
                'charset': CHARSET
            }
            conn = pymysql.connect(**config)
            """
            类型	描述
            Cursor	普通的游标对象，默认创建的游标对象
            SSCursor	不缓存游标，主要用于当操作需要返回大量数据的时候
            DictCursor	以字典的形式返回操作结果
            SSDictCursor	不缓存游标，将结果以字典的形式进行返回
            
            #方式1：pymysql.connection()中指定参数
            conn = pymysql.connect(host = "127.0.0.1",user = "root",password = "root",database = "new_futures",
            charset = 'utf8',cursorclass = pymysql.cursors.DictCursor)
             
            #方式2：conn.cursor()中指定参数
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            """
            if is_dict_cursor:
                cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            else:
                cursor = conn.cursor()
            return conn, cursor
        except Exception as ex:
            raise Exception(ex)
