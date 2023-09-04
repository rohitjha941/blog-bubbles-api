from tortoise import fields
from app.core.models import *

class Urls(BaseModel):
    link = fields.TextField()

    def __str__(self):
        return self.link