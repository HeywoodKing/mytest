from db_set import *


def main():
    conn = connect(db_name)
    cursor = conn.cursor()
    sql = "drop table if exists testa; create table if not exists testa(id integer,data blob);"
    cursor.executescript(sql)
    f = open('test.jpg', 'rb')
    cursor.execute('insert into testa(id, data) values(3,?)', (f. read(), ))
    cursor.execute('select * from testa where id = 3')
    record = cursor.fetchone()
    f = open('tt.jpg', 'wb')
    f.write(record[1])

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()


