from config.db import conn
from models.user import userTable
from models.calculator import operationTable
import hashlib

password1_hashed = hashlib.md5('aB12345@'.encode('utf8')).hexdigest()
password2_hashed = hashlib.md5('aB12345#'.encode('utf8')).hexdigest()

conn.execute('TRUNCATE TABLE User')
conn.execute('TRUNCATE TABLE Operation')
conn.execute('TRUNCATE TABLE Record')

user = [
    {'username': 'test1@test.com', 'password': password1_hashed, 'status': 0, 'balance': 30},
    {'username': 'test2@test.com', 'password': password2_hashed, 'status': 0, 'balance': 30},
    ]

result = conn.execute(userTable.insert().values(user))


operation = [
    {'type':'addition', 'cost':1},
    {'type':'substraction', 'cost':2},
    {'type':'multiplication', 'cost':3},
    {'type':'division', 'cost':4},
    {'type':'square_root', 'cost':5},
    {'type':'random_string', 'cost':6}
    ]

result = conn.execute(operationTable.insert().values(operation))



conn.close()