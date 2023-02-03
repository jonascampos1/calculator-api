from config.pymysql_db import connect_mysql
import hashlib

password1_hashed = hashlib.md5('aB12345@'.encode('utf8')).hexdigest()
password2_hashed = hashlib.md5('aB12345#'.encode('utf8')).hexdigest()

connection = connect_mysql()
with connection:
    with connection.cursor() as cursor:

        cursor.execute('CREATE TABLE `Operation` (\
        `id` int(11) NOT NULL AUTO_INCREMENT,\
        `type` varchar(30) DEFAULT NULL,\
        `cost` float DEFAULT NULL,\
        PRIMARY KEY (`id`)\
        ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;\
        ')
        cursor.execute('CREATE TABLE `Record` (\
        `id` int(11) NOT NULL AUTO_INCREMENT,\
        `operation_id` int(11) DEFAULT NULL,\
        `user_id` int(11) DEFAULT NULL,\
        `amount` float DEFAULT NULL,\
        `user_balance` float DEFAULT NULL,\
        `operation_response` varchar(30) DEFAULT NULL,\
        `date` datetime DEFAULT NULL,\
        `deletedAt` datetime DEFAULT NULL,\
        PRIMARY KEY (`id`)\
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;\
        ')

        cursor.execute('CREATE TABLE `User` (\
        `id` int(11) NOT NULL AUTO_INCREMENT,\
        `username` varchar(30) DEFAULT NULL,\
        `password` varchar(50) DEFAULT NULL,\
        `status` smallint(6) DEFAULT NULL,\
        `balance` float DEFAULT NULL,\
        PRIMARY KEY (`id`)\
        ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;\
        ')

        sql = "INSERT INTO `Operation` (\
                type,\
                cost\
                ) \
                VALUES(%s,%s)"
        cursor.execute(sql, ('addition','1'))
        cursor.execute(sql, ('substraction','2'))
        cursor.execute(sql, ('multiplication','3'))
        cursor.execute(sql, ('division','4'))
        cursor.execute(sql, ('square_root','5'))
        cursor.execute(sql, ('random_string','6'))

        sql = "INSERT INTO `User` (\
                username,\
                password,\
                status,\
                balance\
                ) \
                VALUES(%s,%s,%s,%s)"
        cursor.execute(sql, ('test1@test.com',password1_hashed,'0','30'))
        cursor.execute(sql, ('test2@test.com',password2_hashed,'0','30'))
       
    connection.commit()


