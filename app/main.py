from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from app.core.config import settings

from auth.models import *
from data.models import *
from auth.api import v1
from data.api import v1 as data_v1

def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(v1.router)
    _app.include_router(data_v1.router)

    print(settings.DATABASE_URI)


    DB_CONFIG = {
        'connections': {
            'default': {
                'engine': 'tortoise.backends.asyncpg',
                'credentials': {
                    'host': 'database',
                    'port': '5432',
                    'user': 'postgres',
                    'password': 'postgres',
                    'database': 'app',
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



    @_app.on_event("startup")
    async def startup_event():
        print("Starting up...")
        register_tortoise(
            _app,
            config=DB_CONFIG,
            generate_schemas=False,
            add_exception_handlers=True,
        )

    @_app.on_event("shutdown")
    async def shutdown_event():
        print("Shutting down...")

    return _app


app = get_application()
