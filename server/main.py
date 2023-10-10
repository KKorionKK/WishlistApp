from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.api_router import api_router
from contextlib import asynccontextmanager
from services.database import engine
import logging
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Database metadata initialized")
    yield
    await engine.dispose()
    logging.info("Database engine has been disposed")


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)
