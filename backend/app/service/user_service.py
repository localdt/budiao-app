 # Funções CRUD
from sqlalchemy.orm import Session
from ..model.user import User
from ..schema.user_schema import UserCreate
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.asyncio import AsyncSession

class UserService:
    async def get_user(db: AsyncSession, user_id: int):
        result = await db.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()

    async def get_user_by_email(db: AsyncSession, email: str):
        result = await db.execute(select(User).filter(User.email == email))
        return result.scalars().first()

    async def get_user_by_id(db: AsyncSession, user_id: int):
        result = await db.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()

    async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10):
        result = await db.execute(select(User).offset(skip).limit(limit))
        return result.scalars().all()

    async def create_user(db: AsyncSession, user: UserCreate):
        hashed_password = generate_password_hash(user.password)
        db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user

    async def delete_user(db: AsyncSession, user_id: int):
        result = db.execute(select(User).filter(User.id == user_id))
        user = result.scalars().first()
        if user:
            await db.delete(user)
            await db.commit()
            return True
        return False

    async def update_user(db: AsyncSession, user_id: int, user: UserCreate):
        result = await db.execute(select(User).filter(User.id == user_id))
        db_user = result.scalars().first() 
        if db_user:
            db_user.name = user.name
            db_user.email = user.email
            db_user.hashed_password = generate_password_hash(user.password)
            await db.commit()
            await db.refresh(db_user)
            return db_user
        return None