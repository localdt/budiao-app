 # Esquemas Pydantic
from pydantic import BaseModel
from typing import TypeVar, Optional, List
from fastapi import UploadFile, File

T = TypeVar('T')

class Response(BaseModel):
    detail: str
    result: Optional[T] = None
    
class FileBase(BaseModel):
    name: str
    path: str
    sighting_id: int

class FileCreate(FileBase):
    name: str
    path: str
    sighting_id: int
    
class SightingFile(FileBase):
    id: int

    class Config:
        orm_mode = True
    
class SightingBase(BaseModel):
    longitude: float
    latitude: float

class SightingCreate(SightingBase):    
    pass

class Sighting(SightingBase):
    id: int
    #files: list[File] = []

    class Config:
        orm_mode = True

class SightingForm(BaseModel):
    longitude: float
    latitude: float
    files: List[UploadFile] = File(...)
