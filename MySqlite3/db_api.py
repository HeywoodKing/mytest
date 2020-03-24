from db_set import *


def main():
    sql = {
        "create": "create table general_tab(card_id integer, name text, address text)",
        "insert": [
            "insert into general_tab(card_id,name,address) values(1, 'LiMing', 'East Zone')",
            "insert into general_tab(card_id,name,address) values(2, 'WangMing', 'West Zone')",
            "insert into general_tab(card_id,name,address) values(3, 'ZhaoMing', 'South Zone')",
            "insert into general_tab(card_id,name,address) values(4, 'DingMing', 'North Zone')",
        ],
        "select": "select * from general_tab",
        "update": "update general_tab set name = 'QianMing' where card_id=4",
        "delete": "delete from general_tab where card_id = 3",
    }

    conn = connect(db_name)
    conn.row_factory = Row
    cursor = conn.cursor()

    print('create table')
    cursor.execute(sql['create'])
    print('insert')
    for t in sql['insert']:
        cursor.execute(t)

    cursor.execute(sql['select'])
    res = cursor.fetchall()
    for item in res:
        print(item)

    print('update')
    cursor.execute(sql['update'])
    cursor.execute(sql['select'])
    res = cursor.fetchall()
    for item in res:
        print(item)

    print('delete')
    cursor.execute(sql['delete'])
    cursor.execute(sql['select'])
    res = cursor.fetchall()
    for item in res:
        print(item)

    # cursor.fetchone()
    # cursor.fetchmany()

    # cursor.execute()
    # cursor.executemany()
    # cursor.executescript()

    # cursor.commit()
    # cursor.rollback()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
