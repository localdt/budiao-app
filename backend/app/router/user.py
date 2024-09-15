# Rotas relacionadas ao usuário

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from ..service.user_service import UserService
from ..schema.user_schema import User, UserCreate
from ..utils.config import get_async_session

router = APIRouter(prefix="/users", tags=['User'])

@router.post("/users/", response_model=User)
async def create_user_route(user: UserCreate, db: AsyncSession = Depends(get_async_session)):
    db_user = await UserService.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await UserService.create_user(db=db, user=user)

@router.get("/users/", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_async_session)):
    users = await UserService.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_async_session)):
    db_user = await UserService.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_async_session)):
    result = await delete_user(db, user_id=user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status": "deleted"}

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate, db: AsyncSession = Depends(get_async_session)):
    updated_user = await update_user(db, user_id=user_id, user=user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user