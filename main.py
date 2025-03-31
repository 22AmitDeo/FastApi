from typing import Union
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return "Root Page"

@app.get("/about")
def about():
    return {"data":{"About":"Made by Amit"}}


