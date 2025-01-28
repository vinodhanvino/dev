from typing import Optional
from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from user_db import User

router = APIRouter()
PREFIX = '/api/v1/users_'

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    bio: str
    profile_picture: str
    interest: list[str]
    more: Optional[dict] = {}

class Users(UserCreate):
    id : int

@router.post('/add_user', response_model=User)
def AddUser(request:Request, body:UserCreate):
    try:

        user = User.addUser(
            username=body.username,
            password = body.password,
            email = body.email,
            bio = body.bio,
            profile_picture = body.profile_picture,
            interest = body.interest,
            more = body.more
        )
    except:
        raise HTTPException()