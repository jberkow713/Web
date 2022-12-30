from fastapi import FastAPI, Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import random

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
    
    
@app.get('/')
def home():
    return 'You are home now'

@app.get('/post')
def get_post():
    return {"data": my_posts}

@app.post('/post',status_code=status.HTTP_201_CREATED)
def create_post(post:Post):
    post_dict = post.dict()
    post_dict['rating']=random.randint(0,10)
    post_dict['id']=len(my_posts)+1
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/post/latest")
def get_latest():
    return {"latest_post": my_posts[len(my_posts)-1]}

@app.get("/post/{id}")
def get_post(id):
    post = Get_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,\
            detail=f'id {id} not found')
        
    return {"post_detail":post}

@app.delete("/post/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id):
    id = int(id)
    for p in my_posts:
        if p['id']==id:
            my_posts.remove(p)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='id not found')
