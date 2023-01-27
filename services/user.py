from models.user import userTable
from config.db import conn
from models.user import User


def get_users():
    r = conn.execute(userTable.select()).fetchall()
    return r


def create_user(user: User):
    result = conn.execute(userTable.insert().values(user))
    return conn.execute(userTable.select().where(userTable.c.id == result.lastrowid)).first()


def verify_user_exist(username):
    result = conn.execute(userTable.select().where(userTable.c.username == username)).first()
    return result
