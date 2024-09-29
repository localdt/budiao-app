# Rotas relacionadas ao usuário

from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from ..service.sighting_service import SightingService
from ..schema.file_schema import Response
from ..schema.sighting_schema import SightingCreate, Sighting
from ..utils.config import get_async_session
from pathlib import Path
from typing import List

router = APIRouter(prefix="/sightings", tags=['Sighting'])

UPLOAD_DIR = Path("sightings")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload/", response_model=Response)
async def submit_sighting(longitude: float = Form(...), latitude: float = Form(...), files: List[UploadFile] = File(...), db: AsyncSession = Depends(get_async_session)):
    print("======= create sighting in db ======")
    print(longitude)
    print(latitude)
    sighting_data = SightingCreate(latitude=latitude, longitude=longitude, files=files)
    sighting = await SightingService.create_sighting(db, sighting_data)
    print(sighting_data)
    
    print("======= file upload ======")
    #file_path = UPLOAD_DIR / file.filename
    #with file_path.open("wb") as buffer:
    #    buffer.write(await file.read())

    print("======= create file in db ======")
    
    
    return Response(detail="Avistamento cadastrado com sucesso!")

@router.get("/sightings/", response_model=list[Sighting])
async def read_sightings(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_async_session)):
    users = await SightingService.get_sightings(db, skip=skip, limit=limit)
    return users