

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

Base = declarative_base()

# Dependency that provides an async session to routes
async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session

'''


from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import asyncio
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5433/db"

# Create the async engine
async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Create the session
AsyncSessionLocal = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)
Base = declarative_base()
# Dependency to get the session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# This method can be used to ensure that the connection is established properly
async def init_db():
    try:
        async with async_engine.begin() as conn:
            await conn.run_sync(lambda conn: conn.execute("SELECT 1"))
        print("Database connected successfully!")
    except Exception as e:
        print(f"Failed to connect to the database: {e}")

# This method can be used to create all tables if they do not exist
async def create_all_tables():
    from .models import Base  # Replace with your actual models base
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
'''