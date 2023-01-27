from config.db import conn
from models.calculator import operationTable, recordTable, Record

from math import sqrt, floor

def sum_(v1,v2): 
    return v1+v2

def sub_(v1,v2): 
    return v1-v2

def mult_(v1,v2): 
    return v1*v2

def div_(v1,v2): 
    return v1/v2

def sqrt_(v1): 
    return round(sqrt(v1),2)

def rand_str_():
    return 'askkdjajds'

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
    print(f"****************{user_id}")
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