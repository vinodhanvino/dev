from typing import Optional
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.users.user_db import User
import hashlib
import os

router = APIRouter()
PREFIX = '/api/v1/session_'


class LoginRequest(BaseModel):
    email: str
    password: str
    more: Optional[dict] = {}


class SessionResponse(BaseModel):
    id: int
    email: str
    token: str

