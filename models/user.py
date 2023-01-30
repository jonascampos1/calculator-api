from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import INTEGER, VARCHAR, SMALLINT, FLOAT
from typing import Optional
from pydantic import BaseModel

userTable = Table("User", meta,
                  Column("id", INTEGER, primary_key=True),
                  Column("username", VARCHAR(30)),
                  Column("password", VARCHAR(50)),
                  Column('status', SMALLINT),
                  Column('balance', FLOAT)
                )

meta.create_all(engine)

class User(BaseModel):
    id: Optional[str]
    username: str
    password: str
    balance: float
    status: int
