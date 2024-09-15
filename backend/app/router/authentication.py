# Rotas relacionadas a autenticação

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from ..service.auth_service import AuthService
from ..schema.auth_schema import Response, Login
from ..utils.config import get_async_session

router = APIRouter(prefix="/auth", tags=['Authentication'])

@router.post("/login", response_model=Response)
async def login(request_body: Login, db: AsyncSession = Depends(get_async_session)):
    login = await AuthService.login_service(db, request_body)
    return Response(detail="Login realizado com sucesso!")