

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
# Create the asynchronous engine
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Create a sessionmaker that uses AsyncSession
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession  # Ensure the session is asynchronous
)

db = declarative_base()

# Dependency that provides an async session to routes
async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session

async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
