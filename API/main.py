#FastAPI関連
from typing import Union
from fastapi import FastAPI

#MySQLに接続するスクリプト
from Extend import table

app = FastAPI()

Wroktime = table.Worktime

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}