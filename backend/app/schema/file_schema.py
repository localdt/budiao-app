 # Esquemas Pydantic
from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class FileBase(BaseModel):
    filename: str

class Response(BaseModel):
    detail: str
    result: Optional[T] = None

class File(FileBase):
    id: int

    class Config:
        orm_mode = True