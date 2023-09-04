from tortoise import fields
from app.core.models import *

class PositionalData(BaseModel):
    identifier = fields.JSONField()
    url_id = fields.IntField()

    def __str__(self):
        return self.identifier