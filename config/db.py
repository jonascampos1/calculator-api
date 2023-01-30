from urllib.parse import quote_plus
from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

load_dotenv()

user=os.getenv('MYSQL_USER')
password=os.getenv('MYSQL_PASSWORD')
host=os.getenv('MYSQL_HOST')
database=os.getenv('MYSQL_DATABASE')


engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:3306/{database}')

meta = MetaData()

conn = engine.connect()
