from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from src.config import settings



class Base(DeclarativeBase):
    pass


engine = create_async_engine(url=settings.DATABASE_URL, echo=True)


async def get_session():
    async_session = async_sessionmaker(bind=engine, expire_on_commit=False) 
    yield async_session


async def init_db():
    async with engine.begin() as conn:
        from src.models import User
        await conn.run_sync(Base.metadata.create_all)
