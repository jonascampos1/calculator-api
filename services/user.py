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
    connection = connect_mysql()

    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "INSERT INTO `User` (\
                    username,\
                    password,\
                    status,\
                    balance\
                    ) \
                    VALUES(%s,%s,%s,%s)"
            print(sql, (user["username"],user['password'],user['active'],user['balance']))
            cursor.execute(sql, (user["username"],user['password'],user['active'],user['balance']))
            
        connection.commit()
        r = connection.insert_id()
    return r


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
    

