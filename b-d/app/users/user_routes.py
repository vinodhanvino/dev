from typing import Optional, List
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from .user_db import User

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

@router.post('/add_user')
def AddUser(request: Request, body: UserCreate):
    try:
        user = User.addUser(
            username=body.username,
            password=body.password,
            email=body.email,
            bio=body.bio,
            profile_picture=body.profile_picture,
            interest=body.interest,
            more=body.more
        )
        return {
            "status": "success",
            "message": "User created successfully",
            "data": user.to_dict()
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "message": str(e)
            }
        )

@router.post('/get_user')
def getUser(request: Request, body: Users):
    try:
        user = User.getUserById(body.id)
        return {
            "status": "success",
            "data": user.to_dict()
        }
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "message": str(e)
            }
        )

@router.post('/list')
def getUsers(request: Request, skip: int = 0, limit: int = 10):
    try:
        result = User.getAllUsers(skip=skip, limit=limit)
        return {
            "status": "success",
            "data": {
                "users": [user.to_dict() for user in result["users"]],
                "total": result["total"],
                "skip": result["skip"],
                "limit": result["limit"]
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "message": str(e)
            }
        )

@router.post('/list_by_interest')
def getUsersByInterest(request: Request, interests: list[str], skip: int = 0, limit: int = 10):
    try:
        # Handle multiple interests by getting results for each interest
        all_users = []
        total = 0
        seen_user_ids = set()  # To track unique users
        
        for interest in interests:
            result = User.getUsersByInterest(interest=interest, skip=0, limit=None)  # Get all matches
            
            # Add only unique users
            for user in result["users"]:
                if user.id not in seen_user_ids:
                    all_users.append(user)
                    seen_user_ids.add(user.id)
                    
        # Apply pagination after combining results
        total = len(all_users)
        paginated_users = all_users[skip:skip + limit]
            
        return {
            "status": "success",
            "data": {
                "users": [user.to_dict() for user in paginated_users],
                "total": total,
                "skip": skip,
                "limit": limit
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "message": str(e)
            }
        )
