from fastapi import FastAPI, HTTPException
from models import User, Post

app = FastAPI()

Users = []
Posts = []



User1 = User(username = 'Zhenia')
Users.append(User1)
User2 = User(username = 'Andrey')
Users.append(User2)
post1 = Post(author="Zhenia", text='hello it is my first post')
Posts.append(post1)
User1.posts.append(post1)



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
def create_post(postauthor:str,text:str):
    for user in Users:
        if user.username == postauthor:
            new_post = Post(author=user.username,text=text)
            user.posts.append(new_post)
            return new_post
        else:
            raise HTTPException(status_code=404,datail='User not found')


@app.get('/posts')
def get_posts():
    return Posts   


@app.get('/posts/{username}')
def get_userpost(username:str):
    for user in Users:
        if user.username == username:
            return user.posts
        else:
            raise HTTPException(status_code=404,detail='Username not found')  
