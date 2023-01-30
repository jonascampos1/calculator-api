from config.db import conn
from models.calculator import operationTable, recordTable
from models.user import userTable
from flask import jsonify
from datetime import datetime
from math import sqrt
from services.user import getBalance_


def getOperations_by_type_(type_: str):
    res = conn \
        .execute(operationTable
                 .select()
                 .where(operationTable.c.type == type_ ))\
                 .first()
    return res


def checkBalance_(operation: str, user_id: int):
    rcost = conn \
        .execute(operationTable
                 .select(operationTable.c.cost)
                 .where(operationTable.c.type == operation ))\
                 .first()
    
    ruser = conn \
        .execute(userTable
                 .select(userTable.c.balance)
                 .where(userTable.c.id == user_id ))\
                 .first()
    if rcost is not None and ruser is not None:
        if ((ruser.balance - rcost.cost) >= 0 ):
            return {'check': True}
        else:
            return {'check': False}
    else:
        return {'check': False}
    

def insertRecord(user_id, operation: str, user_balance, response):
    res = conn \
        .execute(operationTable
                 .select()
                 .where(operationTable.c.type == operation ))\
                 .first()
    if res is not None:
        record = {
            'operation_id': res["id"],
            'user_id': user_id,
            'amount': res["cost"],
            'user_balance': user_balance,
            'operation_response': response,
            'date': datetime.now()
        }
        result = conn.execute(recordTable.insert().values(record))
    return 0

def sum_(v1,v2,user_id, operation):
    result = v1+v2
    r = getOperations_by_type_(operation)
    user_balance = getBalance_(user_id)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    updateBalance(user_id, user_balance)
    return response
    
    

def sub_(v1,v2,user_id, operation):
    result = v1-v2
    r = getOperations_by_type_(operation)
    user_balance = getBalance_(user_id)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    updateBalance(user_id, user_balance)
    return response
    

def mult_(v1,v2,user_id, operation): 
    result = v1*v2
    r = getOperations_by_type_(operation)
    user_balance = getBalance_(user_id)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    updateBalance(user_id, user_balance)
    return response


def div_(v1,v2,user_id, operation): 
    result = v1/v2
    r = getOperations_by_type_(operation)
    user_balance = getBalance_(user_id)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    updateBalance(user_id, user_balance)
    return response


def square_root_(v1,user_id, operation):
    result = round(sqrt(v1),2)
    r = getOperations_by_type_(operation)
    user_balance = getBalance_(user_id)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    updateBalance(user_id, user_balance)
    return response


def rand_str_(user_id, operation, result):
    r = getOperations_by_type_(operation)
    user_balance = getBalance_(user_id)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    updateBalance(user_id, user_balance)
    return response


def getOperations_():
    res = conn \
        .execute(operationTable
                 .select()).fetchall()
    operation=[]
    for item in res:
        operation.append({
            'id': item.id,
            'type': item.type,
            'cost': item.cost
        })
    return operation

def getTotalRecords(user_id):
    
    res = conn \
        .execute\
        (f"SELECT count(1) as total FROM Record \
        WHERE user_id={user_id} \
        AND deletedAt is NULL\
        ").first()
    return res.total

def getRecords_(user_id, page, order_field, order, elements_peer_page):
    npag = (page-1)*elements_peer_page
    res = conn \
        .execute\
        (f"SELECT * FROM Record \
        WHERE user_id={user_id} \
        AND deletedAt IS NULL\
        ORDER BY {order_field} {order}\
        LIMIT {npag},{elements_peer_page}\
        ").fetchall()
    
    
    record=[]
    for item in res:
        record.append({
            'id': item.id,
            'operation_id': item.operation_id,
            'user_id': item.user_id,
            'amount': item.amount,
            'user_balance': item.user_balance,
            'operation_response': item.operation_response,
            'date': item.date.strftime("%Y-%m-%d %H:%M"),
            'deletedAt': item.deletedAt,
        })
    return record

def deleteRecord_(id):
    date = datetime.now()
    date = str(date)
    res = conn.execute(f'UPDATE Record SET deletedAt="{date}" WHERE id="{id}"')

def updateBalance(user_id, user_balance):
    res = conn.execute(f'UPDATE User SET BALANCE="{user_balance}" WHERE id="{user_id}"')
