# -*- coding:utf-8 -*-
# @Author: clark
# @Time: 2020-03-01 21:39
# @File: main.py
# @project demand:FastApi增删改查、发送请求返回的2种情况联系
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


if __name__ == '__main__':
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=80)
