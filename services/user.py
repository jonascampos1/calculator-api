from models.user import userTable
from config.db import conn
from models.user import User


def get_users():
    r = conn.execute(userTable.select()).fetchall()
    return r


def create_user(user: User):
    resultc = conn.execute(userTable.insert().values(user))
    return conn.execute(userTable.select().where(userTable.c.id == resultc.lastrowid)).first()


def verify_user_exist(username):
    resultv = conn.execute(userTable.select().where(userTable.c.username == username)).first()
    return resultv

def getBalance_(id):
    
    resultb = conn.execute(userTable.select().where(userTable.c.id == id)).first()
    return int(resultb['balance'])
    