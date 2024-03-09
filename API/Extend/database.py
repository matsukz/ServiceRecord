#DBの接続情報をセットする
#DB情報
from sqlalchemy.future import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

#環境変数
import os
import sys
from dotenv import load_dotenv

#main.pyからのパスを設定する
env_path = "./Extend/Extend_env/database.env"

try:
    load_dotenv(env_path)
    db_address = os.environ["db_address"]
    db_database = os.environ["db_database"]
    db_table = os.environ["db_table"]
    db_user = os.environ["db_user"]
    db_passwd = os.environ["db_passwd"]
except Exception as e:
    print(f"環境変数エラー\n{e}")

Engine = create_engine(f"mysql+pymysql://{db_user}:{db_passwd}@{db_address}/{db_table}?charset=utf8")
Base = declarative_base()
Sessionmake = sessionmaker(bind=Engine)
session = Sessionmake()