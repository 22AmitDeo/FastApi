from typing import Optional, Union
from fastapi import FastAPI
from pydantic import BaseModel
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

#Post 
@app.post("/blogs")
def pos(name):
    return {"data": {'within':name}}


#Blog
class Blog(BaseModel):
    title:str
    body: str
    published_at: Optional[bool]
    
@app.post('/blog')
def create_blog(request:Blog):
    return request
