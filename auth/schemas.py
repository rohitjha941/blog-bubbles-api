from .models import *
from pydantic import BaseModel, EmailStr
from typing import Optional


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class RegisterSchema(BaseModel):
    email: EmailStr
    password1: str
    password2: str


class NewPasswordSchema(BaseModel):
    oldpassword1: str
    newpassword1: str
    newpassword2: str
