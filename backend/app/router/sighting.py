# Rotas relacionadas ao usuário

from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from ..service.sighting_service import SightingService
from ..schema.sighting_schema import SightingCreate, Sighting, Response, FileCreate, SightingFile
from ..utils.config import get_async_session
from pathlib import Path
from typing import List

router = APIRouter(prefix="/sightings", tags=['Sighting'])

UPLOAD_DIR = Path("sightings")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload/", response_model=Response)
async def submit_sighting(longitude: float = Form(...), latitude: float = Form(...), files: List[UploadFile] = File(...), db: AsyncSession = Depends(get_async_session)):
    #TODO rollback the entire transaction in case of error
    #Create sighting
    sighting_data = SightingCreate(latitude=latitude, longitude=longitude)
    sighting = await SightingService.create_sighting(db, sighting_data)
    
    #Create files in the upload folder
    for file in files:    
        file_path = UPLOAD_DIR / file.filename
        file_data = FileCreate(name=file.filename,path=str(file_path), sighting_id = sighting.id)
        with file_path.open("wb") as buffer:
            buffer.write(await file.read())
        
        #Create files in the database associated with the sighting
        sighting_file = await SightingService.create_sighting_file(db, file_data)

    return Response(detail="Avistamento cadastrado com sucesso!")

@router.get("/sightings/", response_model=list[Sighting])
async def read_sightings(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_async_session)):
    sightings = await SightingService.get_sightings(db, skip=skip, limit=limit)
    return sightings


@router.get("/files/", response_model=list[SightingFile])
async def read_sightings_files(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_async_session)):
    sightings_files = await SightingService.get_sightings_files(db, skip=skip, limit=limit)
    return sightings_files