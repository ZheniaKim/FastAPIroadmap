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
    
class get_post:
    author:str
    text:str    

User1 = User(username = 'Zhenia')
Users.append(User1)
post1 = Post(author=User1, text='hello it is my first post')
Posts.append(post1)

@app.get('/main')
def get_posts():
    return Posts


@app.post('/creat_user')
def create_user(username:str):
    for user in Users:
        if user.username == username:
            raise HTTPException(status_code=409, detail='Username is in Database')
    new_user = User(username=username)
    Users.append(new_user)
    return {'message': 'username was created'}    
        

@app.get('/users')
def get_Users():
    return Users        


@app.post('/create_post')
def create_post(username:str,text:str):
    user = next((user for user in Users if user.username == username),None)
    if user == None:
        raise HTTPException(status_code=404, detail="user not found")
    new_post = Post(author=user,text=text)
    Posts.append(new_post)
    return new_post.author.username, new_post.text


@app.get('/posts')
def get_posts():
    getpost = []
    for post in Posts:
        getpost.append({post.author.username:post.text})
    return getpost    

