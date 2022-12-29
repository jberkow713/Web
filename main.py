from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    rating: Optional[int]


@app.get('/')
def home():
    return 'You are home now'

@app.post('/post')
def create_post(post:Post):
    print(post.title)
    return post
    
