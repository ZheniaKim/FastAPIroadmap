from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



app = FastAPI()

Users = []
Posts = []

class User(BaseModel):
    username:str
    posts : list = []
    friend:list = []


class Post(BaseModel):
    author:User
    text:str    
    

@app.get('/main')
def get_posts()
    return Posts


@app.create_user('/creat_user')
def create_user(username:str):
    for user in Users:
        if user.username == username:
            raise HTTPException(status_code=409, detail='Username is in Database')
        else:
            new_user = User(username=username)
            Users.append(new_user)
    return {'message': 'username was created'}        


