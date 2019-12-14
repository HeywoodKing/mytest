# -*- encoding: utf-8 -*-
"""
@File           : read_file.py
@Time           : 2019/11/21 18:57
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import pandas as pd
from sqlalchemy import create_engine
from MyPandas.setting import *


def read_excel():
    df = pd.read_excel(
        FILE_PATH,
        'tb_electron_factory - 副本',
        index_col=None,
        # columns=['id', 'zh_name', 'en_name', 'new_zh_name', 'new_en_name', 'new_id'],
        # na_values=['NA']
    )
    print(df.head(5))
    # print(df.info())
    # df.fillna(0)
    # df.isna()
    # print(df.tail(5))
    for row in df.itertuples(index=True, name='factory'):
        # if pd.isna(getattr(row, 'new_id')):
        if pd.isnull(getattr(row, 'new_id')):
            # 无需变更
            pass
        else:
            # 需要变更
            if getattr(row, 'id') == getattr(row, 'new_id'):
                print('相等')
                # print(type(getattr(row, 'id')), type(getattr(row, 'new_id')))

            else:
                print('不相等')
                # print(type(getattr(row, 'id')), type(getattr(row, 'new_id')))

            # print(row)
            print(
                int(getattr(row, 'id')),
                getattr(row, 'zh_name'),
                getattr(row, 'en_name'),
                int(getattr(row, 'new_id')),
                getattr(row, 'new_zh_name'),
                getattr(row, 'new_en_name')
            )


def db_to_excel():
    try:
        engine = create_engine(DB_URL)
        with engine.connect() as conn:
            # df = pd.read_sql_table(table_name='temp_electron_factory_mapping', con=conn)

            # sql = "select * from temp_electron_factory_mapping where new_id is not null"
            # df = pd.read_sql(sql, con=conn)
            # df = pd.read_sql_query(sql, conn)
            # print(df)

            # df = pd.read_clipboard(sep='|')
            # print(df, df.columns, type(df.columns))
            # clip_context = df.columns[0]
            # print(clip_context)
            pass

    except Exception as ex:
        print(ex)


def excel_to_db():
    try:
        engine = create_engine(DB_URL)
        # conn = engine.connect()

        df = pd.read_excel(
            FILE_PATH,
            'tb_electron_factory - 副本',
            index_col=None,
            # columns=['id', 'zh_name', 'en_name', 'new_zh_name', 'new_en_name', 'new_id'],
            # na_values=['NA']
        )

        """
        name是表名
        con是连接
        if_exists：表如果存在怎么处理
            append：追加
            replace：删除原表，建立新表再添加
            fail：什么都不干
        index=False：不插入索引index
        """
        with engine.connect() as conn, conn.begin():
            df.to_sql(name='temp_electron_factory_mapping', con=conn, if_exists='replace', index=False)

        print('excel to db 导入成功')
    except Exception as ex:
        print(ex)
