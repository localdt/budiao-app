 # Esquemas Pydantic
from pydantic import BaseModel
from typing import TypeVar, Optional, List
from fastapi import UploadFile

T = TypeVar('T')

class File(BaseModel):
    name: str
    path: str

class SightingBase(BaseModel):
    longitude: float
    latitude: float
    #files: List[UploadFile]

class Response(BaseModel):
    detail: str
    result: Optional[T] = None

class SightingCreate(SightingBase):    
    longitude: float
    latitude: float

class Sighting(SightingBase):
    id: int

    class Config:
        orm_mode = True


