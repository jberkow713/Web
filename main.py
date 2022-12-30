from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    rating: Optional[int]
    id: int

my_posts = [{"title":"title_1", "content":"content_1", "rating":5, "id":1},
{"title":"title_2", "content":"content_2", "rating":3, "id":2}]

def Get_post(id):
    id = int(id)
    for p in my_posts:
        if p["id"]==id:
            return p 
    return 'post_id not found'
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

@app.get("/post/latest")
def get_latest():
    return {"latest_post": my_posts[len(my_posts)-1]}

@app.get("/post/{id}")
def get_post(id):
    post = Get_post(id)
    return {"post_detail":post}


    
