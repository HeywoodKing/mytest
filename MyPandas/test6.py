# -*- encoding: utf-8 -*-
"""
@File           : segment_table.py
@Time           : 2019/12/12 9:57
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mofang_data_cleaning
@description    : 描述
"""
import pandas as pd
from sqlalchemy import create_engine

from MyPandas.setting import *
# from MyPandas.helper import *


def segment_table_data(from_table_name: str = None, to_table_name: str = None):
    try:
        df = None
        engine = create_engine(DB_URL)
        # with engine.begin() as conn:
        with engine.connect() as conn:
            # query_sql = """
            # replace into tb_electron_digikey_summary select * from tb_electron_digikey
            # where summary is not null and summary != '';
            # """

            query_sql = "select * from {} where 1=1".format(from_table_name)
            df = pd.read_sql(sql=query_sql, con=conn)
            print(df.head())
            print(df.shape, df.shape[0])
            # print(df.count(axis=0))

            if not df.empty:
                print('ok')
                """
                name 是表名
                con 是连接
                if_exists：表如果存在怎么处理
                    append：追加
                    replace：删除原表，建立新表再添加
                    fail：什么都不干
                    index=False：不插入索引index
                """
                # 如果想要自动建表的话if_exists="replace"
                # 如果想要自己建表的话if_exists="append"
                df.to_sql(name=to_table_name, con=conn, index=False, if_exists='append',)

                # df.to_csv(to_table_name+'.csv', sep='\t', index=False, header=False)
            else:
                print('error')

    except Exception as ex:
        print(ex)


def segment_table_data2(from_table_name: str = None, to_table_name: str = None):
    try:
        df = None
        engine = create_engine(DB_URL)
        with engine.raw_connection() as conn:
            query_sql = "select * from {} where 1=1".format(from_table_name)
            df = pd.read_sql(sql=query_sql, con=conn)
            print(df.head())
            print(df.shape, df.shape[0])
            # print(df.count(axis=0))

            if not df.empty:
                print('ok')
                # import cStringIO
                # output = cStringIO.StringIO()
                # df.to_csv(output, sep='\t', index=False, header=False)
                # output.getvalue()
                # output.seek(0)
                # cursor = conn.cursor()
                # cursor.copy_from(output, to_table_name, null='')
                # conn.commit()
                # cursor.close()
            else:
                print('error')

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    segment_table_data("fk_message", "fk_message_backup")
    pass
