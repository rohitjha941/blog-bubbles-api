from tortoise import fields
from app.core.models import *

class Comments(BaseModel):
    position_id = fields.ForeignKeyField('models.PositionalData', related_name='comments')
    user_id = fields.IntField()
    url_id = fields.IntField()
    comment = fields.TextField()
    status = fields.BooleanField(default=True)

    def __str__(self):
        return self.comment