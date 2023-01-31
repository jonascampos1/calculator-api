from models.user import userTable
from config.db import conn
from models.user import User
import pymysql
import os

try:
    conn2 = pymysql.connect(
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        host=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'),
    )
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Error db no connect: ", e)

cursor =  conn2.cursor()

def get_users():
    r = conn.execute(userTable.select()).fetchall()
    return r


def create_user(user):
    resultc = conn.execute(userTable.insert().values(user))
    return conn.execute(userTable.select().where(userTable.c.id == resultc.lastrowid)).first()


def verify_user_exist(username):
    resultv = conn.execute(userTable.select().where(userTable.c.username == username)).first()
    return resultv

def getBalance_(id):
    cursor.execute('SELECT balance FROM User WHERE id='+str(id))
    resultb= cursor.fetchone()
    #resultb = conn.execute(userTable.select().where(userTable.c.id == id)).first()
    for e in resultb:
        return e
    
    
    