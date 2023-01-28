from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import INTEGER, VARCHAR, FLOAT, DATETIME
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

operationTable = Table("Operation", meta,
                  Column("id", INTEGER, primary_key=True),
                  Column("type", VARCHAR(30)),
                  Column("cost", FLOAT),
                )

recordTable = Table("Record", meta,
                  Column("id", INTEGER, primary_key=True),
                  Column("operation_id", INTEGER),
                  Column("user_id", INTEGER),
                  Column("amount", FLOAT),
                  Column("user_balance", FLOAT),
                  Column("operation_response", VARCHAR(30)),
                  Column("date", DATETIME),
                  Column("deletedAt", DATETIME, nullable=True)
                )

meta.create_all(engine)

class Operation(BaseModel):
    id: Optional[str]
    type: str
    cost: float

class Record(BaseModel):
    id: Optional[str]
    operation_id: int
    user_id: int
    amount: float
    user_balance: float
    operation_response: float
    date: datetime
    deletedAt: Optional[str]
