from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    rating: Optional[int]

my_posts = [{"title":"title_1", "content":"content_1", "rating":5},
{"title":"title_2", "content":"content_2", "rating":3}]

@app.get('/')
def home():
    return 'You are home now'

@app.get('/post')
def get_post():
    return {"data": my_posts}

@app.post('/post')
def create_post(post:Post):
    print(post.title)
    return post
    
