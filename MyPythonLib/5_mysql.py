# -*- coding: utf-8 -*-


import pymysql


# class PyMySqlDb(object):
#     def __init__(self):
#         self.state = False
#         self.context = None
#         self.cursor = None
#
#     def __enter__(self):
#         return self.cursor
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.context.commit()
#         self.cursor.close()
#         self.context.close()
#
#     def connect(self, host='localhost', port=3306, db='test', username='root', password='123456', charset='utf8'):
#         self.context = pymysql.connect(host=host, port=port, user=username, password=password, db=db, charset=charset)
#         if self.context:
#             # 使用 cursor() 方法创建一个游标对象 cursor
#             self.cursor = self.context.cursor()  # cursor=cursors.DictCursor
#
#         return self.context
#
#     def close(self):
#         if self.cursor:
#             self.cursor.close()
#             self.context.close()
#
#     def create_db(self):
#         pass
#
#     def create_table(self, sql, table_name):
#         if self.cursor:
#
#             try:
#                 self.cursor.execute('drop table if exists %s' % table_name)
#                 self.cursor.execute(sql)
#                 return True
#             except:
#                 pass
#
#         return False
#
#     def insert(self, sql):
#         if self.cursor:
#
#             try:
#                 self.cursor.execute(sql)
#                 self.context.commit()
#                 return True
#             except:
#                 self.context.rollback()
#                 return False
#
#         return False
#
#     def delete(self, sql):
#         if self.cursor:
#
#             try:
#                 self.cursor.execute(sql)
#                 self.context.commit()
#                 return True
#             except:
#                 self.context.rollback()
#                 return False
#
#         return False
#
#     def update(self, sql):
#         if self.cursor:
#
#             try:
#                 self.cursor.execute(sql)
#                 self.context.commit()
#                 return True
#             except:
#                 self.context.rollback()
#                 return False
#
#         return False
#
#     def query(self, sql):
#         if self.cursor:
#
#             try:
#                 self.cursor.execute(sql)
#                 self.context.commit()
#                 return True
#             except:
#                 self.context.rollback()
#                 return False
#
#         return False
#
#     def count(self, sql):
#         if self.cursor:
#
#             try:
#                 self.cursor.execute(sql)
#                 count = len(self.cursor.fetchall())
#                 return count
#             except:
#                 self.context.rollback()
#                 return 0
#
#         return 0
#
#     def limit(self):
#         pass
#
#     def exec(self, sql):
#         if self.cursor:
#
#             try:
#                 # 使用 execute()  方法执行 SQL 查询
#                 self.cursor.execute(sql)
#                 # 使用 fetchone() 方法获取单条数据
#                 # data = cursor.fetchone()
#                 data = self.cursor.fetchall()
#                 return data
#             except:
#                 return None
#
#         return None


class MySqlHelper(object):
    def __init__(self, host, port, db, user, passwd, charset='utf8'):
        self.context = None
        self.cursor = None
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.context.commit()
        self.cursor.close()
        self.context.close()

    def open(self):
        self.context = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.passwd, db=self.db, charset=self.charset)
        if self.context:
            # 使用 cursor() 方法创建一个游标对象 cursor
            self.cursor = self.context.cursor()  # cursor=cursors.DictCursor

        return True

    def close(self):
        if self.cursor:
            self.cursor.close()
            self.context.close()

    def create_db(self):
        pass

    def create_table(self, sql, table_name):
        if self.cursor:

            try:
                self.cursor.execute('drop table if exists %s' % table_name)
                self.cursor.execute(sql)
                return True
            except:
                pass

        return False

    def cud(self, sql, params=[]):
        try:
            self.open()
            if self.cursor:
                self.cursor.execute(sql, params)
                self.context.commit()
                return True
        except Exception as e:
            print(e.message)
            self.context.rollback()
            return False
        finally:
            self.close()

    def query(self, sql, params=[]):
        try:
            self.open()
            if self.cursor:
                # 使用 execute()  方法执行 SQL 查询
                self.cursor.execute(sql, params)
                # 使用 fetchone() 方法获取单条数据
                # data = cursor.fetchone()
                return self.cursor.fetchall()
        except Exception as e:
            print(e.message)
            return None
        finally:
            print('finally')
            self.close()


if __name__ == "__main__":
    pmysql = MySqlHelper(host='192.168.99.100', port=3306, db='test', user='root', passwd='123456', charset='utf8')
    # pmysql.open()
    # res = pmysql.query('select version()')
    datas = pmysql.query('select * from subjects')
    for row in datas:
        print(row[0], row[1], str(row[2], encoding='gb2312'))
        # print(row[0], row[1], row[2].decode())



