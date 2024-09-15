 # Funções CRUD
from sqlalchemy.orm import Session

from ..repository.user_repository import UsersRepository
from ..model.user import User
from ..schema.auth_schema import Login
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncSession
from ..service.user_service import UserService
from fastapi import HTTPException
from werkzeug.security import check_password_hash

class AuthService:
    async def login_service(db: AsyncSession, login: Login):
        _user = await UsersRepository.find_by_username(db, login.username)        
        if _user is not None:
           if check_password_hash(_user.hashed_password,login.password):
                return _user
           raise HTTPException(status_code=400, detail="Senha incorreta.")
        raise HTTPException(status_code=404, detail="Usuário não encontrado.") 