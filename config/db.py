from urllib.parse import quote_plus
from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://jonas:password@db:3306/calculator')

meta = MetaData()

conn = engine.connect()
