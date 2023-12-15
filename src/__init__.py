from fastapi import FastAPI
from src.auth.auth_routes import auth_router
from src.config import Settings
from contextlib import asynccontextmanager
from src.config import settings
from src.db import init_db




# lifespan code

@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()

    yield

def create_app():
    app = FastAPI(
        description="This is a simple REST API for a book review service",
        title="Bookly",
        version=settings.VERSION,
        lifespan=lifespan
    )
    app.include_router(auth_router)

    return app


app = create_app()
