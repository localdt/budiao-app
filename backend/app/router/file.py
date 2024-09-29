# Rotas relacionadas ao usuário

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from ..service.user_service import UserService
from ..schema.file_schema import Response
from ..utils.config import get_async_session
from pathlib import Path

router = APIRouter(prefix="/file", tags=['File'])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload/", response_model=Response)
async def upload_file(file: UploadFile = File(...)):
    
    print("======= file upload ======")
    file_path = UPLOAD_DIR / file.filename
    print("======= file_path ======")
    print(file_path)

    with file_path.open("wb") as buffer:
        buffer.write(await file.read())
    return Response(detail="Upload realizado com sucesso!")


@router.get("/download/{file_name}")
async def download_file(file_name: str):
    file_path = UPLOAD_DIR / file_name

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path)