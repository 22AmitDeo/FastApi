from typing import Union
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return "Root Page"

@app.get("/about")
def about():
    return {"data":{"About":"Made by Amit"}}

#Path Parameter 
@app.get("/blog/{id}")
def getid(id:int):
    return{"data":id}

#Query parameter 
@app.get("/items/")
def get_items(name: str, price: float = None):
    return {"name": name, "price": price}