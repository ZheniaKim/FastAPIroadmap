from pydantic import BaseModel


class User(BaseModel):
    username:str
    posts : list = []
    friend:list = []


class Post(BaseModel):
    author:str
    text:str    
