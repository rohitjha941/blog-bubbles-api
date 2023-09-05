from tortoise import fields
from app.core.models import *

class Comments(BaseModel):
    user_id = fields.IntField()
    url_id = fields.IntField()
    comment = fields.TextField()
    status = fields.BooleanField(default=True)
    identifier = fields.JSONField()

    def __str__(self):
        return self.comment