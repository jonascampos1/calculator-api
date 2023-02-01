from config.pymysql_db import connect_mysql
from models.user import User


def get_users():
    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `User`"
            cursor.execute(sql)
            r = cursor.fetchall()
            cursor.close()
    return r


def create_user(user: User):
    resultc = conn.execute(userTable.insert().values(user))
    return conn.execute(userTable.select().where(userTable.c.id == resultc.lastrowid)).first()


def verify_user_exist(username):
    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `User` WHERE username=%s"
            cursor.execute(sql,(username))
            r = cursor.fetchone()
            cursor.close()
    return r

def getBalance_(id):
    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `User` WHERE id=%s"
            cursor.execute(sql,(id))
            r = cursor.fetchone()
            cursor.close()
    return int(r['balance'])
    

