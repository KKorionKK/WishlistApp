from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from services.config import SettingsDotEnv
from services.models import Base
from sqlalchemy.orm import sessionmaker


settings = SettingsDotEnv().get_settings()
if settings.DATABASE_PORT:
    connection_string = f"{settings.DATABASE_DBMS}://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_URL}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
else:
    connection_string = f"{settings.DATABASE_DBMS}://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_URL}/{settings.DATABASE_NAME}"
engine = create_async_engine(connection_string, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=True)


async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
