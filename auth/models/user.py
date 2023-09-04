from tortoise import fields
from app.core.models import *


class User(BaseModel):

    """
    The User model, This is the table used to store auth credentails
    """

    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=1000)
    disabled = fields.BooleanField(default=False)

    class PydanticMeta:
        exclude = ["password_hash"]

    def __str__(self):
        return self.email
