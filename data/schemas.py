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
    anchor_text: Optional[str] = None

class PositionalDataSchema(BaseModel):
    comments: str

c