from mysqlhelper import *

mysql = MySqlHelper()


def main():
    conn, cursor = mysql.context()
    sql = "select * from db_student"
    cursor.execute(sql)
    res = cursor.fetchall()
    for item in res:
        print(item)


if __name__ == '__main__':
    main()
