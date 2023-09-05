from tortoise import fields
from app.core.models import *

class Comments(BaseModel):
    position_id = fields.IntField()
    user_id = fields.IntField()
    url_id = fields.IntField()
    comment = fields.TextField()
    status = fields.BooleanField(default=True)
    archor_text = fields.TextField()

    def __str__(self):
        return self.comment