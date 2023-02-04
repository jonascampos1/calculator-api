from config.pymysql_db import connect_mysql
from datetime import datetime
from math import sqrt


def getOperations_by_type_(type_: str):
    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Operation` WHERE `type`=%s"
            cursor.execute(sql, (type_))
            res = cursor.fetchone()
            cursor.close()
    
    return res


def checkBalance_(operation: str, user_id: int):
    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql1 = "SELECT `cost` FROM `Operation` WHERE `type`=%s"
            cursor.execute(sql1, (operation))
            rcost = cursor.fetchone()

            sql2 = "SELECT * FROM `User` WHERE `id`=%s"
            cursor.execute(sql2, (user_id))
            ruser = cursor.fetchone()

            cursor.close()

    if rcost is not None and ruser is not None:
        res = ruser['balance'] - rcost['cost']
        if res >= 0:
            return {'check': True, 'balance_result': res}
        else:
            return {'check': False}
    else:
        return {'check': False}
    

def insertRecord(user_id, operation: str, user_balance, response):
    
    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Operation` WHERE `type`=%s"
            cursor.execute(sql, (operation))
            res = cursor.fetchone()
    
    if res is not None:
        

        connection = connect_mysql()
        with connection:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "INSERT INTO `Record` (\
                        operation_id,\
                        user_id,\
                        amount,\
                        user_balance,\
                        operation_response,\
                        date) \
                        VALUES(%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (res["id"],user_id,res["cost"],user_balance,response,datetime.now()))
                res = cursor.fetchone()
            connection.commit()

    return 0

def sum_(v1,v2):
    if type(v1) not in [int,float]:
        raise TypeError("Invalid v1 int or float neded")
    if type(v2) not in [int,float]:
        raise TypeError("Invalid v1 int or float neded")

    result = v1+v2    
    return result
    
    

def sub_(v1,v2):
    if type(v1) not in [int,float]:
        raise TypeError("Invalid v1 int or float neded")
    if type(v2) not in [int,float]:
        raise TypeError("Invalid v1 int or float neded")

    result = v1-v2    
    return result
    

def mult_(v1,v2):
    if type(v1) not in [int,float]:
        raise TypeError("Invalid v1 int or float neded")
    if type(v2) not in [int,float]:
        raise TypeError("Invalid v1 int or float neded")

    result = v1*v2    
    return result


def div_(v1,v2):
    if type(v1) not in [int,float]:
        raise TypeError("Invalid v1 int or float neded")
    if type(v2) not in [int,float]:
        raise TypeError("Invalid v1 int or float neded")

    if v2==0:
        raise ZeroDivisionError('Division by zero not possible')
        
    result = v1/v2
    return result


def square_root_(v1):
    if type(v1) not in [int,float]:
        raise TypeError("Invalid v1 int or float neded")

    if v1<0:
        raise ValueError('Square root from a negative value does not exists')

    result = round(sqrt(v1),2)
    return result


def getOperations_():
    
    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Operation`"
            cursor.execute(sql)
            res = cursor.fetchone()
            cursor.close()

    operation=[]
    for item in res:
        operation.append({
            'id': item.id,
            'type': item.type,
            'cost': item.cost
        })
    return operation

def getTotalRecords(user_id):
    
    

    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT COUNT(1) as total FROM `Record` WHERE `user_id`=%s AND deletedAt is NULL"
            cursor.execute(sql,(user_id))
            res = cursor.fetchone()
            cursor.close()

    return res['total']

def getRecords_(user_id, page, order_field, order, elements_peer_page):
    npag = (page-1)*elements_peer_page
    

    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM Record \
                    WHERE user_id=%s \
                    AND deletedAt IS NULL\
                    ORDER BY %s %s\
                    LIMIT %s,%s"
            cursor.execute(sql,(user_id,order_field,order,npag,elements_peer_page))
            res = cursor.fetchall()
            cursor.close()
    
    
    record=[]
    for item in res:
        record.append({
            'id': item['id'],
            'operation_id': item['operation_id'],
            'user_id': item['user_id'],
            'amount': item['amount'],
            'user_balance': item['user_balance'],
            'operation_response': item['operation_response'],
            'date': item['date'].strftime("%Y-%m-%d %H:%M"),
            'deletedAt': item['deletedAt'],
        })
    return record

def deleteRecord_(id):
    date = datetime.now()
    date = str(date)

    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = 'UPDATE Record SET deletedAt=%s WHERE id=%s'
            cursor.execute(sql,(date,id))
            cursor.close()

def updateBalance(user_id, user_balance):
    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "UPDATE User SET balance='%s' WHERE id='%s'"
            cursor.execute(sql,(user_balance,user_id))
        connection.commit()