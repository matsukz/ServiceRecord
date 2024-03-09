#テーブルのモデルを定義する
from Extend import database

from sqlalchemy import Column
from sqlalchemy import Integer,BigInteger,String,DateTime,Time

class Worktime(database.Base):
    __tablename__ = database.db_table
    id = Column("id",BigInteger,primary_key=True)
    date = Column("date",DateTime)
    start_time = Column("start_time",Time)
    end_time = Column("end_time",Time)