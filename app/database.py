from app.core.config import settings


TORTOISE_ORM = {
    "connections": {
        "default":
            {
                'engine': 'tortoise.backends.asyncpg',
                'credentials': {
                    'host': settings.POSTGRES_SERVER,
                    'port': settings.POSTGRES_PORT,
                    'user': settings.POSTGRES_USER,
                    'password': settings.POSTGRES_PASSWORD,
                    'database': settings.POSTGRES_DB,
                }
                }
            },
    "apps": {
        "models": {
            "models": ["aerich.models", "auth.models", "data.models"],
            "default_connection": "default",
        },
    },
}


DB_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': settings.POSTGRES_SERVER,
                'port': settings.POSTGRES_PORT,
                'user': settings.POSTGRES_USER,
                'password': settings.POSTGRES_PASSWORD,
                'database': settings.POSTGRES_DB,
            }
        },
    },
    'apps': {
        'models': {
            'models': ["auth.models", "data.models"],
            'default_connection': 'default',
        }
    }
}