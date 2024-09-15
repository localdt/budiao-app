 # Funções CRUD
from sqlalchemy.orm import Session

from ..repository.base_repository import BaseRepo
from ..model.user import User
from sqlalchemy.future import select
from ..utils.config import db, commit_rollback
from sqlalchemy.ext.asyncio import AsyncSession

class UsersRepository(BaseRepo):
    async def find_by_username(db: AsyncSession, email: str):
        result = await db.execute(select(User).filter(User.email == email))
        return result.scalars().first()