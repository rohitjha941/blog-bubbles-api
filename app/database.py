from app.core.config import settings


TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URI},
    "apps": {
        "models": {
            "models": ["aerich.models"],
            "default_connection": "default",
        },
        "auth": {
            "models": ["auth.models.all"],
            "default_connection": "default",
        }
    },
}
