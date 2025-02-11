from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message":"Hello world!"}

#query
@app.get('/greet/{name}')
async def great_name(name:str) ->dict:
    return {"message": f"Hello {name}"}

#Parameters
@app.get('/greet1')
async def great_name1(name:str) ->dict:
    return {"message": f"Hello {name}"}


#Both
@app.get('/greet2/{name}')
async def great_name2(name:str,age: Optional[int]=23) ->dict:
    return {"message":f"Hello {name}, age:{age}"}

class BookCreateModel(BaseModel):
    title : str
    author: str

@app.post('/create_book')
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }