from .models import *
from pydantic import BaseModel, EmailStr
from typing import Optional

class UrlsSchema(BaseModel):
    link: str

class PositionalDataWithCommentsSchema(BaseModel):
    identifier: dict
    url: str
    comment: str
    identifier_id: Optional[int] = None

class PositionalDataSchema(BaseModel):
    comments: str