# -*- coding:utf-8 -*-
# @Author: clark
# @Time: 2020-03-01 21:39
# @File: test_1.py
# @project demand:
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
