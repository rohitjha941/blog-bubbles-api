from tortoise import fields
from app.core.models import *

class Comments(BaseModel):
    position_id = fields.IntField(null=True)
    user_id = fields.ForeignKeyField('models.User', related_name='comments')
    url_id = fields.IntField()
    comment = fields.TextField()
    status = fields.BooleanField(default=True)
    anchor_text = fields.TextField()

    def __str__(self):
        return self.comment