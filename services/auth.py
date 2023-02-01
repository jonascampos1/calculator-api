from config.pymysql_db import connect_mysql
import hashlib


def auth_user(username, password):
   
    
    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `User` WHERE `username`=%s"
            cursor.execute(sql, (username))
            res = cursor.fetchone()
            cursor.close()

    

    if res is None:
        return {'auth': 0,
                'username': '',
                'user_id': ''
                }
    else:
        
        password_hashed = hashlib.md5(password.encode('utf-8')).hexdigest()
        if username == res['username'] and password_hashed == res['password']:
            return {'auth': 1,
                    'username': res['username'],
                    'user_id': res['id'],
                    'balance': res['balance']
                    }
        else:
            return {'auth': 0}
