from urllib.parse import quote_plus
from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://igle_jonas:%s@31.220.21.34:3306/igle_calculator'% quote_plus('Amdk@62400'))

meta = MetaData()

conn = engine.connect()
