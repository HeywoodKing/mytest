# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库
db = pymysql.connect('localhost', 'user', '123456', 'TestDB')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行sql
cursor.execute('select version()')

# 使用fetchone()方法获取一条数据记录
data = cursor.fetchone()
# cursor.fetchall()
# cursor.rowcount

print('Database version: %s' % data)

# 如果数据表已经存在使用execute()方法删除表
cursor.execute('drop table if exists employee')

# 创建数据表sql语句
sql = '''create table employee(
first_name char(20) not null,
last_name char(20),
age int,
sex char(1),
income float)
'''

cursor.execute(sql)

sql = '''insert into employee(
first_name,last_name,age,sex,income) 
values("Mac","Mohan",20,"M",2000)'''

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)


try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 回滚
    db.rollback()

# 关闭数据库连接
db.close()





