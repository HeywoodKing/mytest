HOST = '172.17.0.2'
PORT = 3306
USER = 'root'
PASSWORD = '123456'
DATABASE = 'db_student'
CHARSET = 'utf8mb4'

DB_URI = 'mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}?charset={charset}'.format(user=USER, pwd=PASSWORD, host=HOST,
                                                                            port=PORT, db=DATABASE, charset=CHARSET)
