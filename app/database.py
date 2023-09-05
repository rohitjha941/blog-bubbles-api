from app.core.config import settings


TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "localhost",
                "port": "5432",
                "user": "postgres",
                "password": "postgres",
                "database": "app",
            },
        }
    },
    "apps": {
        "models": {
            "models": ["aerich.models", "auth.models", "data.models"],
            "default_connection": "default",
        },
    },
}
