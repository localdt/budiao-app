# Rotas relacionadas ao usuário

from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from ..service.sighting_service import SightingService
from ..schema.sighting_schema import SightingCreate, Sighting, Response, FileCreate, SightingFile, SightingForm
from ..utils.config import get_async_session
from pathlib import Path
from typing import List

import os
import json
import requests


service_url = 'http://localhost:5000/classify_inception'

router = APIRouter(prefix="/sightings", tags=['Sighting'])

UPLOAD_DIR = Path("sightings")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload", response_model=Response)
async def submit_sighting(latitude: Annotated[str, Form()], longitude: Annotated[str, Form()], file_uploads: list[UploadFile], db: AsyncSession = Depends(get_async_session)):
    
    try:
        # Create sighting
        sighting_data = SightingCreate(latitude=latitude, longitude=longitude)
        sighting = await SightingService.create_sighting(db, sighting_data)
        sighting_id = sighting.id
        
        # Upload files and create sighting files
        for file in file_uploads:
            save_to = UPLOAD_DIR / file.filename
            # Save file to disk
            with save_to.open("wb") as buffer:
                buffer.write(file.file.read())
            # Create sighting file record in the database
            file_data = FileCreate(name=file.filename, path=str(save_to), sighting_id=sighting_id)
            await SightingService.create_sighting_file(db, file_data)
            
            #Call ML Model - input will be filename
            print("========= call ml ANTES ==========")
            serialized = json.dumps(os.path.join(os.getcwd(), save_to))
            response_ml = requests.post(url=service_url, data=serialized, headers={'content_type':'application/json'})
            print(str(response_ml.content)) # type: ignore
            print("========= call ml DEPOIS ==========")

        return Response(detail="Avistamento cadastrado com sucesso!")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao cadastrar avistamento.")

@router.get("/sightings", response_model=list[Sighting])
async def read_sightings(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_session)):
    sightings = await SightingService.get_sightings(db, skip=skip, limit=limit)
    return sightings


@router.get("/files", response_model=list[SightingFile])
async def read_sightings_files(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_session)):
    sightings_files = await SightingService.get_sightings_files(db, skip=skip, limit=limit)
    return sightings_files

@router.get("/files/{sighting_id}", response_model=list[SightingFile])
async def read_user(sighting_id: int, db: AsyncSession = Depends(get_async_session)):
    sightings_files = await SightingService.get_sightings_files_by_sighting_id(db, sighting_id)
    return sightings_files

@router.get("/sightings/images/{file_id}")
async def get_image(file_id: int, db: AsyncSession = Depends(get_async_session)):
    sightings_file = await SightingService.get_file_by_id(db, file_id)
    filename = sightings_file.name
    file_path = UPLOAD_DIR / filename
    print(file_path)
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(file_path)