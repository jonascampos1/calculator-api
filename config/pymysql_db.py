import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()

def connect_mysql():
    connection = pymysql.connect(host=os.getenv('MYSQL_HOST'),
                            user=os.getenv('MYSQL_USER'),
                            password=os.getenv('MYSQL_PASSWORD'),
                            database=os.getenv('MYSQL_DATABASE'),
                            cursorclass=pymysql.cursors.DictCursor)
    return connection