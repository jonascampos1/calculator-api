from config.db import conn
from models.calculator import operationTable, recordTable
from flask import jsonify
from datetime import datetime
from math import sqrt

def getOperations_by_type_(type_: str):
    res = conn \
        .execute(operationTable
                 .select()
                 .where(operationTable.c.type == type_ ))\
                 .first()
    return res
    

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

def sum_(v1,v2,user_id, operation, user_balance):
    result = v1+v2
    r = getOperations_by_type_(operation)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    return response
    
    

def sub_(v1,v2,user_id, operation, user_balance):
    result = v1-v2
    r = getOperations_by_type_(operation)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    return response
    

def mult_(v1,v2,user_id, operation, user_balance): 
    result = v1*v2
    r = getOperations_by_type_(operation)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    return response


def div_(v1,v2,user_id, operation, user_balance): 
    result = v1/v2
    r = getOperations_by_type_(operation)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    return response


def sqrt_(v1,user_id, operation, user_balance):
    result = round(sqrt(v1),2)
    r = getOperations_by_type_(operation)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
    return response


def rand_str_(user_id, operation, user_balance, result):
    r = getOperations_by_type_(operation)
    user_balance = user_balance - r["cost"]
    insertRecord(user_id, operation, user_balance, result)
    response = { 'result': result, 'user_balance': user_balance, 'cost': r["cost"]}
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


def getRecords_(user_id: int):
    res = conn \
        .execute(recordTable
                 .select()
                 .where(recordTable.c.user_id == user_id ))\
                 .fetchall()
    
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